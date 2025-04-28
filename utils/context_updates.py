# utils/context_updates.py

from autogen import SwarmResult
import streamlit as st

def update_story_overview(story_summary: str, context_variables: dict) -> SwarmResult:
    context_variables["story"] = story_summary
    st.sidebar.success('Story overview: ' + story_summary)
    return SwarmResult(agent="gameplay_agent", context_variables=context_variables)

def update_gameplay_overview(gameplay_summary: str, context_variables: dict) -> SwarmResult:
    context_variables["gameplay"] = gameplay_summary
    st.sidebar.success('Gameplay overview: ' + gameplay_summary)
    return SwarmResult(agent="visuals_agent", context_variables=context_variables)

def update_visuals_overview(visuals_summary: str, context_variables: dict) -> SwarmResult:
    context_variables["visuals"] = visuals_summary
    st.sidebar.success('Visuals overview: ' + visuals_summary)
    return SwarmResult(agent="tech_agent", context_variables=context_variables)

def update_tech_overview(tech_summary: str, context_variables: dict) -> SwarmResult:
    context_variables["tech"] = tech_summary
    st.sidebar.success('Tech overview: ' + tech_summary)
    return SwarmResult(agent="story_agent", context_variables=context_variables)
