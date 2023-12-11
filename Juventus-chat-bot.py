import re
from list_of_files import *
import string
import math
# from nltk.corpus import wordnet   #for synonym function
import random


file_path = 'soccer.txt'

def makelower(input): #turn a string into lowercase
    loweredinput = ''
    for chr in input:
        if chr.isalnum() or chr == ' ':
            loweredinput += chr.lower()
    return loweredinput

def isquestion(input):
    if "?" in input:
        return True
    
    changedinput = makelower(input)
    inputwordlist = changedinput.split(" ")
    if inputwordlist[0] in questionwordlist:
        return True

    return False

# removes question mark, period, or exclamation point from sentence
def remove_punctuation(input):
    punctuation_chars = string.punctuation
    # Create a translation table to remove punctuation
    translation_table = str.maketrans("", "", punctuation_chars)
    # Use translate to remove punctuation from the sentence
    cleaned_sentence = input.translate(translation_table)
    return cleaned_sentence

def inputcleanup(input):
    #Taken from laplace soothing project
    #There are many question words in stopwordslist use isquestion to identify if question
    #then use this function to get keywords
    
    cleaninput = makelower(input)
    
    cleaninput = cleaninput.split()
    deletinglist = [] #using a list to avoid messing with the index of the cleaninput for loop

    for word in cleaninput:
        found = False
        for x in stoplist:
            if word == x:
                found = True
        if found == True:
            deletinglist.append(word)
    for y in deletinglist:
        cleaninput.remove(y)
    return cleaninput

# finds the number of times the target word appears in the file 
def occurrences_text(file_path, target_word):
    with open(file_path, 'r') as file:
        #line_count = sum(1 for line in file)
        content = file.read()
        # Using regex to find the number of times the target word appears
        occurrences = len(re.findall(r'\b' + re.escape(target_word) + r'\b', content, re.IGNORECASE))
        return occurrences

# finds the number of lines the document has 
def doc_count(file_path):
    with open(file_path, 'r') as file:
        line_count = sum(1 for line in file)
        return line_count

#finds the number of words in the humaninput
def total_words(humaninput):
    words = humaninput.split()
    total_word_count = len(words)
    return total_word_count

#finds the number of times the target word appears in the humaninput
def word_appearances_input(humaninput, word):
    appearances = humaninput.lower().split().count(word.lower())
    return appearances

# caluclates the tf-idf for each word and puts it and its score in a dictionary
def tf_idf(input):
    input = inputcleanup(input)
    tf_idf_dict = {}
    for item in input:
        total_lines = doc_count(file_path)
        word_total = total_words(humaninput)
        word_input_appearances = word_appearances_input(makelower(humaninput), item)
        word_file_occurrences = occurrences_text(file_path, item)
        tf = word_input_appearances/word_total
        tf_idf = 0
        if word_file_occurrences > 0:
            idf = math.log10(total_lines/word_file_occurrences)
            tf_idf = tf*idf
        tf_idf_dict[item] = tf_idf
    return tf_idf_dict

# sorts the dictionary, removes the keys with values of 0, then appends each remaining key to the keyword list
def get_keyword(tf_idf_dict):
    keywords = []
    sorted_keys = sorted(tf_idf_dict, key=lambda x: tf_idf_dict[x], reverse=True)
    for key, value in tf_idf_dict.items():
        if value > 0:
            keywords.append(key)
    return keywords
    

def keywordtracing(input):
    tf_idf_dict = tf_idf(input)
    keywordlist = get_keyword(tf_idf_dict)
    foundlines = dict()
    for word in keywordlist:
        with open(file_path, 'r') as file:
            content = file.read()
            regexstring = r'(?:[^.!?]*\b' + re.escape(word) + r'\b[^.!?]*[.!?])'
            lineswithword = re.findall(regexstring, content, re.IGNORECASE )
        
        #add all to dictionary after checking all hits with all keywords
        #then use this to find most likely sentence to match question
        
        for x in lineswithword:
            if x in foundlines.keys():
                foundlines[x] = foundlines[x] + 1
            else:
                foundlines[x] = 1
        foundlines = dict(sorted(foundlines.items(), key=lambda item: item[1], reverse=True))
    if len(foundlines) != 0:
        answer = list(foundlines.keys())[0]
        repeatQuestion(makelower(humaninput),answer)
        return answer
    return #In the case where there are no keywords it returns nothing, we can change it to be a message of output like: Can you rephrase the question

# def synonyms(input): #probably not useful, but keeping function in case, REMEMBER to uncomment import if using
#     synonyms = []

#     for syn in wordnet.synsets(input):
#         for lm in syn.lemmas():
#                 synonyms.append(lm.name())

#     synonyms.append(input)
#     return (set(synonyms)) #returns a set of synonym for the word

def addToDocument(input):
    with open(file_path, 'a') as file:
        file.write(f"{input}. ")
        return

questiondict = dict()
def repeatQuestion(input,output):
    
    if input in questiondict.keys():
        print(repeatquestionlist[random.randint(0,4)])
        return questiondict.get(input)
    else:
        questiondict[input] = output
    return

#####   MAIN   #####
humaninput = ''
while(humaninput != 'q'):
    humaninput = input('Enter q to quit: \n')
    isQ = isquestion(humaninput) #used to for if else of how to treat input
    if humaninput == 'q':
        break # JUST HERE WHILE WE NEED IT FOR THE TESTING LOOP

    if isQ == True:
        message = keywordtracing(humaninput)
        print(message)
    else:
        addToDocument(humaninput)
    


    


