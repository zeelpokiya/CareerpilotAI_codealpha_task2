from pathlib import Path

import pandas as pd


# ============================================================
# PATH CONFIGURATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "careers.csv"


# ============================================================
# LOAD CAREER DATA
# ============================================================

def load_career_data():
    """
    Load career information from careers.csv.
    """

    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"careers.csv not found at: {DATA_FILE}"
        )

    return pd.read_csv(DATA_FILE)


# ============================================================
# TEXT NORMALIZATION
# ============================================================

def normalize_text(value):
    """
    Convert text into a normalized lowercase format.
    """

    return str(value).strip().lower()


# ============================================================
# SPLIT CSV VALUES
# ============================================================

def split_values(value):
    """
    Convert comma-separated CSV values into a list.
    """

    return [
        item.strip()
        for item in str(value).split(",")
        if item.strip()
    ]


# ============================================================
# CAREER RECOMMENDATION ENGINE
# ============================================================

def recommend_careers(
    user_skills,
    user_interests,
    target_role=""
):
    """
    Recommend suitable career paths based on:

    1. Current skills
    2. User interests
    3. Target role

    Returns a ranked list of career recommendations.
    """

    df = load_career_data()

    skills = {
        normalize_text(skill)
        for skill in user_skills
        if str(skill).strip()
    }

    interests = {
        normalize_text(interest)
        for interest in user_interests
        if str(interest).strip()
    }

    target = normalize_text(target_role)

    recommendations = []

    for _, row in df.iterrows():

        career_name = str(
            row.get("career", "")
        ).strip()

        required_skills = split_values(
            row.get("skills", "")
        )

        career_interests = split_values(
            row.get("interests", "")
        )

        required_skill_set = {
            normalize_text(skill)
            for skill in required_skills
        }

        career_interest_set = {
            normalize_text(interest)
            for interest in career_interests
        }

        # ----------------------------------------------------
        # SKILL MATCH
        # ----------------------------------------------------

        matched_skills = skills.intersection(
            required_skill_set
        )

        skill_score = 0

        if required_skill_set:
            skill_score = (
                len(matched_skills)
                / len(required_skill_set)
            ) * 100

        # ----------------------------------------------------
        # INTEREST MATCH
        # ----------------------------------------------------

        matched_interests = interests.intersection(
            career_interest_set
        )

        interest_score = 0

        if career_interest_set:
            interest_score = (
                len(matched_interests)
                / len(career_interest_set)
            ) * 100

        # ----------------------------------------------------
        # TARGET ROLE MATCH
        # ----------------------------------------------------

        target_score = 0

        if target:
            career_text = normalize_text(
                career_name
            )

            if target in career_text:
                target_score = 100

            else:
                target_words = set(
                    target.split()
                )

                career_words = set(
                    career_text.split()
                )

                if target_words.intersection(
                    career_words
                ):
                    target_score = 50

        # ----------------------------------------------------
        # FINAL SCORE
        # ----------------------------------------------------

        if target:
            final_score = (
                skill_score * 0.45
                + interest_score * 0.25
                + target_score * 0.30
            )
        else:
            final_score = (
                skill_score * 0.60
                + interest_score * 0.40
            )

        final_score = round(
            max(0, min(100, final_score)),
            2
        )

        recommendations.append(
            {
                "career": career_name,
                "score": final_score,
                "match_score": final_score,
                "matched_skills": sorted(
                    matched_skills
                ),
                "matched_interests": sorted(
                    matched_interests
                ),
                "required_skills": required_skills,
                "description": str(
                    row.get("description", "")
                ),
            }
        )

    # ========================================================
    # SORT BY BEST MATCH
    # ========================================================

    recommendations.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return recommendations[:5]