# Plagiarism Detector app

This program compares two text files and calculates how similar they are based on word usage. I buld it as part of my summative, individual coding lab 2 in module called, introduction to programming with python

# how it operate

The program reads two essay files, cleans the text by removing punctuation and converting everything to lowercase, then counts how many times each word appears. It compares these word counts to find common vocabulary and calculate a similarity percentage.

# What the Program Does

- Loads and reads essay1.txt and essay2.txt
- Removes punctuation and standardizes case
- Counts word frequencies for each essay
- Lists words that appear in both essays with their counts
- Calculates a plagiarism percentage based on unique word overlap
- Allows users to search for specific words

# Requirements

Python 3.x. No external libraries are needed - the program uses only Python's standard library.

# how to run
To run this program,  save the Python code as a file named plagiarism_detector.py. Then create two text files called essay1.txt and essay2.txt in the exact same folder as the Python file and type your essays into these files. Open a terminal,in terminal open that folder, and type python plagiarism_detector.py (or python3 plagiarism_detector.py on some systems) then press Enter. The program will automatically load both essays, display word counts, show common words, calculate a plagiarism percentage, and give a verdict. After that, you can type any word to search for it in both essays, and type quit to exit the program. If you see a FileNotFoundError, make sure both text files exist in the same folder as the Python script.




