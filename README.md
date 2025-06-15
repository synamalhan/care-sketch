# 🩺 CareSketch

**CareSketch** is an AI-powered care planning assistant built for social good. It helps caregivers create personalized, goal-based daily care plans from natural language descriptions, enriched with emotion-aware context, risk detection, interactive scheduling, and exportable summaries.

Built during the **Hack the Vibe 2025** hackathon, CareSketch focuses on empowering non-technical caregivers to deliver thoughtful, informed, and emotionally supportive care.

---

## 🌟 Features

- 🧠 **Natural Language to Care Plan**: Generate detailed care plans from simple English descriptions.
- 🎯 **Goal & Emotion-Aware**: Customize the plan based on goals (e.g., pain relief, mobility) and emotional state.
- 💬 **Conversational Emotional Support**: Chat interface for overwhelmed caregivers to receive validation and kindness.
- ⚠️ **Risk Detection**: Highlights potential red flags or clinical risks in the generated plan.
- 📆 **Interactive Timeline**: Visual care schedule with Plotly-based interactive chart.
- 📤 **PDF Export**: Download a clean, printable version of the care plan.
- 🎨 **Beautiful UI**: Gradient backgrounds, themed sidebar, and modern UX with Streamlit's latest features.

---

## 🛠️ Tech Stack

| Component        | Tech |
|------------------|------|
| Frontend         | Streamlit |
| LLM Interface    | Ollama (local inference with `llama3`) |
| Charting         | Plotly |
| PDF Generation   | FPDF / ReportLab (custom module) |
| Risk Detection   | Custom rule-based logic |
| Deployment       | Local or via Streamlit Cloud |

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/synamalhan/care-sketch.git
cd caresketch
```

### 2. Set Up Environment

Make sure you have Python 3.9+ installed.

Install dependencies:

```bash
pip install -r requirements.txt
```

You will also need [Ollama](https://ollama.com/) installed and running locally:

```bash
ollama run llama3
```

### 3. Run the App

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
caresketch/
│
├── app.py                  # Main Streamlit app
├── planner.py              # Query LLM for care plans
├── formatter.py            # Format care plan for display
├── export.py               # PDF generation
├── timeline.py             # Interactive timeline renderer
├── risk.py                 # Risk detection logic
├── resources.py            # Helpful links for caregivers
├── requirements.txt
└── .streamlit/
    └── config.toml         # Theme settings
```

---

## 📦 Requirements

* `streamlit`
* `plotly`
* `fpdf` or `reportlab`
* `ollama` (running locally with a supported model like `llama3`)
* Python 3.9+

Install with:

```bash
pip install -r requirements.txt
```

---

## 🧪 Sample Inputs

You can test the app using built-in scenarios like:

* "A 70-year-old woman with diabetes, knee pain, and limited mobility."
* "An 80-year-old woman with dementia who occasionally wanders."
* "Post-surgery patient recovering from hip replacement, living alone."

---

## 🧠 How It Works

1. **User Input**: The caregiver describes the situation in plain language.
2. **LLM Prompting**: The input is enriched with tone, goals, and emotions before being sent to `llama3` via Ollama.
3. **Plan Structuring**: The model returns a structured JSON with medications, meals, exercises, rest, and notes.
4. **Risk Detection**: Simple rule-based system detects clinical red flags.
5. **Output**: Care plan is rendered in Markdown, JSON, timeline view, and downloadable as PDF.
6. **Chat**: A mental health chatbot responds to emotional input with empathetic messages using a separate Ollama call.

---

## 📚 Resources Panel

CareSketch also includes an expandable section of curated resources such as:

* Support helplines
* Alzheimer’s and dementia guides
* Caregiving forums
* Mental health checklists

---

## 💡 Future Roadmap

* 🔊 **Voice Input**
* 📱 **Mobile Optimization**
* 🧠 **Knowledge Graph Integration**
* 🧾 **Care Plan Validation with Clinical Rules**
* ⏰ **Daily Reminders & Calendar Sync**

---

## 🤝 Team & Acknowledgments

Built by Syna Malhan at [Hack the Vibe 2025](https://hackthevibe.devpost.com).
Special thanks to Open Source LLM tools like [Ollama](https://ollama.com/), and the incredible caregiver communities who inspired this project.

---

## 🛡️ License

MIT License. Free to use, modify, and share for non-commercial caregiving and research purposes.

---

## 💌 Contribute

We welcome contributors! If you’d like to improve CareSketch or adapt it for new caregiving needs:

* Open an issue or feature request.
* Submit a pull request with improvements.
* Or just reach out!

---

> *CareSketch — Empowering caregivers with empathy, structure, and AI.*