from pathlib import Path

import pandas as pd


# ============================================================
# PATH CONFIGURATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "projects.csv"


# ============================================================
# LOAD PROJECT DATA
# ============================================================

def load_project_data():
    """
    Load project recommendation data from projects.csv.
    """

    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"projects.csv not found at: {DATA_FILE}"
        )

    return pd.read_csv(DATA_FILE)


# ============================================================
# TEXT NORMALIZATION
# ============================================================

def normalize_text(value):
    """
    Normalize text for reliable comparison.
    """

    return str(value).strip().lower()


# ============================================================
# SPLIT SKILLS
# ============================================================

def split_skills(value):
    """
    Convert comma-separated skills into a clean list.
    """

    return [
        skill.strip()
        for skill in str(value).split(",")
        if skill.strip()
    ]


# ============================================================
# PROJECT RECOMMENDATION
# ============================================================

def recommend_projects(
    career,
    skill_gaps,
    limit=6
):
    """
    Recommend projects based on:

    1. Selected career
    2. Identified skill gaps
    3. Project skill relevance
    """

    df = load_project_data()

    selected_career = normalize_text(
        career
    )

    user_gaps = {
        normalize_text(skill)
        for skill in skill_gaps
        if str(skill).strip()
    }

    recommendations = []

    # ========================================================
    # ANALYZE EACH PROJECT
    # ========================================================

    for _, row in df.iterrows():

        project_career = normalize_text(
            row.get("career", "")
        )

        # Only recommend projects for selected career
        if project_career != selected_career:
            continue

        project_skills = split_skills(
            row.get("skills", "")
        )

        project_skill_set = {
            normalize_text(skill)
            for skill in project_skills
        }

        # ====================================================
        # FIND MATCHING SKILL GAPS
        # ====================================================

        matched_gap_skills = (
            project_skill_set.intersection(
                user_gaps
            )
        )

        relevance_score = len(
            matched_gap_skills
        )

        recommendations.append(
            {
                "title": str(
                    row.get("title", "")
                ),

                "career": str(
                    row.get("career", "")
                ),

                "difficulty": str(
                    row.get("difficulty", "")
                ),

                "skills": str(
                    row.get("skills", "")
                ),

                "description": str(
                    row.get("description", "")
                ),

                "why": str(
                    row.get("why", "")
                ),

                "matched_gap_skills": [
                    skill
                    for skill in project_skills
                    if normalize_text(skill)
                    in user_gaps
                ],

                "_relevance_score":
                    relevance_score,
            }
        )

    # ========================================================
    # SORT PROJECTS BY RELEVANCE
    # ========================================================

    recommendations.sort(
        key=lambda item: item["_relevance_score"],
        reverse=True
    )

    # ========================================================
    # REMOVE INTERNAL SCORE
    # ========================================================

    for project in recommendations:
        project.pop(
            "_relevance_score",
            None
        )

    # ========================================================
    # RETURN TOP PROJECTS
    # ========================================================

    return recommendations[:limit]