stoplist = ["a","A","about","above","across","after","again","against","all","almost","alone","along","already","also","although","always","am","among","an","and","another","any","anyone","anything","anywhere","are","aren't","around","as","at","b","B","back","be","became","because","become","becomes","been","before","behind","being","below","between","both","but","by","c","C","can","cannot","can't","could","couldn't","d","D","did","didn't","do","does","doesn't","doing","done","don't","down","during","e","E","each","either","enough","even","ever","every","everyone","everything","everywhere","f","F","few","find","first","for","four","from","full","further","g","G","get","give","go","h","H","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","her","here","here's","hers","herself","he's","him","himself","his","how","however","how's","i","I","i'd","if","i'll","i'm","in","interest","into","is","isn't","it","it's","its","itself","i've","j","J","k","K","keep","l","L","last","least","less","let's","m","M","made","many","may","me","might","more","most","mostly","much","must","mustn't","my","myself","n","N","never","next","no","nobody","noone","nor","not","nothing","now","nowhere","o","O","of","off","often","on","once","one","only","or","other","others","ought","our","ours","ourselves","out","over","own","p","P","part","per","perhaps","put","q","Q","r","R","rather","s","S","same","see","seem","seemed","seeming","seems","several","shan't","she","she'd","she'll","she's","should","shouldn't","show","side","since","so","some","someone","something","somewhere","still","such","t","T","take","than","that","that's","the","their","theirs","them","themselves","then","there","therefore","there's","these","they","they'd","they'll","they're","they've","this","those","though","three","through","thus","to","together","too","toward","two","u","U","under","until","up","upon","us","v","V","very","w","W","was","wasn't","we","we'd","we'll","well","we're","were","weren't","we've","what","what's","when","when's","where","where's","whether","which","while","who","whole","whom","who's","whose","why","why's","will","with","within","without","won't","would","wouldn't","x","X","y","Y","yet","you","you'd","you'll","your","you're","yours","yourself","yourselves","you've","z","Z"]
#this is a list of stopwords
questionwordlist = ["who", "what", "when", "where", "why", "which", "whose", "whom", "how", "is", "are", "am", "do", "does", "did", "can", "could", "will", "would", "have", "has", "had", "should", "must"]

def makelower(input): #turn a string into lowercase
    loweredinput = ''
    for chr in input:
        if chr.isalpha() or chr == ' ':
            loweredinput += chr.lower()
    return loweredinput

def isquestion(input):
    if "?" in input:
        return True
    
    changedinput = makelower(input)
    inputwordlist = changedinput.split(" ")
    print(inputwordlist[0])
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


#####   MAIN   #####
humaninput = input()
