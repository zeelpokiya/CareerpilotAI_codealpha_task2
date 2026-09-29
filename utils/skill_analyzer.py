from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "skills.csv"


def load_skill_data():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"skills.csv not found at: {DATA_FILE}"
        )

    return pd.read_csv(DATA_FILE)


def normalize_text(value):
    return " ".join(
        str(value).strip().lower().split()
    )


def split_skills(value):
    return [
        skill.strip()
        for skill in str(value).split(",")
        if skill.strip()
    ]


def find_career_rows(df, target_career):
    target = normalize_text(target_career)

    careers = df["career"].astype(str)

    exact_match = careers.apply(
        normalize_text
    ) == target

    career_rows = df[exact_match]

    if not career_rows.empty:
        return career_rows

    partial_match = careers.apply(
        normalize_text
    ).str.contains(
        target,
        regex=False,
        na=False
    )

    career_rows = df[partial_match]

    if not career_rows.empty:
        return career_rows

    target_words = set(target.split())

    best_rows = []
    best_score = 0

    for index, career in careers.items():
        career_words = set(
            normalize_text(career).split()
        )

        score = len(
            target_words.intersection(career_words)
        )

        if score > best_score:
            best_score = score
            best_rows = [index]

        elif score == best_score and score > 0:
            best_rows.append(index)

    if best_rows:
        return df.loc[best_rows]

    return df.iloc[0:0]


def analyze_skill_gap(
    current_skills,
    target_career
):
    df = load_skill_data()

    user_skills = {
        normalize_text(skill)
        for skill in current_skills
        if str(skill).strip()
    }

    career_rows = find_career_rows(
        df,
        target_career
    )

    if career_rows.empty:
        return []

    required_skills = []

    for _, row in career_rows.iterrows():
        skills_value = row.get(
            "required_skills",
            ""
        )

        required_skills.extend(
            split_skills(skills_value)
        )

    unique_required_skills = {}

    for skill in required_skills:
        normalized = normalize_text(skill)

        if normalized:
            unique_required_skills[
                normalized
            ] = skill.strip()

    skill_gaps = []

    for normalized, readable in unique_required_skills.items():
        if normalized not in user_skills:
            skill_gaps.append(readable)

    return sorted(
        skill_gaps,
        key=str.lower
    )


def get_skill_analysis(
    current_skills,
    target_career
):
    df = load_skill_data()

    user_skills = {
        normalize_text(skill)
        for skill in current_skills
        if str(skill).strip()
    }

    career_rows = find_career_rows(
        df,
        target_career
    )

    if career_rows.empty:
        return {
            "career": target_career,
            "current_skills": list(current_skills),
            "required_skills": [],
            "skill_gaps": [],
            "matched_skills": [],
            "skill_coverage": 0,
        }

    required_skills = []

    for _, row in career_rows.iterrows():
        required_skills.extend(
            split_skills(
                row.get(
                    "required_skills",
                    ""
                )
            )
        )

    unique_required_skills = {}

    for skill in required_skills:
        normalized = normalize_text(skill)

        if normalized:
            unique_required_skills[
                normalized
            ] = skill.strip()

    matched_skills = []
    skill_gaps = []

    for normalized, readable in unique_required_skills.items():
        if normalized in user_skills:
            matched_skills.append(readable)
        else:
            skill_gaps.append(readable)

    total_required = len(
        unique_required_skills
    )

    if total_required:
        coverage = (
            len(matched_skills)
            / total_required
        ) * 100
    else:
        coverage = 0

    return {
        "career": target_career,
        "current_skills": sorted(
            current_skills,
            key=str.lower
        ),
        "required_skills": sorted(
            unique_required_skills.values(),
            key=str.lower
        ),
        "skill_gaps": sorted(
            skill_gaps,
            key=str.lower
        ),
        "matched_skills": sorted(
            matched_skills,
            key=str.lower
        ),
        "skill_coverage": round(
            coverage
        ),
    }