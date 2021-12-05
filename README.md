# flash_cards

A flash card "game"/"study aide" that reads a CSV file with the comma delimeter separating each side of the card.  This was created to help me learn my wife's native language, Khmer(Cambodia), but designed so it can accept different csv files(card decks) for other applications.

Currently available CSV files are:
* sample.csv - for testing
* Spanish-English Numbers 1-100.csv - first implementation of "real" data

The games can be "reversed", for example, you can be presented a Spanish number as a question and enter an English number as the answer, or you can be presented with an English number as a question and enter a Spanish word as the answer.

Reversing the game works best if it is a single word/number or short phrase as opposed to a long question.  Matches must be exact at this point.  If the question is "What color is the sky" and the answer is "blue", reversing that so that the question simply is "blue" won't be very intuitive.

### To-Do
* Help text depending on the file that is loaded.  For example, in the Spanish-English Numbers 1-100.csv file, the Spanish words do not have accent marks, tildes, etc.  For English numbers, 21-99 are separated by hyphens except for those divisible by 10 (for example, twenty-four)
* Documentation
* More CSV files for flashcards, possibly eliminate need to enter ".csv".
* Possible menu
* Possible GUI
