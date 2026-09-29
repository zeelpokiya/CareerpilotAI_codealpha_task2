def generate_basic_roadmap(career, skill_gaps):
    """
    Generate a practical learning roadmap
    based on selected career and identified skill gaps.
    """

    career = str(career).strip()

    gaps = []

    for skill in skill_gaps:
        skill = str(skill).strip()

        if skill and skill not in gaps:
            gaps.append(skill)

    roadmap = []

    # ============================================================
    # PHASE 1 — FOUNDATION
    # ============================================================

    roadmap.append(
        {
            "phase": "Phase 1",
            "title": "Foundation Building",
            "duration": "2-3 Weeks",
            "topics": [
                "Python Programming",
                "Problem Solving",
                "Git and GitHub",
                "Basic Data Structures",
            ],
        }
    )

    # ============================================================
    # PHASE 2 — SKILL GAP DEVELOPMENT
    # ============================================================

    if gaps:
        roadmap.append(
            {
                "phase": "Phase 2",
                "title": "Skill Gap Development",
                "duration": "3-4 Weeks",
                "topics": gaps[:6],
            }
        )

    else:
        roadmap.append(
            {
                "phase": "Phase 2",
                "title": "Core Technical Skills",
                "duration": "3-4 Weeks",
                "topics": [
                    "Machine Learning",
                    "Data Analysis",
                    "Model Evaluation",
                    "Practical AI Development",
                ],
            }
        )

    # ============================================================
    # PHASE 3 — PROJECT DEVELOPMENT
    # ============================================================

    roadmap.append(
        {
            "phase": "Phase 3",
            "title": "Practical Project Development",
            "duration": "3-4 Weeks",
            "topics": [
                f"Build a {career} project",
                "Dataset Collection and Preprocessing",
                "Model Development",
                "Model Evaluation",
                "Streamlit or API Deployment",
            ],
        }
    )

    # ============================================================
    # PHASE 4 — CAREER PREPARATION
    # ============================================================

    roadmap.append(
        {
            "phase": "Phase 4",
            "title": "Portfolio and Career Preparation",
            "duration": "2-3 Weeks",
            "topics": [
                "GitHub Portfolio",
                "Resume Preparation",
                "LinkedIn Profile",
                "Project Documentation",
                "Interview Preparation",
            ],
        }
    )

    return roadmap