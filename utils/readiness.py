def calculate_readiness(
    skill_coverage,
    experience="",
    education="",
    target_aligned=True,
):
    """
    Calculate CareerPilot AI Career Readiness Score.

    This is an application-level heuristic for career planning.
    It is NOT a hiring or employment prediction.
    """

    # ============================================================
    # EXPERIENCE SCORE
    # ============================================================

    experience_text = str(
        experience
    ).strip().lower()

    if any(
        keyword in experience_text
        for keyword in [
            "2 year",
            "3 year",
            "4 year",
            "5 year",
            "experienced",
        ]
    ):
        experience_score = 95

    elif any(
        keyword in experience_text
        for keyword in [
            "1 year",
            "internship",
            "intern",
        ]
    ):
        experience_score = 80

    elif "fresher" in experience_text:
        experience_score = 65

    elif experience_text:
        experience_score = 55

    else:
        experience_score = 45

    # ============================================================
    # EDUCATION SCORE
    # ============================================================

    education_text = str(
        education
    ).strip().lower()

    relevant_education_keywords = [
        "bca",
        "b.tech",
        "btech",
        "mca",
        "m.tech",
        "computer",
        "computer science",
        "artificial intelligence",
        "ai",
        "data science",
    ]

    if any(
        keyword in education_text
        for keyword in relevant_education_keywords
    ):
        education_score = 85
    else:
        education_score = 65

    # ============================================================
    # CAREER ALIGNMENT SCORE
    # ============================================================

    alignment_score = (
        90
        if target_aligned
        else 70
    )

    # ============================================================
    # OVERALL READINESS SCORE
    # ============================================================

    overall_score = round(
        (float(skill_coverage) * 0.50)
        + (experience_score * 0.20)
        + (education_score * 0.15)
        + (alignment_score * 0.15)
    )

    # Keep score between 0 and 100

    overall_score = max(
        0,
        min(100, overall_score)
    )

    # ============================================================
    # READINESS LEVEL
    # ============================================================

    if overall_score >= 80:
        level = "Job Ready"

    elif overall_score >= 65:
        level = "Nearly Ready"

    elif overall_score >= 50:
        level = "Developing"

    else:
        level = "Early Stage"

    # ============================================================
    # FINAL RESULT
    # ============================================================

    return {
        "overall": overall_score,
        "skill_readiness": round(
            float(skill_coverage)
        ),
        "experience": experience_score,
        "education": education_score,
        "career_alignment": alignment_score,
        "level": level,
        "note": (
            "This score is an application heuristic "
            "for career planning. It is not a hiring "
            "or employment prediction."
        ),
    }