import re
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


# ============================================================
# AI-BASED PERSONALIZED PROJECT RECOMMENDATION SYSTEM
# PREPROCESSING MODULE
# ============================================================


def load_dataset():
    """
    Load the project dataset from the data folder.
    """

    # Find the project root directory
    project_root = Path(__file__).resolve().parent.parent

    # Dataset location
    dataset_path = project_root / "data" / "project_dataset.csv"

    # Check whether dataset exists
    if not dataset_path.exists():
        raise FileNotFoundError(
            f"Dataset not found at: {dataset_path}"
        )

    # Load CSV
    df = pd.read_csv(dataset_path)

    return df


def clean_text(text):
    """
    Clean text before applying TF-IDF.

    Operations:
    - Convert text to lowercase
    - Remove special characters
    - Remove extra spaces
    """

    if pd.isna(text):
        return ""

    text = str(text).lower()

    # Replace special characters with spaces
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text


def prepare_project_text(df):
    """
    Create a combined text representation for every project.

    Important project attributes are combined because
    content-based recommendation works by comparing
    the content/features of projects with the student's profile.
    """

    df = df.copy()

    # Convert important columns to strings
    text_columns = [
        "Project_Name",
        "Domain",
        "Description",
        "Required_Skills",
        "Project_Type",
        "AI_Technique",
        "Difficulty"
    ]

    for column in text_columns:
        df[column] = df[column].fillna("").astype(str)

    # Create combined project text
    df["combined_text"] = (
        df["Project_Name"] + " "
        + df["Domain"] + " "
        + df["Description"] + " "
        + df["Required_Skills"] + " "
        + df["Project_Type"] + " "
        + df["AI_Technique"] + " "
        + df["Difficulty"]
    )

    # Clean combined text
    df["cleaned_text"] = df["combined_text"].apply(clean_text)

    return df


def create_tfidf_matrix(df):
    """
    Convert project text into numerical TF-IDF vectors.

    TF-IDF:
    Term Frequency - Inverse Document Frequency

    It gives higher importance to useful words and
    lower importance to words that appear too frequently.
    """

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2),
        max_features=5000
    )

    tfidf_matrix = vectorizer.fit_transform(
        df["cleaned_text"]
    )

    return vectorizer, tfidf_matrix


def build_preprocessing_pipeline():
    """
    Complete preprocessing pipeline.

    Returns:
        df              -> processed project dataset
        vectorizer      -> fitted TF-IDF vectorizer
        tfidf_matrix    -> numerical representation of projects
    """

    # Load dataset
    df = load_dataset()

    # Prepare text
    df = prepare_project_text(df)

    # Create TF-IDF matrix
    vectorizer, tfidf_matrix = create_tfidf_matrix(df)

    return df, vectorizer, tfidf_matrix


# ============================================================
# TEST THE MODULE
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("PREPROCESSING MODULE TEST")
    print("=" * 60)

    # Run complete pipeline
    df, vectorizer, tfidf_matrix = build_preprocessing_pipeline()

    print(f"\nTotal Projects: {len(df)}")

    print(f"TF-IDF Matrix Shape: {tfidf_matrix.shape}")

    print(
        f"Number of TF-IDF Features: "
        f"{len(vectorizer.get_feature_names_out())}"
    )

    print("\nSample Cleaned Text:")
    print("-" * 60)

    for i in range(min(3, len(df))):
        print(f"\nProject: {df.iloc[i]['Project_Name']}")
        print(df.iloc[i]["cleaned_text"])

    print("\n" + "=" * 60)
    print("PREPROCESSING TEST COMPLETED SUCCESSFULLY")
    print("=" * 60)