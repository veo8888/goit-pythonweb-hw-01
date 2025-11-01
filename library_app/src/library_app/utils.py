"""
Helper function for required input from the user.
Prompts for input until the user enters a non-empty string.
"""


# Follows the SRP principle - each function performs one task.
def input_required(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if not value:
            print("⚠️  This field cannot be empty. Please try again.")
        else:
            return value
