import streamlit as st
import random
import time

st.set_page_config(page_title="🎲 Coin & Dice Game", layout="wide")

if 'coin_result' not in st.session_state:
    st.session_state.coin_result = None
if 'dice_result' not in st.session_state:
    st.session_state.dice_result = None

st.title("Welcome to the Coin Toss & Dice Roll Game 🎉")
st.write("Hello! Select a game from the sidebar to get started.")

st.sidebar.title("Choose a Game")
game_option = st.sidebar.radio("Select a game:", ["Coin Toss", "Dice Roll"])

def reset():
    """Function to reset the game state."""
    st.session_state.coin_result = None
    st.session_state.dice_result = None

def coin_toss():
    st.subheader("🪙 Coin Toss")

    left, mid, right = st.columns(3)

    with mid:
        result_image = st.empty()

        if st.button("TOSS"):
            result_image.image("COINTOSS.gif", caption="Spinning...", use_column_width=True)
            time.sleep(2)

            st.session_state.coin_result = random.choice(["HEADS", "TAILS"])
            result_image.image(f"{st.session_state.coin_result}.png", 
                               caption=f"Result: {st.session_state.coin_result}", 
                               use_column_width=True)
            st.success(f"The coin landed on **{st.session_state.coin_result}**!")

def dice_roll():
    st.subheader("🎲 Dice Roll")

    left, mid, right = st.columns(3)

    with mid:
        dice_image = st.empty()

        if st.button("ROLL"):
            dice_image.image("dice-game.gif", caption="Rolling...", use_column_width=True)
            time.sleep(2)

            st.session_state.dice_result = random.randint(1, 6)
            dice_image.image(f"dice_{st.session_state.dice_result}.png", 
                             caption=f"Result: {st.session_state.dice_result}", 
                             use_column_width=True)
            st.success(f"The dice landed on **{st.session_state.dice_result}**!")

if game_option == "Coin Toss":
    coin_toss()
elif game_option == "Dice Roll":
    dice_roll()
st.sidebar.button("Reset", on_click=reset)

