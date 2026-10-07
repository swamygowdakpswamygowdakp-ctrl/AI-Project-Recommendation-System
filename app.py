import sys
from pathlib import Path

import streamlit as st
import pandas as pd


# ============================================================
# PROJECT PATH SETUP
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))


from recommender import ProjectRecommender
from data.project_roadmaps import get_roadmap


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Project Recommendation System",
    page_icon="🎯",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .recommendation-card {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #dddddd;
        margin-bottom: 15px;
    }

    .match-score {
        font-size: 24px;
        font-weight: bold;
    }

    .roadmap-header {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #dddddd;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    .step-box {
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #dddddd;
        margin-bottom: 12px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOAD RECOMMENDER
# ============================================================

@st.cache_resource
def load_recommender():
    """
    Load the recommendation engine once and cache it.
    """

    return ProjectRecommender()


recommender = load_recommender()


# ============================================================
# SESSION STATE
# ============================================================

if "recommendations" not in st.session_state:
    st.session_state.recommendations = None

if "skills" not in st.session_state:
    st.session_state.skills = []

if "interests" not in st.session_state:
    st.session_state.interests = []

if "selected_roadmap" not in st.session_state:
    st.session_state.selected_roadmap = None

if "selected_project_name" not in st.session_state:
    st.session_state.selected_project_name = None


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">'
    '🎯 AI-Based Personalized Project Recommendation System'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Find project ideas based on your skills, interests, '
    'preferred domain and difficulty level.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("👨‍🎓 Student Profile")

st.sidebar.write(
    "Enter your information to receive personalized "
    "project recommendations."
)


# ============================================================
# SKILLS INPUT
# ============================================================

skills_input = st.sidebar.text_input(
    "Technical Skills",
    placeholder="Example: Python, Pandas, Machine Learning"
)


# ============================================================
# INTERESTS INPUT
# ============================================================

interests_input = st.sidebar.text_input(
    "Interests",
    placeholder="Example: AI, Computer Vision, NLP"
)


# ============================================================
# DOMAIN
# ============================================================

domain_options = [
    "Any",
    "Machine Learning",
    "Computer Vision",
    "Natural Language Processing",
    "Recommender Systems",
    "Artificial Intelligence",
    "Data Science",
    "Cloud Computing"
]

preferred_domain = st.sidebar.selectbox(
    "Preferred Domain",
    domain_options
)


# ============================================================
# DIFFICULTY
# ============================================================

difficulty_options = [
    "Any",
    "Beginner",
    "Intermediate",
    "Advanced"
]

difficulty = st.sidebar.selectbox(
    "Preferred Difficulty",
    difficulty_options
)


# ============================================================
# PROJECT TYPE
# ============================================================

project_type_options = [
    "Any",
    "Prediction",
    "Classification",
    "Recommendation",
    "Clustering",
    "Data Analysis",
    "Image Classification",
    "Object Detection",
    "Text Analysis",
    "Forecasting"
]

project_type = st.sidebar.selectbox(
    "Preferred Project Type",
    project_type_options
)


# ============================================================
# NUMBER OF RECOMMENDATIONS
# ============================================================

top_n = st.sidebar.slider(
    "Number of Recommendations",
    min_value=3,
    max_value=10,
    value=5
)


# ============================================================
# RECOMMEND BUTTON
# ============================================================

recommend_button = st.sidebar.button(
    "🚀 Get Recommendations",
    use_container_width=True
)


# ============================================================
# CLEAR ROADMAP BUTTON
# ============================================================

if st.session_state.selected_roadmap is not None:

    if st.sidebar.button(
        "❌ Close Project Roadmap",
        use_container_width=True
    ):
        st.session_state.selected_roadmap = None
        st.session_state.selected_project_name = None
        st.rerun()


# ============================================================
# GENERATE RECOMMENDATIONS
# ============================================================

if recommend_button:

    # --------------------------------------------------------
    # Validate input
    # --------------------------------------------------------

    if not skills_input.strip() and not interests_input.strip():

        st.warning(
            "⚠️ Please enter at least your skills or interests."
        )

        st.stop()

    # --------------------------------------------------------
    # Convert input into lists
    # --------------------------------------------------------

    skills = [
        skill.strip()
        for skill in skills_input.split(",")
        if skill.strip()
    ]

    interests = [
        interest.strip()
        for interest in interests_input.split(",")
        if interest.strip()
    ]

    # --------------------------------------------------------
    # Convert 'Any' into empty values
    # --------------------------------------------------------

    selected_domain = (
        ""
        if preferred_domain == "Any"
        else preferred_domain
    )

    selected_difficulty = (
        ""
        if difficulty == "Any"
        else difficulty
    )

    selected_project_type = (
        ""
        if project_type == "Any"
        else project_type
    )

    # --------------------------------------------------------
    # Generate recommendations
    # --------------------------------------------------------

    with st.spinner(
        "🤖 Analyzing your profile and finding "
        "the best projects..."
    ):

        recommendations = recommender.recommend_projects(
            skills=skills,
            interests=interests,
            preferred_domain=selected_domain,
            difficulty=selected_difficulty,
            project_type=selected_project_type,
            top_n=top_n
        )

    # --------------------------------------------------------
    # Save recommendations in session state
    # --------------------------------------------------------

    st.session_state.recommendations = recommendations
    st.session_state.skills = skills
    st.session_state.interests = interests

    # Close previously opened roadmap
    st.session_state.selected_roadmap = None
    st.session_state.selected_project_name = None

    st.rerun()


# ============================================================
# INFORMATION SECTION
# ============================================================

if st.session_state.recommendations is None:

    st.info(
        "👈 Enter your skills and interests in the sidebar, "
        "then click **Get Recommendations**."
    )

    st.markdown("## How the System Works")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            ### 1️⃣ Student Profile

            The system collects your:

            - Skills
            - Interests
            - Preferred domain
            - Difficulty
            - Project type
            """
        )

    with col2:

        st.markdown(
            """
            ### 2️⃣ AI Matching

            The system uses:

            - Text preprocessing
            - TF-IDF
            - Cosine Similarity
            - Content-Based Filtering
            """
        )

    with col3:

        st.markdown(
            """
            ### 3️⃣ Recommendations

            The system ranks projects and
            displays the most relevant
            project ideas with match scores.
            """
        )

    st.markdown("---")

    st.markdown("## 🚀 What You Can Do Next")

    st.markdown(
        """
        After receiving a recommendation, you can start a
        **practical project roadmap** containing:

        - Requirements
        - Dataset
        - Dataset location
        - Folder structure
        - Setup commands
        - Implementation steps
        - Run commands
        - Testing
        - Common errors
        - Final checklist
        """
    )

    st.markdown("---")

    st.markdown("## 📊 System Information")

    info_col1, info_col2, info_col3 = st.columns(3)

    with info_col1:

        st.metric(
            "Projects",
            "60"
        )

    with info_col2:

        st.metric(
            "TF-IDF Features",
            "1,134"
        )

    with info_col3:

        st.metric(
            "Recommendation Method",
            "Content-Based"
        )


# ============================================================
# DISPLAY RECOMMENDATIONS
# ============================================================

if st.session_state.recommendations is not None:

    recommendations = st.session_state.recommendations
    skills = st.session_state.skills
    interests = st.session_state.interests

    # ========================================================
    # RESULTS HEADER
    # ========================================================

    st.success(
        f"Found {len(recommendations)} personalized "
        f"project recommendations!"
    )

    st.markdown("## 🎯 Recommended Projects")

    st.info(
        "💡 Click **🚀 Start Project Roadmap** on any project "
        "to see exactly how to build it step by step."
    )

    # ========================================================
    # DISPLAY RECOMMENDATIONS
    # ========================================================

    for _, project in recommendations.iterrows():

        project_name = project["Project_Name"]

        match_percentage = project[
            "Match_Percentage"
        ]

        # ----------------------------------------------------
        # Recommendation card
        # ----------------------------------------------------

        st.markdown(
            f"""
            <div class="recommendation-card">

            <h3>
            #{int(project["Rank"])}
            {project_name}
            </h3>

            <p class="match-score">
            Match Score: {match_percentage:.2f}%
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        # ----------------------------------------------------
        # Project details
        # ----------------------------------------------------

        col1, col2, col3 = st.columns(3)

        with col1:

            st.write(
                f"**Domain:** {project['Domain']}"
            )

        with col2:

            st.write(
                f"**Difficulty:** {project['Difficulty']}"
            )

        with col3:

            st.write(
                f"**Duration:** {project['Duration']}"
            )

        col4, col5 = st.columns(2)

        with col4:

            st.write(
                f"**Project Type:** "
                f"{project['Project_Type']}"
            )

        with col5:

            st.write(
                f"**AI Technique:** "
                f"{project['AI_Technique']}"
            )

        st.write(
            f"**Required Skills:** "
            f"{project['Required_Skills']}"
        )

        st.write(
            f"**Description:** "
            f"{project['Description']}"
        )

        # ----------------------------------------------------
        # Explanation
        # ----------------------------------------------------

        explanation = recommender.generate_explanation(
            project,
            skills,
            interests
        )

        st.info(
            f"💡 **Why this project was recommended:** "
            f"{explanation}"
        )

        # ====================================================
        # PROJECT ROADMAP BUTTON
        # ====================================================

        roadmap_button = st.button(
            "🚀 Start Project Roadmap",
            key=f"roadmap_{project_name}",
            use_container_width=True
        )

        if roadmap_button:

            st.session_state.selected_project_name = project_name

            st.session_state.selected_roadmap = (
                get_roadmap(project_name)
            )

            st.rerun()

        st.markdown("---")


    # ========================================================
    # RESULTS TABLE
    # ========================================================

    st.markdown("## 📋 Recommendation Summary")

    summary_columns = [
        "Rank",
        "Project_Name",
        "Domain",
        "Difficulty",
        "Project_Type",
        "Match_Percentage"
    ]

    summary = recommendations[
        summary_columns
    ].copy()

    summary["Match_Percentage"] = (
        summary["Match_Percentage"].round(2)
    )

    summary = summary.rename(
        columns={
            "Project_Name": "Project",
            "Project_Type": "Type",
            "Match_Percentage": "Match %"
        }
    )

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )


    # ========================================================
    # MATCH SCORE CHART
    # ========================================================

    st.markdown("## 📊 Match Score Comparison")

    chart_data = recommendations[
        ["Project_Name", "Match_Percentage"]
    ].copy()

    chart_data = chart_data.set_index(
        "Project_Name"
    )

    st.bar_chart(
        chart_data
    )


    # ========================================================
    # PROFILE SUMMARY
    # ========================================================

    st.markdown("## 👤 Your Profile")

    profile_col1, profile_col2 = st.columns(2)

    with profile_col1:

        st.write("**Technical Skills**")

        if skills:

            st.write(
                ", ".join(skills)
            )

        else:

            st.write("Not specified")

    with profile_col2:

        st.write("**Interests**")

        if interests:

            st.write(
                ", ".join(interests)
            )

        else:

            st.write("Not specified")


