from langgraph.graph import StateGraph, START, END

from .state import CareerPilotState

from ..agent.nodes import (
    career_recommendation_node,
    skill_gap_node,
    roadmap_node,
    llm_response_node
)


def create_careerpilot_graph():

    graph = StateGraph(CareerPilotState)

    graph.add_node(
        "career_recommendation",
        career_recommendation_node
    )

    graph.add_node(
        "skill_gap_analysis",
        skill_gap_node
    )

    graph.add_node(
        "roadmap_generation",
        roadmap_node
    )

    graph.add_node(
        "ai_response",
        llm_response_node
    )

    graph.add_edge(
        START,
        "career_recommendation"
    )

    graph.add_edge(
        "career_recommendation",
        "skill_gap_analysis"
    )

    graph.add_edge(
        "skill_gap_analysis",
        "roadmap_generation"
    )

    graph.add_edge(
        "roadmap_generation",
        "ai_response"
    )

    graph.add_edge(
        "ai_response",
        END
    )

    return graph.compile()
