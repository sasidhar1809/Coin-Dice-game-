import streamlit as st ## TO Run the File Use "stremlit run main.py" in the terminal after clicking the Run button. 
import random
import time

st.set_page_config(page_title="🎲 Coin & Dice Game", layout="wide")

# Initialize session state
if 'coin_result' not in st.session_state:
    st.session_state.coin_result = None
if 'dice_result' not in st.session_state:
    st.session_state.dice_result = None

st.title("Welcome to the Coin Toss & Dice Roll Game 🎉")
st.write("Hello! Select a game from the sidebar to get started.")

# Sidebar to select game
st.sidebar.title("Choose a Game")
game_option = st.sidebar.radio("Select a game:", ["Coin Toss", "Dice Roll"])

# Reset function
def reset():
    """Function to reset the game state."""
    st.session_state.coin_result = None
    st.session_state.dice_result = None

# Coin Toss function
def coin_toss():
    st.subheader("🪙 Coin Toss")
    left, mid, right = st.columns(3)
    
    with mid:
        result_image = st.empty()

        if st.button("TOSS"):
            # Display spinning GIF using relative path from the 'images' folder
            try:
                result_image.image("images/COINTOSS.gif", caption="Spinning...", use_column_width=True)
                time.sleep(2)  # Delay to simulate spinning
                
                # Show final result
                st.session_state.coin_result = random.choice(["HEADS", "TAILS"])
                result_image.image(f"images/{st.session_state.coin_result}.png", 
                                   caption=f"Result: {st.session_state.coin_result}", 
                                   use_column_width=True)
                st.success(f"The coin landed on **{st.session_state.coin_result}**!")
            except Exception as e:
                st.error("Error displaying the image.")
                st.write(e)
                # HTML fallback
                result_image.markdown(f"<img src='images/COINTOSS.gif' alt='Spinning...' width='100%'>", 
                                      unsafe_allow_html=True)

# Dice Roll function
def dice_roll():
    st.subheader("🎲 Dice Roll")
    left, mid, right = st.columns(3)

    with mid:
        dice_image = st.empty()

        if st.button("ROLL"):
            # Display rolling GIF using relative path from the 'images' folder
            try:
                dice_image.image("images/dice-game.gif", caption="Rolling...", use_column_width=True)
                time.sleep(2)  # Delay to simulate rolling
                
                # Show final result
                st.session_state.dice_result = random.randint(1, 6)
                dice_image.image(f"images/dice_{st.session_state.dice_result}.png", 
                                 caption=f"Result: {st.session_state.dice_result}", 
                                 use_column_width=True)
                st.success(f"The dice landed on **{st.session_state.dice_result}**!")
            except Exception as e:
                st.error("Error displaying the image.")
                st.write(e)
                # HTML fallback
                dice_image.markdown(f"<img src='images/dice-game.gif' alt='Rolling...' width='100%'>", 
                                    unsafe_allow_html=True)

# Main logic to choose game
if game_option == "Coin Toss":
    coin_toss()
elif game_option == "Dice Roll":
    dice_roll()

# Reset button
st.sidebar.button("Reset", on_click=reset)
