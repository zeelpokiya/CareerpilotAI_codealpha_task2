from datetime import datetime


def generate_career_report(result):
    """
    Generate a complete CareerPilot AI career report
    in Markdown format.
    """

    name = result.get("name", "User")
    education = result.get("education", "Not provided")
    experience = result.get("experience", "Not provided")
    target_role = result.get("target_role", "Not specified")

    skills = result.get("skills", [])
    interests = result.get("interests", [])

    recommendations = result.get(
        "career_recommendations",
        []
    )

    skill_gaps = result.get(
        "skill_gaps",
        []
    )

    readiness = result.get(
        "readiness",
        {}
    )

    roadmap = result.get(
        "roadmap",
        []
    )

    projects = result.get(
        "project_recommendations",
        []
    )

    final_response = result.get(
        "final_response",
        ""
    )

    report = []

    # ============================================================
    # HEADER
    # ============================================================

    report.append("# CareerPilot AI")
    report.append("")
    report.append(
        "## Intelligent Career & Skill Roadmap Report"
    )
    report.append("")

    report.append(
        f"**Generated:** "
        f"{datetime.now().strftime('%d %B %Y, %I:%M %p')}"
    )

    report.append("")

    # ============================================================
    # 1. PROFILE
    # ============================================================

    report.append("## 1. Candidate Profile")
    report.append("")

    report.append(f"- **Name:** {name}")
    report.append(f"- **Education:** {education}")
    report.append(f"- **Experience:** {experience}")
    report.append(f"- **Target Role:** {target_role}")

    report.append("")

    # ============================================================
    # 2. CURRENT SKILLS
    # ============================================================

    report.append("## 2. Current Skills")
    report.append("")

    if skills:

        for skill in skills:
            report.append(
                f"- {skill}"
            )

    else:

        report.append(
            "- No skills provided."
        )

    report.append("")

    # ============================================================
    # 3. INTERESTS
    # ============================================================

    report.append("## 3. Career Interests")
    report.append("")

    if interests:

        for interest in interests:
            report.append(
                f"- {interest}"
            )

    else:

        report.append(
            "- No interests provided."
        )

    report.append("")

    # ============================================================
    # 4. CAREER RECOMMENDATIONS
    # ============================================================

    report.append(
        "## 4. Recommended Career Paths"
    )

    report.append("")

    if recommendations:

        for index, career in enumerate(
            recommendations,
            start=1
        ):

            career_name = career.get(
                "career",
                "Unknown"
            )

            score = career.get(
                "score",
                career.get(
                    "match_score",
                    "N/A"
                )
            )

            report.append(
                f"### {index}. {career_name}"
            )

            report.append(
                f"- **Match Score:** {score}"
            )

            matched_skills = career.get(
                "matched_skills",
                []
            )

            if matched_skills:

                report.append(
                    "- **Matched Skills:** "
                    + ", ".join(matched_skills)
                )

            matched_interests = career.get(
                "matched_interests",
                []
            )

            if matched_interests:

                report.append(
                    "- **Matched Interests:** "
                    + ", ".join(matched_interests)
                )

            description = career.get(
                "description",
                ""
            )

            if description:

                report.append(
                    f"- **Description:** "
                    f"{description}"
                )

            report.append("")

    else:

        report.append(
            "No career recommendations available."
        )

        report.append("")

    # ============================================================
    # 5. READINESS
    # ============================================================

    report.append(
        "## 5. Career Readiness"
    )

    report.append("")

    report.append(
        f"- **Overall Score:** "
        f"{readiness.get('overall', 0)}/100"
    )

    report.append(
        f"- **Readiness Level:** "
        f"{readiness.get('level', 'Not determined')}"
    )

    report.append(
        f"- **Skill Readiness:** "
        f"{readiness.get('skill_readiness', 0)}%"
    )

    report.append(
        f"- **Experience Score:** "
        f"{readiness.get('experience', 0)}%"
    )

    report.append(
        f"- **Education Score:** "
        f"{readiness.get('education', 0)}%"
    )

    report.append(
        f"- **Career Alignment:** "
        f"{readiness.get('career_alignment', 0)}%"
    )

    report.append("")

    # ============================================================
    # 6. SKILL GAP
    # ============================================================

    report.append(
        "## 6. Skill Gap Analysis"
    )

    report.append("")

    if skill_gaps:

        for gap in skill_gaps:

            report.append(
                f"- {gap}"
            )

    else:

        report.append(
            "- No major skill gaps identified."
        )

    report.append("")

    # ============================================================
    # 7. ROADMAP
    # ============================================================

    report.append(
        "## 7. Personalized Learning Roadmap"
    )

    report.append("")

    if roadmap:

        for phase in roadmap:

            phase_name = phase.get(
                "phase",
                "Phase"
            )

            title = phase.get(
                "title",
                ""
            )

            duration = phase.get(
                "duration",
                ""
            )

            report.append(
                f"### {phase_name}: {title}"
            )

            if duration:

                report.append(
                    f"**Duration:** {duration}"
                )

                report.append("")

            topics = phase.get(
                "topics",
                []
            )

            for topic in topics:

                report.append(
                    f"- {topic}"
                )

            report.append("")

    else:

        report.append(
            "No roadmap available."
        )

        report.append("")

    # ============================================================
    # 8. PROJECT RECOMMENDATIONS
    # ============================================================

    report.append(
        "## 8. Recommended Projects"
    )

    report.append("")

    if projects:

        for index, project in enumerate(
            projects,
            start=1
        ):

            title = project.get(
                "title",
                "Project"
            )

            difficulty = project.get(
                "difficulty",
                "Not specified"
            )

            description = project.get(
                "description",
                ""
            )

            why = project.get(
                "why",
                ""
            )

            project_skills = project.get(
                "skills",
                ""
            )

            report.append(
                f"### {index}. {title}"
            )

            report.append(
                f"- **Difficulty:** "
                f"{difficulty}"
            )

            if project_skills:

                report.append(
                    f"- **Skills:** "
                    f"{project_skills}"
                )

            if description:

                report.append(
                    f"- **Description:** "
                    f"{description}"
                )

            if why:

                report.append(
                    f"- **Why this project:** "
                    f"{why}"
                )

            report.append("")

    else:

        report.append(
            "No project recommendations available."
        )

        report.append("")

    # ============================================================
    # 9. AI INSIGHTS
    # ============================================================

    report.append(
        "## 9. AI Career Insights"
    )

    report.append("")

    if final_response:

        report.append(
            final_response
        )

    else:

        report.append(
            "AI insights are not available."
        )

    report.append("")

    # ============================================================
    # 10. RESPONSIBLE AI
    # ============================================================

    report.append(
        "## 10. Responsible AI Disclaimer"
    )

    report.append("")

    report.append(
        "CareerPilot AI provides career-planning guidance "
        "based on the information supplied by the user. "
        "The readiness score is an application-level "
        "heuristic and is not a hiring, employment, "
        "admission, or recruitment prediction."
    )

    report.append("")

    report.append("---")

    report.append(
        "Generated by **CareerPilot AI – "
        "Intelligent Career & Skill Roadmap Assistant**"
    )

    return "\n".join(report)