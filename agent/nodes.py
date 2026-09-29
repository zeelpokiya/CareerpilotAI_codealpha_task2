from utils.career_engine import recommend_careers
from utils.skill_analyzer import analyze_skill_gap
from utils.roadmap import generate_basic_roadmap
from utils.readiness import calculate_readiness
from utils.project_recommender import recommend_projects


def career_recommendation_node(state):
    recommendations = recommend_careers(
        user_skills=state.get("skills", []),
        user_interests=state.get("interests", []),
        target_role=state.get("target_role", ""),
    )
    state["career_recommendations"] = recommendations
    return state


def skill_gap_node(state):
    recommendations = state.get("career_recommendations", [])

    if not recommendations:
        state["skill_gaps"] = []
        return state

    best_career = recommendations[0].get("career", "")

    gaps = analyze_skill_gap(
        current_skills=state.get("skills", []),
        target_career=best_career,
    )

    state["skill_gaps"] = gaps
    return state


def readiness_node(state):
    recommendations = state.get("career_recommendations", [])
    best_career = recommendations[0].get("career", "") if recommendations else ""

    current_skills = state.get("skills", [])
    skill_gaps = state.get("skill_gaps", [])

    total_skills = len(current_skills) + len(skill_gaps)
    skill_coverage = (len(current_skills) / total_skills) * 100 if total_skills else 0

    target_role = str(state.get("target_role", "")).strip().lower()
    career_name = str(best_career).strip().lower()

    target_aligned = True

    if target_role and career_name:
        target_words = set(target_role.split())
        career_words = set(career_name.split())
        target_aligned = bool(target_words.intersection(career_words))

    readiness = calculate_readiness(
        skill_coverage=skill_coverage,
        experience=state.get("experience", ""),
        education=state.get("education", ""),
        target_aligned=target_aligned,
    )

    state["readiness"] = readiness
    state["skill_analysis"] = {
        "current_skills": current_skills,
        "skill_gaps": skill_gaps,
        "skill_coverage": round(skill_coverage),
    }

    return state


def roadmap_node(state):
    recommendations = state.get("career_recommendations", [])

    if not recommendations:
        state["roadmap"] = []
        return state

    career = recommendations[0].get("career", "")

    state["roadmap"] = generate_basic_roadmap(
        career=career,
        skill_gaps=state.get("skill_gaps", []),
    )

    return state


def project_recommendation_node(state):
    recommendations = state.get("career_recommendations", [])

    if not recommendations:
        state["project_recommendations"] = []
        return state

    best_career = recommendations[0].get("career", "")

    state["project_recommendations"] = recommend_projects(
        career=best_career,
        skill_gaps=state.get("skill_gaps", []),
        limit=6,
    )

    return state


def llm_response_node(state):
    recommendations = state.get("career_recommendations", [])

    best_career = (
        recommendations[0].get("career", "Not determined")
        if recommendations
        else "Not determined"
    )

    readiness = state.get("readiness", {})
    skill_gaps = state.get("skill_gaps", [])

    gaps_text = ", ".join(skill_gaps) if skill_gaps else "No major skill gaps identified"

    state["final_response"] = (
        f"Career analysis completed for {state.get('name', 'Candidate')}.\n\n"
        f"Recommended Career: {best_career}\n\n"
        f"Readiness Score: {readiness.get('overall', 0)}/100\n\n"
        f"Readiness Level: {readiness.get('level', 'Not determined')}\n\n"
        f"Skill Gaps: {gaps_text}\n\n"
        "Use the Dashboard, Skill Gap, Roadmap, and Projects sections "
        "to view your complete career analysis."
    )

    return state
