import random

# --- Rubric Item: Modularize code with a reusable function ---
def get_magic_answer():
    """
    Purpose: Generates a random number to select and return 
    a prediction from a collection sequence.
    """
    # Generate a random number between 0 and 7 (for list indexing)
    random_index = random.randint(0, 7)
    
    # --- Rubric Item: Create collections of data with sequences (lists) ---
    # Converted dictionary to a sequence list
    answers = [
        "yes",
        "no",
        "signs point to maybe",
        "ask me again later",
        "most likely will happen",
        "dont count on it",
        "maybe",
        "never in a million years"
    ]
    
    # Access and return the used element from the list
    return answers[random_index]


print("start")

# --- Rubric Item: Integrate three distinct data types ---
# 1. Boolean (True/False) used for game state control
# 2. Strings used for text inputs/outputs
# 3. Integers used for random list indexing
game_is_running = True 

# --- Rubric Item: Create applications that can perform repeated tasks ---
# Wrapped game in a while loop so the user can ask multiple questions
while game_is_running:
    
    # Get user input, remove spaces, and convert to lowercase
    user_input = input("Input a yes or no question or type 'exit' to quit: ").strip().lower()
    
    # --- Rubric Item: Create decision making with decision structures ---
    if user_input == "exit":
        game_is_running = False  # Changes boolean to break the loop safely
    else:
        # Call the custom reusable function
        selected_answer = get_magic_answer()
        # Display answer to user on the screen
        print(f"Answer: {selected_answer}\n")

print("end")
