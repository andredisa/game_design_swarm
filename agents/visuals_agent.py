# agents/visuals_agent.py

from autogen import SwarmAgent, AFTER_WORK
from utils.context_updates import update_visuals_overview
from utils.agent_helpers import update_system_message_func

def create_visuals_agent(llm_config):
    from autogen import UPDATE_SYSTEM_MESSAGE
    state_update = UPDATE_SYSTEM_MESSAGE(update_system_message_func)

    agent = SwarmAgent(
        "visuals_agent",
        llm_config=llm_config,
        functions=update_visuals_overview,
        update_agent_state_before_reply=[state_update]
    )
    return agent
