# utils/agent_helpers.py

from config.system_messages import story_agent_prompt, gameplay_agent_prompt, visuals_agent_prompt, tech_agent_prompt

system_messages = {
    "story_agent": story_agent_prompt,
    "gameplay_agent": gameplay_agent_prompt,
    "visuals_agent": visuals_agent_prompt,
    "tech_agent": tech_agent_prompt,
}

def update_system_message_func(agent, messages):
    system_prompt = system_messages[agent.name]

    current_gen = agent.name.split("_")[0]
    if agent._context_variables.get(current_gen) is None:
        system_prompt += f" Call the update function provided to first provide a 2-3 sentence summary of your ideas on {current_gen.upper()} based on the context provided."
        agent.llm_config['tool_choice'] = {"type": "function", "function": {"name": f"update_{current_gen}_overview"}}
    else:
        agent.llm_config["tools"] = None
        agent.llm_config['tool_choice'] = None
        system_prompt += f"\n\nYour task: write the {current_gen} part of the report. No XML tags. Start with: '## {current_gen.capitalize()} Design'."

        k = list(agent._oai_messages.keys())[-1]
        agent._oai_messages[k] = agent._oai_messages[k][:1]

    system_prompt += "\n\nContext for you to refer to:"
    for k, v in agent._context_variables.items():
        if v is not None:
            system_prompt += f"\n{k.capitalize()} Summary:\n{v}"

    return system_prompt
