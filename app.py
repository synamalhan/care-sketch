import streamlit as st
from planner import query_ollama, query_empathy_bot
from formatter import format_plan_for_display
from export import generate_pdf
from timeline import render_timeline_with_interactivity
from risk import detect_risks

st.set_page_config(page_title="CareSketch", layout="wide")

# # Gradient background: white to light teal at a diagonal angle
# st.markdown("""
#     <style>
#     body, .stApp {
#         background: linear-gradient(135deg, #ffffff, #e0f7f7, #b2ebf2, #80deea);
#         background-attachment: fixed;
#     }
#     </style>
# """, unsafe_allow_html=True)
# Header
st.markdown("""
    <h1 style='text-align: center; color: #4F8A8B;'>🩺 CareSketch</h1>
    <p style='text-align: center; font-size: 18px; color: #6c757d;'>
        Your friendly AI caregiver planner. Describe the care needs, and we'll sketch the day with love 💖
    </p>
""", unsafe_allow_html=True)

# Sidebar Input
with st.sidebar:
    st.markdown("## ✍️ Describe Care Scenario")

    # Preset Scenarios
    care_presets = {
        "Elderly Diabetic with Mobility Issues": "A 70-year-old woman with diabetes, knee pain, and limited mobility...",
        "Post-Surgery Hip Replacement": "A middle-aged man recovering from hip surgery who lives alone...",
        "Dementia Patient with Wandering Risk": "An 80-year-old woman with mid-stage dementia who occasionally wanders..."
    }
    preset = st.selectbox("Or choose a preset scenario:", ["None"] + list(care_presets.keys()))

    if preset != "None":
        user_input = care_presets[preset]
    else:
        user_input = st.text_area("Or type here:", height=180, placeholder="e.g. A 70-year-old diabetic woman with knee pain...")

    # Goal-Based Planning
    goals = st.multiselect("Select care goals:", ["Pain Relief", "Mobility", "Cognitive Stimulation", "Better Sleep", "Diet Control"])

    # Tone Selection
    tone = st.radio("Preferred tone of the plan:", ["Compassionate", "Professional", "Simple", "Detailed"])

    # Emotional State
    emotions = st.selectbox("Recipient's emotional state (optional):", ["None", "Anxious", "Depressed", "Irritable", "Happy"])

    # Optional Health Details
    with st.expander("📋 Add optional health details"):
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        has_diabetes = st.checkbox("Diabetic")
        mobility_level = st.select_slider("Mobility Level", options=["Low", "Medium", "High"])

    st.markdown("---")
    st.markdown("🌼 _CareSketch is here to support families and caregivers with empathy and clarity._")
    generate = st.button("🎨 Generate Care Plan")

# Save plan to session state
if generate:
    if not user_input.strip():
        st.warning("Please provide a care description.")
    else:
        # Assemble enriched input
        enriched_input = f"Care Scenario: {user_input}\n"
        if goals:
            enriched_input += f"Goals: {', '.join(goals)}\n"
        if emotions != "None":
            enriched_input += f"Emotional State: {emotions}\n"
        enriched_input += f"Tone: {tone}\n"
        enriched_input += f"Age: {age if age else 'Not provided'}\n"
        enriched_input += f"Mobility: {mobility_level}\n"
        if has_diabetes:
            enriched_input += "Has diabetes\n"

        with st.spinner("Sketching a personalized care plan... 🎨"):
            plan = query_ollama(enriched_input)

            if "error" in plan:
                st.error("⚠️ Error generating plan: " + plan["error"])
            else:
                st.session_state.generated_plan = plan

