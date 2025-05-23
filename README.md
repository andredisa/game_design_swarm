# 🎮 **Game Design Swarm**

>**Game Design Swarm** is an **AI-powered**, collaborative **multi-agent system** that automatically generates a **professional Game Design Document (GDD)** tailored to your unique game ideas. This tool simplifies and accelerates the traditionally time-consuming process of game design, enabling both novice and experienced developers to conceptualize and pitch their ideas efficiently.

---

## ✨ **How It Works**

> **Game Design Swarm** brings together four specialized agents, each focused on a key area of game development. These agents collaborate dynamically to generate a cohesive GDD that covers every major aspect of your game.

Think of them as your personal **game design team**, each handling a different focus:

### 🧙 **Story Agent**
- **`Focus`:** Narrative & World-Building  
- **`Role`:** Craft compelling **storylines**, **character arcs**, and **world-building** to bring your game's universe to life.

### 🕹️ **Gameplay Agent**
- **`Focus`:** Mechanics & Systems  
- **`Role`:** Design **core gameplay loops**, **player progression**, and **game systems** to create an engaging, balanced experience for players.

### 🎨 **Visuals Agent**
- **`Focus`:** Art Direction & Audio Design  
- **`Role`:** Define the **art style**, **visual direction**, and **sound design**, ensuring the aesthetic complements the narrative and gameplay.

### ⚙️ **Tech Agent**
- **`Focus`:** Technical Architecture & Tools  
- **`Role`:** Recommend the **best game engine**, **tools**, and **platforms**, while ensuring optimal **performance** and **scalability**.

---

## 🚀 **Why Game Design Swarm?**

>Gone are the days of spending months on a game design document. With **Game Design Swarm**, you can generate a complete, professional GDD in no time, ready for **prototyping**, **pitching**, or even **early production**.

>The tool is powered by **OpenAI GPT-4** and features an intuitive **Streamlit interface**, allowing you to easily input your game ideas and watch as the agents collaborate in real-time. This streamlined process frees up your time to focus on the creative aspects of game development.

---

## 🧠 **Real-Time AI Collaboration**

>Once you input your game concept, the agents begin working together, integrating their insights into a unified design. You’ll see how the agents interact and update each other’s work, ensuring **consistency** and **cohesion** across every element of the game.

---

## 🌐 **Ideal for Every Developer**

>Whether you're an **indie developer**, part of a **game studio**, or a passionate **gamer** with an idea, **Game Design Swarm** provides an efficient, **AI-driven solution** for turning your game ideas into a professional design document.

>No more juggling endless spreadsheets or disparate notes. **Game Design Swarm** does it all—quickly, professionally, and with the power of advanced AI.

---

## 🚀 **Features**

- 🤖 **Multi-Agent Collaboration**: Seamless hand-offs between agents simulate a real-world game design team.
- 🧠 **Autonomous Context Management**: Agents update and synchronize their knowledge to maintain consistency.
- 🏗️ **Automatic Full GDD Creation**: Generate a comprehensive GDD ready for use in pitching, prototyping, or early-stage production.
- 🎯 **User-Driven Input**: Specify game details like genre, mechanics, and visual style via an intuitive interface.
- 🎨 **Specialized Agent Prompts**: Each agent has unique, domain-specific instructions for high-quality outputs.
- 🖼️ **Interactive UI**: A user-friendly **Streamlit frontend** with dynamic content generation.
- 🛠️ **API Key Integration**: Bring your own **OpenAI API key** for flexible and scalable use.
- 📄 **Modular GDD Outputs**: Review sections (Story, Gameplay, Visuals, Tech) separately in collapsible panels.
- 🔥 **Session Management**: Automatically saves progress for a seamless design process.

---

## 🛠️ Setup

1. **Clone the repository**:

```bash
git clone https://github.com/andredisa/game_design_swarm.git
cd game_design_swarm
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the app:**

```bash
streamlit run streamlit_app.py
```

4. **Provide your OpenAI API Key when prompted.**

---

## 🎯 Usage Instructions
1. Fill in the basic game details via the sidebar inputs.

2. Hit **Start Game Design Swarm**.

3. Watch as each specialized agent contributes to building the document.

4. Download your final Game Design Document.

---

## 📂 Project Structure

```plaintext
game_design_swarm/
│
├── README.md               # 📖 Project documentation
├── requirements.txt        # 📦 Python dependencies
├── streamlit_app.py         # 🚀 Main Streamlit application
│
├── config/
│   └── system_messages.py   # 📜 Agent-specific system prompts and configurations
│
├── agents/
│   ├── story_agent.py       # 🧙 Story creation agent
│   ├── gameplay_agent.py    # 🕹️ Gameplay mechanics agent
│   ├── visuals_agent.py     # 🎨 Visual and audio direction agent
│   └── tech_agent.py        # ⚙️ Technology and development planning agent
│
└── utils/
    ├── context_updates.py   # 🔄 Logic for context synchronization among agents
    └── agent_helpers.py     # 🛠️ Supporting functions for agent operations
```

---
## 🚧 Future Plans

- 🤖 **More specialized agents** (e.g., Marketing, Monetization, Community Building)
- 🎭 **Multiple art style presets** (choose pre-defined artistic themes)
- 🎮 **Game mechanics simulation previews** (basic gameplay flow simulations)
- 📈 **AI-powered project cost & timeline estimations** (budget & scheduling projections)
- 🌐 **Multilingual support** (design documents in different languages)

---

## ✨ Contributing

🎉 **Contributions are more than welcome!**

If you find a bug 🐞, have a feature request ✨, or want to improve the code 💻:

- Open an [Issue](https://github.com/andredisa/game_design_swarm/issues)  
- Submit a [Pull Request](https://github.com/andredisa/game_design_swarm/pulls) 🚀  

>💬 Feel free to reach out on [GitHub](https://github.com/andredisa) or by [email](mailto:andreadisanti22@gmail.com)!

Let’s build this together!

---

## 📜 License

📄 This project is released under the **MIT License**.  
Please refer to the [LICENSE](LICENSE) file for full details.

---

## ☕ Support Me

If you find my work useful and would like to support me, you can buy me a coffee! Your support helps me keep creating and improving my projects. Thank you! 😊

<a href="https://www.buymeacoffee.com/andredisa" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

---

### 🧑‍💻✨ Happy coding
