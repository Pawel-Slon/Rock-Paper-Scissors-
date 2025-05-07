import streamlit as st
import random

# --- Page configuration ---
st.set_page_config(page_title="Rock, Paper, Scissors!", page_icon="✂️", layout="centered")

# --- Title and description ---
st.title("✊ ✋ ✌️ Rock, Paper, Scissors!")
st.subheader("Can you beat the computer?")

st.markdown("---")

# --- User choice ---
choices = {'Rock': '✊', 'Paper': '✋', 'Scissors': '✌️'}

user_choice = st.radio("Choose your weapon:", list(choices.keys()), horizontal=True)

# --- Play button ---
if st.button("Play!"):
    computer_choice = random.choice(list(choices.keys()))

    # --- Show choices ---
    st.write(f"**You chose:** {choices[user_choice]} {user_choice}")
    st.write(f"**Computer chose:** {choices[computer_choice]} {computer_choice}")

    # --- Determine the winner ---
    if user_choice == computer_choice:
        st.success("🤝 It's a draw!")
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        st.balloons()
        st.success("🎉 You won!")
    else:
        st.error("😢 You lost!")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit")