# Main Display (render if plan exists)
if "generated_plan" in st.session_state:
    plan = st.session_state.generated_plan

    # Display formatted care plan
    with st.expander("📝 View Care Plan Details", expanded=True):
        st.markdown(format_plan_for_display(plan), unsafe_allow_html=True)

    # # Show raw JSON
    # with st.expander("📋 Care Plan Breakdown", expanded=False):
    #     st.markdown("### 🧩 Raw Plan JSON")
    #     st.json(plan)

    # Summary
    st.markdown("### 🌟 Care Summary")
    st.markdown(f"""
    - **Total Medications:** {len(plan.get("medications", []))}
    - **Meals Planned:** {len(plan.get("meals", []))}
    - **Exercises Included:** {len(plan.get("exercise", []))}
    - **Rest Entries:** {len(plan.get("rest", []))}
    """)

    # Risk Detection
    st.markdown("---")
    st.subheader("🚨 Risk & Red Flag Detection")
    risks = detect_risks(plan)
    if risks:
        for risk in risks:
            st.error(risk)
    else:
        st.success("✅ No major risks detected in the care plan.")

    # Timeline
    st.markdown("---")
    st.subheader("📆 Interactive Care Plan Timeline (5-Day View)")
    fig = render_timeline_with_interactivity(plan, num_days=5)
    st.plotly_chart(fig, use_container_width=True)

    # Emotional Support Chatbot
    with st.expander("💬 Immediate Emotional Support", expanded=False):
        st.markdown("""
            Sometimes caregiving can feel overwhelming. This space is here to comfort and support you 💗  
            Feel free to chat with CareSketch Bot — your empathetic companion.
        """)

        # Initialize chat history
        if "emotional_chat" not in st.session_state:
            st.session_state.emotional_chat = [
                {"role": "assistant", "content": "Hi there 👋 I'm here to support you. What's on your mind?"}
            ]

        # Display chat messages
        for msg in st.session_state.emotional_chat:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        # Accept user input
        user_msg = st.chat_input("Share your thoughts or ask for encouragement...")

        if user_msg:
            st.session_state.emotional_chat.append({"role": "user", "content": user_msg})

            with st.chat_message("user"):
                st.markdown(user_msg)

            # Generate empathetic response using Ollama
            response = query_empathy_bot(
                f"You are a compassionate mental health assistant. A caregiver says: '{user_msg}'. "
                "Respond with emotional validation, empathy, and kindness to help them feel heard and supported."
            )
            st.session_state.emotional_chat.append({"role": "assistant", "content": response})

            with st.chat_message("assistant"):
                st.markdown(response)

    # Additional Resources Section
    with st.expander("📚 Resources & Support Links", expanded=False):
        st.markdown("""
        If you're feeling overwhelmed, remember you're not alone. Here are some resources for support, caregiving advice, and mental health:

        - 🧠 [Mental Health America](https://www.mhanational.org/) – Mental health tools and support.
        - ❤️ [Caregiver Action Network](https://www.caregiveraction.org/) – Resources for family caregivers.
        - ☎️ [Crisis Text Line](https://www.crisistextline.org/) – Text HOME to 741741 to connect with a crisis counselor.
        - 🏥 [Mayo Clinic Caregiver Guide](https://www.mayoclinic.org/healthy-lifestyle/stress-management/in-depth/caregiver-stress/art-20044784) – Articles on caregiver stress and self-care.
        - 🛏️ [DailyCaring](https://dailycaring.com/) – Practical caregiving tips and routines.

        > 💬 _You are doing your best. Please take care of yourself too._ 🌷
        """)

    # Export
    with st.expander("📤 Export Care Plan as PDF", expanded=False):
        st.markdown("Download your care plan as a printable PDF.")
        pdf_bytes = generate_pdf(plan)
        st.download_button(
            label="📥 Download Care Plan as PDF",
            data=pdf_bytes,
            file_name="care_plan.pdf",
            mime="application/pdf"
        )

# Footer
st.markdown("""
    <hr style='border:1px solid #eee;'>
    <p style='text-align: center; font-size: 14px; color: #999999;'>
        Built with ❤️ at Hack the Vibe – CareSketch for Social Good 🌱
    </p>
""", unsafe_allow_html=True)
