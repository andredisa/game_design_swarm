# streamlit_app.py

import streamlit as st
from autogen import Swarm
from agents.story_agent import create_story_agent
from agents.gameplay_agent import create_gameplay_agent
from agents.visuals_agent import create_visuals_agent
from agents.tech_agent import create_tech_agent

st.set_page_config(page_title="Game Design Swarm", page_icon="🎮", layout="wide")

st.title("🎮 Game Design Swarm")
st.write("Collaborative AI agents to assist in building a complete video game design document.")

openai_key = st.text_input("Enter your OpenAI API Key:", type="password")

if openai_key:
    llm_config = {
        "config_list": [
            {
                "model": "gpt-4",  # you can change to gpt-3.5-turbo if needed
                "api_key": openai_key
            }
        ],
        "temperature": 0.7
    }

    st.sidebar.header("Game Design Inputs")
    game_type = st.sidebar.text_input("Game Type (e.g., RPG, FPS, Puzzle):")
    target_audience = st.sidebar.text_input("Target Audience (age group, interests):")
    mood = st.sidebar.text_input("Desired Mood/Atmosphere:")
    perspective = st.sidebar.text_input("Perspective (First Person, Top-Down, etc.):")
    budget = st.sidebar.text_input("Approximate Budget (optional):")

    if st.sidebar.button("Start Game Design Swarm") and game_type and target_audience and mood and perspective:
        context_variables = {
            "game_type": game_type,
            "target_audience": target_audience,
            "mood": mood,
            "perspective": perspective,
            "budget": budget if budget else "Not Specified"
        }

        swarm = Swarm(
            agents=[
                create_story_agent(llm_config),
                create_gameplay_agent(llm_config),
                create_visuals_agent(llm_config),
                create_tech_agent(llm_config),
            ],
            shared_context=context_variables,
        )

        report = swarm.chat()

        st.subheader("📜 Final Game Design Document")
        st.markdown(report.summary, unsafe_allow_html=True)

        st.download_button(
            label="📥 Download Design Document",
            data=report.summary,
            file_name="game_design_document.md",
            mime="text/markdown",
        )
    else:
        st.info("Please fill in all required fields to start.")
else:
    st.warning("Please enter your OpenAI API key to continue.")
