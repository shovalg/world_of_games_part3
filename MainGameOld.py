from Live import load_game, welcome

# Main program that gets username as an input and perform input validation.
# The only input allowed is alpha characters without spaces.

control_var = True
while control_var:
    try:
        user_name = input("Please Enter your name: ")
        control_var = user_name.isalpha()
        if not control_var:
            control_var = True
            raise ValueError
        user_name = user_name.capitalize()
        print(welcome(user_name))
        load_game = load_game()
        break
    except ValueError:
        print("Username can only contain alpha characters and without spaces.")
