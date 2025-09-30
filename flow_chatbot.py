import streamlit as st

def flow_ui():
    st.subheader("Flow Chatbot")

    questions = [
        "👋 Welcome! Let's start. What is your name?",
        "Great! How many years of experience do you have in Data Science?",
        "Nice. Which programming language are you most comfortable with?",
        "Which ML algorithm do you like the most?",
        "Awesome! Finally, what is your career goal in Data Science?"
    ]

    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
    if "answers" not in st.session_state:
        st.session_state.answers = {}

    idx = st.session_state.current_question
    if idx < len(questions):
        question = questions[idx]
        user_input = st.text_input(question, key=f"q_{idx}")

        if user_input:
            valid = False
            if idx == 0: 
                valid = user_input.isalpha()
                if not valid:
                    st.error("Please enter a valid name (alphabets only).")
            elif idx == 1:  
                valid = user_input.isdigit()
                if not valid:
                    st.error("Please enter years of experience as a number.")
            else:  
                valid = not user_input.isdigit()
                if not valid:
                    st.error("Please enter a valid text (not just numbers).")

            if valid:
                st.session_state.answers[question] = user_input
                st.session_state.current_question += 1
                st.experimental_rerun()

    if idx == len(questions):
        st.success("Thank you! Here’s a quick summary of your responses:")
        answers = st.session_state.answers
        st.write(f"- **Name:** {answers[questions[0]]}")
        st.write(f"- **Experience (years):** {answers[questions[1]]}")
        st.write(f"- **Programming Language:** {answers[questions[2]]}")
        st.write(f"- **Favorite Algorithm:** {answers[questions[3]]}")
        st.write(f"- **Career Goal:** {answers[questions[4]]}")

        if st.button("🔄 Restart"):
            st.session_state.current_question = 0
            st.session_state.answers = {}
            st.experimental_rerun()
