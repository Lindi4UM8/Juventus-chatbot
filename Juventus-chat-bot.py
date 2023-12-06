import re
from collections import defaultdict
from list_of_files import *


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

def keywordtracing(input):
    keywordlist = inputcleanup(input)
    foundlines = dict()
    for word in keywordlist:
        #regexstring = f'.*{word}.*'
        regexstring = r'(?:[^.!?]*\b' + re.escape(word) + r'\b[^.!?]*[.!?])'
        lineswithword = re.findall(regexstring,teststring)
        
        #add all to dictionary after checking all hits with all keywords
        #then use this to find most likely sentence to match question
        
        for x in lineswithword:
            if x in foundlines.keys():
                foundlines[x] = foundlines[x] + 1
            else:
                foundlines[x] = 1
        foundlines = dict(sorted(foundlines.items(), key=lambda item: item[1], reverse=True))
    print(foundlines)
    return foundlines #returns entire dictionary


teststring = """In the heart of the dense, emerald jungle, a magnificent tiger named Rajah prowled with silent grace.
His fur, adorned with striking stripes, concealed the power that lay within his sinewy frame. 
Rajah was not just a jungle resident; he was the undisputed king, commanding respect from every creature in his realm.
One day, a sudden drought struck, and the once lush vegetation withered under the unforgiving sun.
Rajah, with keen instincts, led his fellow animals on a journey to find a hidden oasis.
Along the way, he encountered challenges, but his regal demeanor and unwavering determination inspired the diverse group of animals
and other creatures.
As Rajah led them through the harsh terrain, his strength became a symbol of hope.
Eventually, the oasis revealed itself, a shimmering haven amidst the parched land.
Rajah, with 2 triumphant roars, watched as the jungle flourished once more.
The grateful animals, from the smallest birds to the mightiest elephants, acknowledged Rajah's leadership, and harmony was restored in the kingdom.
From that day forward, Rajah's legend echoed through the jungle—a tale of resilience, unity, and the enduring spirit of their majestic tiger king."""

#####   MAIN   #####
humaninput = input()

isQ = isquestion(humaninput) #used to for if else of how to treat input

if isQ == True:
    keywordtracing(humaninput)
else:
    #Do keyword calculation and append information to file
    #We can also check if we have counteractive or similar information already in file
    pass

