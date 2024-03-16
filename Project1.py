# Project1.py
# Author: Laci Trull

print("Welcome to my quiz game! You will be asked a series of questions about my favorite things and you will need to answer them (A, B, C, or D). Each question is worth 1 point. If you answer incorrectly, no points will be awarded. Good luck!")

# function that creates the quiz minigame
def quiz_game():
    # set score to 0
    score = 0
    # create array of questions
    questions = ["What is my favorite color? A) Green B) Purple C) Orange D) Blue ",
                 "What is my favorite game? A) Minecraft B) Genshin Impact C) Celeste D) Stardew Valley",
                 "What is my favorite animal? A) Cat B) Elephant C) Giraffe D) Polar Bear ",
                 "Who is my best friend? A) Luis B) Blake C) Sam D) Alex ",
                 "Which state have I NOT visited before? A) South Dakota B) New York C) California D) Nebraska "]
    # array of correct answers choices
    correct_answer = ["B","C","A","B","D"]
    valid_answers = ["A","B","C","D"]
    question_number = 0
    # for loop that iterates through each question
    while (question_number < 5):
        print("Question " + str(question_number + 1) + ": " + questions[question_number])
        answer = input()
        if answer == correct_answer[question_number]:
            print("Correct!")
            score += 1
            question_number += 1
        elif (answer in valid_answers) and not (answer == correct_answer[question_number]):
            print("Incorrect! The correct answer is " + str(correct_answer[question_number]) + ".")
            question_number += 1
        else:
            print("Invalid input! Please enter A, B, C, or D.")
    print("Your score is " + str(score) + " out of 5. Thanks for playing!")

def main():
    quiz_game()

if __name__ == "__main__":
    main()