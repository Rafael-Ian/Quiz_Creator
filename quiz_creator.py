#Assignment 9: Quiz Creator

def main():
    # open the file called "qz_qstns.txt" in append mode which is "a", meaning new questions will be added without removing those existing ones
    with open("qz_qstns.txt", "a")as file:
        while True:
            print("\n === Quiz Questions Creator ===")

            # The program will ask the user to input questions that the user needs for the quiz.
            question = input("Enter question: ")
            # Next, the program will ask the user to input the choices (a,b,c,d) that the user wants for the quiz.
            a = input("Enter Option a: ")
            b = input("Enter Option b: ")
            c = input("Enter Option c: ")
            d = input("Enter Option d: ")
# Then, the program will ask the user to input the correct answer for that specific question.
            while True:
                correct = ("Enter the correct answer (a/b/c/d): ").lower()
                if correct in ['a', 'b', 'c', 'd']:
# If the input is valid, then it will break out of the loop.
                else:
# Invalid inputs will keep the loop.
# Next, the program will ask the user if he wants to input another question by yes or no.
# The program will exit if the user doesn't want to continue or doesn't need to add any more questions.