import sys
import os
import streamlit as st
import time

# Add the parent directory of 'src' to the Python module search path
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(base_path)

from src.monty_hall_simulation import simulate_game


# Streamlit application setup and configuration
st.title("Monty Hall Simulation")
st.image("https://www.santuon.com/content/images/2022/06/monty_hall.png", width=800)

# Input: Number of games to simulate
num_games: int = st.number_input("Enter number of games to simulate", min_value=1, max_value=1000, value=100)

# Layout: Two columns for displaying results
col1, col2 = st.columns(2)
col1.subheader("Win percentage without switching")
col2.subheader("Win percentage with switching")

# Charts to dynamically update win percentages
chart1 = col1.line_chart(x=None, y=None, height=400)
chart2 = col2.line_chart(x=None, y=None, height=400)

# Variables to track cumulative wins
win_no_switching: int = 0
win_switching: int = 0

# Simulation loop
for i in range(num_games):
    # Simulate one game
    num_wins_without_switching, num_wins_with_switching = simulate_game(1)
    win_no_switching += num_wins_without_switching
    win_switching += num_wins_with_switching

    # Update charts with win percentages
    chart1.add_rows([win_no_switching / (i+1)])
    chart2.add_rows([win_switching / (i+1)])

    # Delay for smoother animation
    time.sleep(0.01)

# To run this code as a streamlit, first I should run "export PYTHONPATH=/home/seihani_7/my_pytopia/monty_hall_simulation" in my terminal, then run "streamlit run src/dashboard.py