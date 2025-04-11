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
                correct = input("Enter the correct answer (a/b/c/d): ").lower()
                if correct in ['a', 'b', 'c', 'd']:
                    break
                # If the input is valid, then it will break out of the loop.
                else:
                    print("Invalid input. Please enter only a, b, c, d.")   # Invalid inputs will keep the loop.

            #Puts the question and answer to the text file
            file.write(f"Question: {question}\n")
            file.write(f"a.) {a}\n")
            file.write(f"b.) {b}\n")
            file.write(f"c.) {c}\n")
            file.write(f"d.) {d}\n")
            file.write(f"Correct Answer: {correct}\n\n") #Adds empty line after questionss

            # Next, the program will ask the user if he wants to input another question by yes or no.
            cont = input("Do you want to add another question? (yes/no): ").lower()
            if cont != 'yes':
                print("Questions are saved to 'qz_qstns.txt'. Exiting Program.")
                break
                # The program will exit if the user doesn't want to continue or doesn't need to add any more questions.

if __name__ == "__main__":
    main()
