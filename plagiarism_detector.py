# importing strings to have acess to punctuation
import string
#reading essay and return its content as a string
def read_essay(filename):
    # open the file and read its content
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as error:
        print(f"Error: {error}")



#cleaning the essay by removing punctuation and converting to lowercase
def clean_and_tokenize(essay):
    # remove punctuation and convert to lowercase
    translation = str.maketrans('','',string.punctuation)
    clean_essay = essay.translate(translation).lower()
    # split the cleaned essay into words
    return clean_essay.split()
#function takes a list of words and returns a DICTIONARY where the key is the word and the value is how many times it appears
def word_frequencies(words):
    frequencies = {}
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    return frequencies
# finding common words between two essays
def common_words(freq1, freq2):
    common_word = {}
    for word in freq1:
        if word in freq2:
            common_word[word] = {
                'essay1_count': freq1[word],
                'essay2_count': freq2[word]
            }
    return common_word
#search for specific words in essays and if the word is found in either essay, return a dictionary with the count of the word in each essay, if not found return false
def search_word(word_tosearch, freq1, freq2):
    word_lower = word_tosearch.lower().strip()
    count1 = freq1.get(word_lower, 0)
    count2 = freq2.get(word_lower, 0)
    if count1 == 0 and count2 == 0:
        return False  # ← Returns False as required!
    else:
        return {'essay1': count1, 'essay2': count2}  # ← Returns dictionary

    #calculating the percentage of plagiarism in the essays
def calculate_plagiarism(freq1, freq2):
    # Convert to sets (unique words only)
    set1 = set(freq1.keys())
    set2 = set(freq2.keys())
    # Intersection (common unique words)
    common_unique = set1 & set2
    # Union (all unique words)
    all_unique = set1 | set2
    if len(all_unique) == 0:
        return 0.0
    percentage = (len(common_unique) / len(all_unique)) * 100
    return percentage
#display common words in essays
def display_common_words(common_freq):
    if not common_freq:
        print("No common words found between the essays.")
    else:
        
        print("Common words between the essays:")
        
        for word, counts in common_freq.items():
            print(f"  '{word}' - appears {counts['essay1_count']} time(s) in essay1, "
                  f"{counts['essay2_count']} time(s) in essay2")
 #def main function to run the program
def main(): 
  
    print("Welcome to the Plagiarism Detector app!")
    
    
    # Read the essays
    print("\nReading essay files...")
    essay1 = read_essay('essay1.txt')  
    essay2 = read_essay('essay2.txt')
    
    # If files do not exist, exit the program
    if essay1 is None or essay2 is None:
        print("Exiting the program due to missing files.")
        return       
    
    print("Both essays loaded successfully!")
    
    # Clean and tokenize the essays
    print("\nCleaning and processing text...")
    words1 = clean_and_tokenize(essay1)
    words2 = clean_and_tokenize(essay2)
    
    print(f"essay1.txt: {len(words1)} total words, {len(set(words1))} unique words")
    print(f"essay2.txt: {len(words2)} total words, {len(set(words2))} unique words")
    
    # Calculate word frequencies for both essays
    print("\nCounting word frequencies...")
    freq1 = word_frequencies(words1)
    freq2 = word_frequencies(words2)
    
    # Find common words between the essays
    print("\nFinding common words...")
    common_freq = common_words(freq1, freq2)
    
    # Display common words
    display_common_words(common_freq)
    
    # Calculate and display plagiarism percentage
   
    plagiarism_percentage = calculate_plagiarism(freq1, freq2)
    print(f"Plagiarism percentage: {plagiarism_percentage:.2f}%")
    
    # Display verdict
    if plagiarism_percentage >= 50:
        print("\n🛑  ATTENTION: PLAGIARISM DETECTED!")
        print(f"   ({plagiarism_percentage:.2f}% is greater than or equal to 50%)")
    else:
        print("\n🟢 VERDICT: NO PLAGIARISM DETECTED")
        print(f"   ({plagiarism_percentage:.2f}% is less than 50%)")
    
    # Word search feature (NO check_word_presence needed!)
   
    print("WORD SEARCH FEATURE")

    print("Type 'quit' to exit")
    
    while True:
        word_to_search = input("\nEnter a word to search: ").strip()
        
        if word_to_search.lower() == 'quit':
            print("Goodbye!")
            break
        
        if not word_to_search:
            print("Please enter a word to search.")
            continue
        
        search_result = search_word(word_to_search, freq1, freq2)
        
        if search_result is False:
            print(f"The word '{word_to_search}' was not found in either essay.")
        else:
            print(f"The word '{word_to_search}' appears {search_result['essay1']} time(s) in essay1 and {search_result['essay2']} time(s) in essay2.")
            # run the main function to start the program
if __name__ == "__main__":    main()   
