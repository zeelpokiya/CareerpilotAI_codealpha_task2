from langgraph.graph import END, START, StateGraph

from .nodes import (
    career_recommendation_node,
    skill_gap_node,
    readiness_node,
    roadmap_node,
    project_recommendation_node,
    llm_response_node,
)

from .state import CareerPilotState


# ============================================================
# CREATE CAREERPILOT AI AGENT
# ============================================================

def create_careerpilot_graph():
    """
    Create and compile the CareerPilot AI agent workflow.

    Workflow:

    START
       ↓
    Career Recommendation
       ↓
    Skill Gap Analysis
       ↓
    Readiness Score
       ↓
    Learning Roadmap
       ↓
    Project Recommendation
       ↓
    AI Response
       ↓
    END
    """

    # --------------------------------------------------------
    # CREATE STATE GRAPH
    # --------------------------------------------------------

    workflow = StateGraph(
        CareerPilotState
    )

    # --------------------------------------------------------
    # ADD AGENT NODES
    # --------------------------------------------------------

    workflow.add_node(
        "career_recommendation",
        career_recommendation_node,
    )

    workflow.add_node(
        "skill_gap_analysis",
        skill_gap_node,
    )

    workflow.add_node(
        "readiness_score",
        readiness_node,
    )

    workflow.add_node(
        "roadmap_generation",
        roadmap_node,
    )

    workflow.add_node(
        "project_recommendation",
        project_recommendation_node,
    )

    workflow.add_node(
        "ai_response",
        llm_response_node,
    )

    # --------------------------------------------------------
    # CONNECT WORKFLOW
    # --------------------------------------------------------

    workflow.add_edge(
        START,
        "career_recommendation",
    )

    workflow.add_edge(
        "career_recommendation",
        "skill_gap_analysis",
    )

    workflow.add_edge(
        "skill_gap_analysis",
        "readiness_score",
    )

    workflow.add_edge(
        "readiness_score",
        "roadmap_generation",
    )

    workflow.add_edge(
        "roadmap_generation",
        "project_recommendation",
    )

    workflow.add_edge(
        "project_recommendation",
        "ai_response",
    )

    workflow.add_edge(
        "ai_response",
        END,
    )

    # --------------------------------------------------------
    # COMPILE GRAPH
    # --------------------------------------------------------

    return workflow.compile()