# Quiz Game 10 Questions

# This task is to create a math game with 3 difficulty levels with their each 10 unique problems

# Easy - Will generate equations that consists of the numbers 1-9
# Normal - Will generate equations that consists of the numbers 10-99
# Hard - Will generate equations that consists of the numbers 100-999

# The user has 2 attempts for each equation before the answer is revealed
# Their overall result will be displayed after the 10 equations has been answered


# Python's in-built random module
import random
print("           __  __  ___  _____  _  _         ___   _   _  ___  ____")
print("          |  \/  |/   \|_   _|| || |       / _ \ | | | ||_ _||_  /")
print("          | |\/| || - |  | |  | __ |      | (_) || |_| | | |  / / ")
print("          |_|  |_||_|_|  |_|  |_||_|       \__\_\ \___/ |___|/___|")


print("\n                         Welcome to the Math's Quiz")
print("                        Please choose the Difficulty")


# This functions displays and sets the difficulty of the game as per the user's input
def displayMenu():
    print("\n")
    print("SET DIFFICULTY")
    print("1. EASY")
    print("2. NORMAL")
    print("3. HARD")
    # gets input of difficulty from the user (converts the input into an integer)
    level = int(input("\nSet Difficulty level (1-3): "))
    return level


# This function determines the equations num1 and num2 by getting the level variable as a parameter
def randomInt(level):
    if level == 1:
        return random.randint(1, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

# This function chooses either addition "+" or subtraction "-"
def decideOperation():
    return random.choice(['+','-'])    


# It keeps track of the attempts and if it is under 2 attempts it will redisplay the equation
# After two attempts it will display the correct answer

# This function is deisgned to present the math equation to the user, accept the input, and assess scoring based on whether the 1st or 2nd attempt was correct
def displayProblem(num1, num2, operation):
    # This function takes 3 parameters "num1 num2 and the operation"
    # It sets the functionalities of getting the correct answer based on the equation that will be generated
    if operation == '+':
        correct_ans = num1 + num2
    else: 
        correct_ans = num1 - num2
    
    
    # Attempt Loop - It is set to 0 and lets the user have two attempts before it is shown the correct answer
    attempts = 0
    while attempts < 2:
        # This displays the equation generated and calls the "isCorrect" function which checks if the stored "correct_ans" is equal to "user_ans"
        # If the user got it right on the first attempt it wuld award 10, if it gets it right on the 2nd they will get 5 points. Otherwise, they get 0
        user_ans = int(input(f"\n{num1} {operation} {num2} =  "))
        if isCorrect(user_ans, correct_ans):
            return 10 if attempts == 0 else 5
        else:
            print("Incorrect. Try again")
            attempts += 1
    print(f"The correct answer was {correct_ans}")
    return 0

# This function is used on the function above to determine if the user's input is equal to the stored correct answer
def isCorrect(user_ans, correct_ans):
    return user_ans == correct_ans

# This function calculates the overall results of the user
def displayResults(score):
    print(f"\nYour final score is {score}/100")
    if score > 90:
        grade = "A+"
    elif score > 80:
        grade = "A"
    elif score > 70:
        grade = "B"
    elif score > 60:
        grade = "C+"
    elif score > 50:
        grade = "D"
    else:
        grade = "F"
    print(f"Your grade is: {grade}")  # Display the grade
            

# This is the main function that executes the Math Quiz
# This sets the score to 0
# It then calls the displayMenu function to get the difficulty of the quiz
def main():
    while True:
        score = 0
        level = displayMenu()
        print("\n           _    ___  ___  _ ___    ___  ___  ___  ___  ___ ")
        print("          | |  | __]|_ _||// __]  / __]|_ _|| . || . \|_ _|")
        print("          | |_ | _]  | |   \__ \  \__ \ | | |   ||   / | | ")
        print("          |___||___] |_|   [___/  [___/ |_| |_|_||_\_\ |_| ")
        
        # This for loop repeats the questions ten times and uses an "_" underscore because the index of the loop will not be called in the loop therefore it is unnecessary
        for _ in range(10):
            # num 1 and 2 calls the randomInt function which takes the level as the paramter to determine if the numbers are 1 digit, 2 digit, or 3 digit
            num1 = randomInt(level)
            num2 = randomInt(level)
            # the operation is determined by the decideOperation function
            operation = decideOperation()
            # the score is determined by the displayProblem function which takes the 3 parameters and runs the function that checks and calculates the result of each question
            score += displayProblem(num1, num2, operation)
        
        # now we feed the score in the displayResults function so that when the 10 questions are done, are overall results are displayed
        displayResults(score)
        
        restart_game = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if restart_game != 'yes':
            print("Thank you for playing")
            break

# This calls the main function to run    
main()