import numpy as np
import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity

from preprocessing import build_preprocessing_pipeline


# ============================================================
# AI-BASED PERSONALIZED PROJECT RECOMMENDATION SYSTEM
# RECOMMENDATION ENGINE
# ============================================================


class ProjectRecommender:
    """
    Content-Based Project Recommendation System.

    The system compares a student's profile with project
    descriptions using TF-IDF and Cosine Similarity.
    """

    def __init__(self):
        """
        Initialize the recommendation system.
        """

        print("Loading project recommendation system...")

        # Load and preprocess project dataset
        (
            self.df,
            self.vectorizer,
            self.tfidf_matrix
        ) = build_preprocessing_pipeline()

        print(
            f"Loaded {len(self.df)} projects successfully."
        )

    # ========================================================
    # CREATE STUDENT PROFILE
    # ========================================================

    def create_student_profile(
        self,
        skills,
        interests,
        preferred_domain="",
        difficulty="",
        project_type=""
    ):
        """
        Create a text profile representing the student.

        Parameters:
            skills:
                Student's technical skills.

            interests:
                Student's areas of interest.

            preferred_domain:
                Preferred project domain.

            difficulty:
                Preferred difficulty level.

            project_type:
                Preferred project type.
        """

        profile_parts = []

        # Add skills
        if skills:
            profile_parts.append(
                " ".join(skills)
                if isinstance(skills, list)
                else str(skills)
            )

        # Add interests
        if interests:
            profile_parts.append(
                " ".join(interests)
                if isinstance(interests, list)
                else str(interests)
            )

        # Add domain
        if preferred_domain:
            profile_parts.append(str(preferred_domain))

        # Add difficulty
        if difficulty:
            profile_parts.append(str(difficulty))

        # Add project type
        if project_type:
            profile_parts.append(str(project_type))

        # Combine everything
        student_profile = " ".join(profile_parts)

        return student_profile

    # ========================================================
    # CALCULATE SIMILARITY
    # ========================================================

    def calculate_similarity(self, student_profile):
        """
        Calculate similarity between the student's profile
        and every project in the dataset.
        """

        # Convert student profile into TF-IDF vector
        student_vector = self.vectorizer.transform(
            [student_profile]
        )

        # Calculate cosine similarity
        similarity_scores = cosine_similarity(
            student_vector,
            self.tfidf_matrix
        ).flatten()

        return similarity_scores

    # ========================================================
    # GENERATE RECOMMENDATIONS
    # ========================================================

    def recommend_projects(
        self,
        skills,
        interests,
        preferred_domain="",
        difficulty="",
        project_type="",
        top_n=5
    ):
        """
        Generate personalized project recommendations.

        Returns:
            DataFrame containing the top recommended projects.
        """

        # Create student profile
        student_profile = self.create_student_profile(
            skills=skills,
            interests=interests,
            preferred_domain=preferred_domain,
            difficulty=difficulty,
            project_type=project_type
        )

        # Calculate similarity scores
        similarity_scores = self.calculate_similarity(
            student_profile
        )

        # Copy dataset
        results = self.df.copy()

        # Add similarity scores
        results["Similarity_Score"] = similarity_scores

        # Convert score into percentage
        results["Match_Percentage"] = (
            results["Similarity_Score"] * 100
        )

        # Sort from highest match to lowest match
        results = results.sort_values(
            by="Similarity_Score",
            ascending=False
        )

        # Select top N projects
        recommendations = results.head(top_n).copy()

        # Reset index
        recommendations = recommendations.reset_index(
            drop=True
        )

        # Add recommendation rank
        recommendations.insert(
            0,
            "Rank",
            range(1, len(recommendations) + 1)
        )

        return recommendations

    # ========================================================
    # EXPLANATION
    # ========================================================

    def generate_explanation(
        self,
        recommendation,
        skills,
        interests
    ):
        """
        Generate a simple explanation for why a project
        was recommended.
        """

        required_skills = str(
            recommendation["Required_Skills"]
        ).lower()

        student_skills = []

        if isinstance(skills, list):
            student_skills = skills
        else:
            student_skills = str(skills).split(",")

        matching_skills = []

        for skill in student_skills:
            skill = skill.strip()

            if skill and skill.lower() in required_skills:
                matching_skills.append(skill)

        if matching_skills:
            skill_text = ", ".join(matching_skills)

            return (
                f"Recommended because your profile matches "
                f"the required skills: {skill_text}."
            )

        return (
            "Recommended because the project content is "
            "similar to your selected skills and interests."
        )

    # ========================================================
    # DISPLAY RECOMMENDATIONS
    # ========================================================

    def display_recommendations(
        self,
        recommendations,
        skills,
        interests
    ):
        """
        Display recommendations in a readable format.
        """

        print("\n")
        print("=" * 70)
        print("PERSONALIZED PROJECT RECOMMENDATIONS")
        print("=" * 70)

        for _, project in recommendations.iterrows():

            print(
                f"\n#{int(project['Rank'])} "
                f"{project['Project_Name']}"
            )

            print(
                f"Domain: {project['Domain']}"
            )

            print(
                f"Match Score: "
                f"{project['Match_Percentage']:.2f}%"
            )

            print(
                f"Difficulty: {project['Difficulty']}"
            )

            print(
                f"Project Type: {project['Project_Type']}"
            )

            print(
                f"AI Technique: {project['AI_Technique']}"
            )

            print(
                f"Duration: {project['Duration']}"
            )

            print(
                f"Required Skills: "
                f"{project['Required_Skills']}"
            )

            explanation = self.generate_explanation(
                project,
                skills,
                interests
            )

            print(
                f"Why Recommended: {explanation}"
            )

            print("-" * 70)


# ============================================================
# TEST THE RECOMMENDATION ENGINE
# ============================================================

if __name__ == "__main__":

    print("=" * 70)
    print("AI-BASED PERSONALIZED PROJECT RECOMMENDATION SYSTEM")
    print("=" * 70)

    # --------------------------------------------------------
    # Create recommendation system
    # --------------------------------------------------------

    recommender = ProjectRecommender()

    # --------------------------------------------------------
    # Example student profile
    # --------------------------------------------------------

    skills = [
        "Python",
        "Pandas",
        "NumPy",
        "Machine Learning",
        "Scikit-learn"
    ]

    interests = [
        "Artificial Intelligence",
        "Machine Learning",
        "Recommendation Systems"
    ]

    preferred_domain = "Machine Learning"

    difficulty = "Intermediate"

    project_type = "Prediction"

    # --------------------------------------------------------
    # Generate recommendations
    # --------------------------------------------------------

    recommendations = recommender.recommend_projects(
        skills=skills,
        interests=interests,
        preferred_domain=preferred_domain,
        difficulty=difficulty,
        project_type=project_type,
        top_n=5
    )

    # --------------------------------------------------------
    # Display recommendations
    # --------------------------------------------------------

    recommender.display_recommendations(
        recommendations=recommendations,
        skills=skills,
        interests=interests
    )

    print("\n")
    print("=" * 70)
    print("RECOMMENDATION TEST COMPLETED SUCCESSFULLY")
    print("=" * 70)