import streamlit as st
import random

st.title("🎰 Jackpot Guessing Game")
st.write("You Have Only 5 Attempt !")

if 'jackpot' not in st.session_state:
    st.session_state.jackpot = random.randint(1, 100)
    st.session_state.count = 0
    st.session_state.game_over = False

name = st.text_input("Enter your name:")
guess = st.number_input("Guess the jackpot number between 1 and 100:", min_value=1, max_value=100, step=1)

if st.button("Submit Guess") and name and not st.session_state.game_over:
    st.session_state.count += 1
    if guess < st.session_state.jackpot:
        st.warning("Too low! Guess higher.")
    elif guess > st.session_state.jackpot:
        st.warning("Too high! Guess lower.")
    else:
        if st.session_state.count <= 5:
            st.success(f"🎉 Congratulations {name}! You've guessed the jackpot number {st.session_state.jackpot} in {st.session_state.count} tries.")
            st.write("You are a lucky winner!")
            st.balloons()
            st.session_state.game_over = True
        else:
            st.error(f"Sorry {name}, you've guessed the jackpot number {st.session_state.jackpot} in {st.session_state.count} tries, but you didn't win. Better luck next time!")
            st.session_state.game_over = True

if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.jackpot = random.randint(1, 100)
        st.session_state.count = 0
        st.session_state.game_over = False
        st.rerun #experimental_rerun()


st.markdown("### 👨‍💻 Developed with ❤️ by **Sk**")
