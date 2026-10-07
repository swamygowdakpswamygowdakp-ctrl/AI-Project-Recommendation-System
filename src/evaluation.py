import pandas as pd

from recommender import ProjectRecommender


# ============================================================
# AI-BASED PERSONALIZED PROJECT RECOMMENDATION SYSTEM
# EVALUATION MODULE
# ============================================================


def calculate_precision_at_k(
    recommendations,
    expected_domain,
    k=5
):
    """
    Calculate Precision@K.

    Precision@K =
    Relevant recommendations in Top K / K
    """

    top_k = recommendations.head(k)

    relevant_count = (
        top_k["Domain"] == expected_domain
    ).sum()

    precision = relevant_count / k

    return precision


def calculate_hit_rate_at_k(
    recommendations,
    expected_domain,
    k=5
):
    """
    Calculate Hit Rate@K.

    Returns 1 if at least one relevant project
    appears in the Top K recommendations.
    Otherwise returns 0.
    """

    top_k = recommendations.head(k)

    relevant_count = (
        top_k["Domain"] == expected_domain
    ).sum()

    if relevant_count > 0:
        return 1.0

    return 0.0


def evaluate_profile(
    recommender,
    profile_name,
    skills,
    interests,
    preferred_domain,
    difficulty,
    project_type,
    k=5
):
    """
    Evaluate one student profile.
    """

    recommendations = recommender.recommend_projects(
        skills=skills,
        interests=interests,
        preferred_domain=preferred_domain,
        difficulty=difficulty,
        project_type=project_type,
        top_n=k
    )

    precision = calculate_precision_at_k(
        recommendations,
        expected_domain=preferred_domain,
        k=k
    )

    hit_rate = calculate_hit_rate_at_k(
        recommendations,
        expected_domain=preferred_domain,
        k=k
    )

    average_score = (
        recommendations["Match_Percentage"].mean()
    )

    print("\n" + "=" * 70)
    print(f"PROFILE: {profile_name}")
    print("=" * 70)

    print(f"Expected Domain: {preferred_domain}")

    print("\nTop Recommendations:")

    for _, project in recommendations.iterrows():

        print(
            f"{int(project['Rank'])}. "
            f"{project['Project_Name']} "
            f"({project['Domain']}) - "
            f"{project['Match_Percentage']:.2f}%"
        )

    print(
        f"\nPrecision@{k}: "
        f"{precision:.2f}"
    )

    print(
        f"Hit Rate@{k}: "
        f"{hit_rate:.2f}"
    )

    print(
        f"Average Match Score: "
        f"{average_score:.2f}%"
    )

    return {
        "Profile": profile_name,
        "Expected_Domain": preferred_domain,
        "Precision@K": precision,
        "Hit_Rate@K": hit_rate,
        "Average_Match_Score": average_score
    }


# ============================================================
# MAIN EVALUATION
# ============================================================

if __name__ == "__main__":

    print("=" * 70)
    print("AI-BASED PERSONALIZED PROJECT RECOMMENDATION SYSTEM")
    print("MODEL EVALUATION")
    print("=" * 70)

    # --------------------------------------------------------
    # Initialize recommender
    # --------------------------------------------------------

    recommender = ProjectRecommender()

    # --------------------------------------------------------
    # Test Profiles
    # --------------------------------------------------------

    test_profiles = [

        {
            "profile_name": "Machine Learning Student",

            "skills": [
                "Python",
                "Pandas",
                "NumPy",
                "Scikit-learn",
                "Machine Learning"
            ],

            "interests": [
                "Machine Learning",
                "Prediction",
                "Data Analysis"
            ],

            "preferred_domain": "Machine Learning",

            "difficulty": "Intermediate",

            "project_type": "Prediction"
        },

        {
            "profile_name": "Computer Vision Student",

            "skills": [
                "Python",
                "OpenCV",
                "TensorFlow",
                "CNN",
                "Computer Vision"
            ],

            "interests": [
                "Computer Vision",
                "Image Processing",
                "Deep Learning"
            ],

            "preferred_domain": "Computer Vision",

            "difficulty": "Advanced",

            "project_type": "Image Classification"
        },

        {
            "profile_name": "NLP Student",

            "skills": [
                "Python",
                "NLP",
                "TF-IDF",
                "Scikit-learn"
            ],

            "interests": [
                "Natural Language Processing",
                "Text Processing",
                "Sentiment Analysis"
            ],

            "preferred_domain": "Natural Language Processing",

            "difficulty": "Intermediate",

            "project_type": "Classification"
        },

        {
            "profile_name": "Recommendation System Student",

            "skills": [
                "Python",
                "Pandas",
                "Machine Learning",
                "TF-IDF",
                "Scikit-learn"
            ],

            "interests": [
                "Recommendation Systems",
                "Artificial Intelligence",
                "Personalization"
            ],

            "preferred_domain": "Recommender Systems",

            "difficulty": "Intermediate",

            "project_type": "Recommendation"
        },

        {
            "profile_name": "Data Science Student",

            "skills": [
                "Python",
                "Pandas",
                "NumPy",
                "Matplotlib",
                "Seaborn"
            ],

            "interests": [
                "Data Analysis",
                "Data Visualization",
                "Statistics"
            ],

            "preferred_domain": "Data Science",

            "difficulty": "Beginner",

            "project_type": "Data Analysis"
        }
    ]

    # --------------------------------------------------------
    # Evaluate all profiles
    # --------------------------------------------------------

    evaluation_results = []

    for profile in test_profiles:

        result = evaluate_profile(
            recommender=recommender,
            profile_name=profile["profile_name"],
            skills=profile["skills"],
            interests=profile["interests"],
            preferred_domain=profile["preferred_domain"],
            difficulty=profile["difficulty"],
            project_type=profile["project_type"],
            k=5
        )

        evaluation_results.append(result)

    # --------------------------------------------------------
    # Create evaluation DataFrame
    # --------------------------------------------------------

    results_df = pd.DataFrame(
        evaluation_results
    )

    # --------------------------------------------------------
    # Calculate overall metrics
    # --------------------------------------------------------

    overall_precision = (
        results_df["Precision@K"].mean()
    )

    overall_hit_rate = (
        results_df["Hit_Rate@K"].mean()
    )

    overall_match_score = (
        results_df["Average_Match_Score"].mean()
    )

    # --------------------------------------------------------
    # Display overall results
    # --------------------------------------------------------

    print("\n")
    print("=" * 70)
    print("OVERALL EVALUATION RESULTS")
    print("=" * 70)

    print(
        f"\nAverage Precision@5: "
        f"{overall_precision:.2f}"
    )

    print(
        f"Average Hit Rate@5: "
        f"{overall_hit_rate:.2f}"
    )

    print(
        f"Average Match Score: "
        f"{overall_match_score:.2f}%"
    )

    print("\nDetailed Results:")
    print("-" * 70)

    print(
        results_df.to_string(index=False)
    )

    # --------------------------------------------------------
    # Save evaluation results
    # --------------------------------------------------------

    results_df.to_csv(
        "evaluation_results.csv",
        index=False
    )

    print("\n")
    print("=" * 70)
    print("EVALUATION COMPLETED SUCCESSFULLY")
    print("=" * 70)

    print(
        "\nEvaluation results saved to:"
    )

    print(
        "evaluation_results.csv"
    )