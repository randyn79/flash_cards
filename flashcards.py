import csv
import random
import sys
import os

def load_dictionary(deck):
    with open(deck, 'r') as file:
        question, answer = file.readline().rstrip('\n').split(',')
        reader = csv.reader(file)
        dict1 = dict(reader)
        return question, answer, dict1

#def file_descriptions(deck):
#    print(deck)
#    with open('file_descriptions.txt', 'r') as descriptions:
#        descriptions.readline()
#        data = descriptions.readlines()
#        print(data[0])


def flash_cards(dict1, choice):
    correct = 0
    incorrect = 0
    while True:
        question = random.choice(list(dict1.items()))
        print('-' * 50)
        print(f'Question:  {question[0]}')
        answer = input('Answer: ').casefold()
        print('-' * 50)
        if answer == question[1]:
            print()
            print('Correct!!! :)')
            print()
            correct += 1
        else:
            print('Incorrect :(')
            print(f'The correct answer was {question[1]}.')
           
            incorrect +=1
        print(f'CURRENT SCORE')
        print(f'Correct: {correct}')
        print(f'Incorrect: {incorrect}')
        print('-' * 50)
        keep_playing = input('Press ENTER to keep playing or enter x to exit:  ').casefold()
        if keep_playing == 'x':
            print('-' * 50)
            print(f'FINAL SCORE')
            print(f'Correct: {correct}')
            print(f'Incorrect: {incorrect}')
            print('-' * 50)
            sys.exit()
        else:
            continue

if __name__ == "__main__":
    

    print('-' * 50)
    print(f'FLASHCARDS')
    print('-' * 50)
    print()
    path = os.getcwd()
    csv_files = os.listdir(path)
    print('Available flashcard decks:')
    for file in csv_files:
        if file.endswith('.csv'):
            print(file)
    print()
    deck = input('Enter the filename for the deck you would like to use:  ')
    #file_description = file_descriptions(deck)
    
    question, answer, dict1 = load_dictionary(deck)
    
    
    while True:
        print('-' * 50)
        print(f'FLASHCARDS: {question} / {answer}')
        print('-' * 50)
        print(f'Enter 1 for {question} to {answer}')
        print(f'Enter 2 for {answer} to {question}')
        print(f'Enter x to exit')
        print()
        choice = input(f"""What is your choice?  """).casefold()
        if choice == '1':
            flash_cards(dict1, choice)
        elif choice == '2':
            dict1 = {value: key for (key, value) in dict1.items()}
            flash_cards(dict1, choice)
        elif choice == 'x':
            sys.exit()
        else:
            print('Invalid selection')
            continue
