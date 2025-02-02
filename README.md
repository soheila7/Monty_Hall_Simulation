# Monty Hall Simulation

This project simulates the famous Monty Hall problem and provides a Streamlit dashboard to visualize the results of the simulation. The project contains two main components:

1. **`monty_hall_simulation.py`**: A Python script containing the logic to simulate the Monty Hall game.
2. **`dashboard.py`**: A Streamlit app to visualize the simulation results in real-time.

## Project Structure

my_pytopia/  
└── monty_hall_simulation/  
    ├── src/  
    │   ├── __init__.py              # Marks src as a package  
    │   ├── monty_hall_simulation.py  # Contains the Monty Hall simulation logic  
    │   └── dashboard.py              # Streamlit dashboard for visualization

## Requirements

To run this project, you'll need Python 3.x and the following packages:
- Streamlit
- Random


## 1. **Monty Hall Simulation (`monty_hall_simulation.py`)**

This file contains the main logic to simulate the Monty Hall problem. The Monty Hall game involves three doors, behind one of which is a car and behind the other two, goats. The user is asked to choose one door. After that, one of the other doors is revealed to show a goat. The user is then given the option to switch to the other unopened door or stick with their original choice.

The script contains two main functions:

- `monty_hall_game(switch_doors: bool) -> bool`: Simulates one game of Monty Hall. It returns `True` if the player wins the car (i.e., the correct door was chosen), and `False` otherwise. The `switch_doors` argument determines whether the player switches doors or not.

- `simulate_game(num_games: int) -> Tuple[int, int]`: Simulates `num_games` of the Monty Hall game. It returns two values: the number of wins without switching and the number of wins with switching.

## 2. **Streamlit Dashboard (`dashboard.py`)**

The `dashboard.py` file contains a Streamlit app that visualizes the results of the Monty Hall simulation. The app allows you to specify the number of games to simulate and dynamically displays two line charts:

- One chart shows the win percentage for the scenario where the player does not switch doors.
- The other chart shows the win percentage for the scenario where the player switches doors.

### How to Run the Dashboard

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_directory>
2. Install the Required Dependencies

    You need to install the following packages:

    - `streamlit` for the dashboard app
    - `numpy` for numerical operations (used in the simulation)

    To install these dependencies, run the following command:

    ```bash
    pip install streamlit numpy
    ```
3. Run the Streamlit dashboard:
    
    After the dependencies are installed, you can run the dashboard with the following command:
    ```bash
    streamlit run src/dashboard.py
    ```
4. Open your browser:
    
    The Streamlit app should now be running, and you can access it by navigating to the URL provided in the terminal.
    

### Features of the Dashboard
- Input: Allows you to enter the number of games to simulate (between 1 and 1000).
- Charts: Displays the win percentages for both the scenarios (switching and not switching doors) as the simulation progresses.

## License
- This project is licensed under the MIT License - see the LICENSE file for details.