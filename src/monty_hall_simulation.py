import random
from typing import List, Tuple

def monty_hall_game(switch_doors: bool) -> bool:
    """
    Simulates a single Monty Hall game.

    Args:
        switch_doors (bool): Whether the player switches their initial choice of door 
        after one of the other doors is revealed.

    Returns:
        bool: True if the player wins the car, False otherwise.
    """
    doors: List[str] = ["car","goat","goat"]
    random.shuffle(doors)

    initial_choice: int = random.choice(range(len(doors)))

    doors_revealed: List[int] = [i for i in range(len(doors)) if i != initial_choice and doors[i] != "car"]
    door_revealed: int = random.choice(doors_revealed)

    if switch_doors:
        final_choice: int = [i for i in range(len(doors)) if i != initial_choice and i != door_revealed][0]
    else:
        final_choice = initial_choice

    return doors[final_choice] == "car"


def simulate_game(num_games: int) -> Tuple[int, int]:
    """
    Simulates a series of Monty Hall games.

    Args:
        num_games (int): The number of games to simulate.

    Returns:
        Tuple[int, int]: A tuple containing:
        - The number of wins without switching doors.
        - The number of wins with switching doors.
    """
    num_wins_without_switching: int = sum([monty_hall_game(False) for _ in range(num_games)])
    num_wins_with_switching: int = sum([monty_hall_game(True) for _ in range(num_games)])
    return num_wins_without_switching, num_wins_with_switching

if __name__ == "__main__":
    num_games: int = 1000
    win_percent_without_switching, win_percent_with_switching = simulate_game(num_games)
    print(win_percent_without_switching)
    print(win_percent_with_switching)