# ============================================================
# PROJECT ROADMAP
# ============================================================

if st.session_state.selected_roadmap is not None:

    roadmap = st.session_state.selected_roadmap
    project_name = st.session_state.selected_project_name

    st.markdown("---")

    st.markdown(
        f"""
        <div class="roadmap-header">

        <h1>🚀 {project_name}</h1>

        <p>
        Practical Project-Building Roadmap
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    # ========================================================
    # ROADMAP OVERVIEW
    # ========================================================

    st.markdown("## 📌 What You Will Build")

    st.write(
        roadmap.get(
            "overview",
            "Build this project as a complete working application."
        )
    )

    # ========================================================
    # ROADMAP INFORMATION
    # ========================================================

    info_col1, info_col2 = st.columns(2)

    with info_col1:

        st.metric(
            "Difficulty",
            roadmap.get(
                "difficulty",
                "Intermediate"
            )
        )

    with info_col2:

        st.metric(
            "Estimated Time",
            roadmap.get(
                "estimated_time",
                "5–8 hours"
            )
        )

    # ========================================================
    # REQUIREMENTS
    # ========================================================

    st.markdown("## 🛠️ Requirements")

    requirements = roadmap.get(
        "requirements",
        []
    )

    for requirement in requirements:

        st.checkbox(
            requirement,
            key=f"requirement_{project_name}_{requirement}"
        )

    # ========================================================
    # LIBRARIES
    # ========================================================

    st.markdown("## 📦 Required Libraries")

    libraries = roadmap.get(
        "libraries",
        []
    )

    if libraries:

        st.code(
            "pip install " + " ".join(libraries),
            language="powershell"
        )

    # ========================================================
    # DATASET
    # ========================================================

    st.markdown("## 📊 Dataset")

    dataset = roadmap.get(
        "dataset",
        {}
    )

    if isinstance(dataset, dict):

        dataset_name = dataset.get(
            "name",
            "Project dataset"
        )

        dataset_source = dataset.get(
            "source",
            "Public dataset"
        )

        dataset_file = dataset.get(
            "file",
            "project_data.csv"
        )

        dataset_placement = dataset.get(
            "placement",
            "data/project_data.csv"
        )

        st.write(
            f"**Dataset:** {dataset_name}"
        )

        st.write(
            f"**Source:** {dataset_source}"
        )

        st.write(
            f"**File:** `{dataset_file}`"
        )

        st.write(
            f"**Place it here:** `{dataset_placement}`"
        )

        st.warning(
            "📌 Download the dataset before starting the "
            "implementation steps."
        )

    # ========================================================
    # FOLDER STRUCTURE
    # ========================================================

    st.markdown("## 📁 Folder Structure")

    folder_structure = roadmap.get(
        "folder_structure",
        ""
    )

    if folder_structure:

        st.code(
            folder_structure,
            language="text"
        )

    # ========================================================
    # PRACTICAL STEPS
    # ========================================================

    st.markdown("## 🧑‍💻 Step-by-Step Project Building")

    steps = roadmap.get(
        "steps",
        []
    )

    total_steps = len(steps)

    completed_steps = 0

    for step_data in steps:

        step_number = step_data.get(
            "step",
            0
        )

        title = step_data.get(
            "title",
            f"Step {step_number}"
        )

        step_key = (
            f"step_{project_name}_"
            f"{step_number}"
        )

        st.markdown(
            f"""
            <div class="step-box">

            <h3>
            Step {step_number}: {title}
            </h3>

            </div>
            """,
            unsafe_allow_html=True
        )

        # ----------------------------------------------------
        # Actions
        # ----------------------------------------------------

        actions = step_data.get(
            "actions",
            []
        )

        if actions:

            for action in actions:

                st.write(
                    f"➡️ {action}"
                )

        # ----------------------------------------------------
        # Commands
        # ----------------------------------------------------

        commands = step_data.get(
            "commands",
            []
        )

        if commands:

            st.markdown("**Run these commands:**")

            st.code(
                "\n".join(commands),
                language="powershell"
            )

        # ----------------------------------------------------
        # Single command
        # ----------------------------------------------------

        command = step_data.get(
            "command"
        )

        if command:

            st.markdown("**Run:**")

            st.code(
                command,
                language="powershell"
            )

        # ----------------------------------------------------
        # Expected result
        # ----------------------------------------------------

        expected = step_data.get(
            "expected"
        )

        if expected:

            st.success(
                f"✅ Expected result: {expected}"
            )

        # ----------------------------------------------------
        # Completion checkbox
        # ----------------------------------------------------

        if st.checkbox(
            f"Step {step_number} completed",
            key=step_key
        ):

            completed_steps += 1

        st.markdown("---")

    # ========================================================
    # PROGRESS
    # ========================================================

    st.markdown("## 📈 Project Progress")

    if total_steps > 0:

        progress = (
            completed_steps / total_steps
        )

        st.progress(progress)

        st.write(
            f"**{completed_steps} / {total_steps} steps completed**"
        )

        if completed_steps == total_steps:

            st.success(
                "🎉 All roadmap steps are completed!"
            )

    # ========================================================
    # COMMON ERRORS
    # ========================================================

    st.markdown("## ⚠️ Common Errors & Fixes")

    common_errors = roadmap.get(
        "common_errors",
        []
    )

    if common_errors:

        for error_data in common_errors:

            error_name = error_data.get(
                "error",
                "Error"
            )

            fix = error_data.get(
                "fix",
                "Check the terminal error message."
            )

            with st.expander(
                f"❌ {error_name}"
            ):

                st.write(
                    f"**Fix:** {fix}"
                )

    # ========================================================
    # FINAL CHECKLIST
    # ========================================================

    st.markdown("## ✅ Final Project Checklist")

    final_checklist = roadmap.get(
        "final_checklist",
        []
    )

    for index, item in enumerate(
        final_checklist
    ):

        st.checkbox(
            item,
            key=f"final_{project_name}_{index}"
        )

    # ========================================================
    # FINISH ROADMAP
    # ========================================================

    st.markdown("---")

    st.success(
        "🎯 When every item is completed, your project "
        "should be ready for final testing and GitHub."
    )

    if st.button(
        "⬆️ Back to Recommended Projects",
        use_container_width=True
    ):

        st.session_state.selected_roadmap = None
        st.session_state.selected_project_name = None

        st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "AI-Based Personalized Project Recommendation System "
    "| Content-Based Filtering | TF-IDF | Cosine Similarity "
    "| Practical Project Roadmaps"
)