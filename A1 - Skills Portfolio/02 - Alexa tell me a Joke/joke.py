# Python's in-built random module
import random

# This function gets the joke by getting the parameter filename to be able to retreive the joke on the randomJokes.txt file
def get_jokes(filename):
    joke = [] # This sets the joke variable as an empty list
    with open (filename, 'r') as file: # This then opens the filename and tells it to only read the file
        for line in file:
            # if there is a question mark in the line it divides it into the setup and the punchline using .split('?', 1)
            if '?' in line:
                setup, punchline = line.strip().split('?', 1)
                joke.append((setup + '? ', punchline)) # now it combines the setup and punchline using append
    return joke

# This function tells the jokes randomly using the variable joke as a parameter.
def tell_joke(joke):
    # joke is stored in the get_jokes function
    joke = random.choice(joke)
    # joke[0] is the setup and joke[1] is the punchline
    print("\nHear this... " + joke[0])
    input("What/Why?...")
    print(joke[1])


# This is the main program that calls the functions above    
def main():
    # joke variable here gets the file name and its file path to load into get_jokes function
    joke = get_jokes("A1 - Skills Portfolio/02 - Alexa tell me a Joke/randomJokes.txt")

    print("    __ _____ _____ _____    _____ _____ _____ _____ _____ _____ _____ _____ _____ ")
    print(" _ |  |     |  |  |   __|  |   __|   __|   | |   __| __  |  _  |_   _|     | __  |")
    print("| |_| |  |  |    -|   __|  |  |  |   __| | | |   __|    -|     | | | |  |  |    -|")
    print("|_____|_____|__|__|_____|  |_____|_____|_|___|_____|__|__|__|__| |_| |_____|__|__|")
    print("      Say 'Alexa tell me a joke' to hear a random joke or 'quit' to exit.")
    
    # This while loop accepts the user's input to either tell a joke again, quit the program, or if the user typed in an invalid key. 
    # The while loop will stay true unless the user input is quit
    while True:
        user_input = input("\nType 'joke/quit' : ").strip().lower() 
        if user_input == "joke":
            tell_joke(joke)
        elif user_input == "quit":
            print("Thank you for listening to my jokes")
            break
        else:
            print("Sorry, I didn't understand that try typing 'Joke' or 'Quit'.")
# This calls the main funciton to run the entire program
main()