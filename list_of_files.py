stoplist = ["a","A","about","above","across","after","again","against","all","almost","alone","along","already","also","although","always","am","among","an","and","another","any","anyone","anything","anywhere","are","aren't","around","as","at","b","B","back","be","became","because","become","becomes","been","before","behind","being","below","between","both","but","by","c","C","can","cannot","can't","could","couldn't","d","D","did","didn't","do","does","doesn't","doing","done","don't","down","during","e","E","each","either","enough","even","ever","every","everyone","everything","everywhere","f","F","few","find","first","for","four","from","full","further","g","G","get","give","go","h","H","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","her","here","here's","hers","herself","he's","him","himself","his","how","however","how's","i","I","i'd","if","i'll","i'm","in","interest","into","is","isn't","it","it's","its","itself","i've","j","J","k","K","keep","l","L","last","least","less","let's","m","M","made","many","may","me","might","more","most","mostly","much","must","mustn't","my","myself","n","N","never","next","no","nobody","noone","nor","not","nothing","now","nowhere","o","O","of","off","often","on","once","one","only","or","other","others","ought","our","ours","ourselves","out","over","own","p","P","part","per","perhaps","put","q","Q","r","R","rather","s","S","same","see","seem","seemed","seeming","seems","several","shan't","she","she'd","she'll","she's","should","shouldn't","show","side","since","so","some","someone","something","somewhere","still","such","t","T","take","than","that","that's","the","their","theirs","them","themselves","then","there","therefore","there's","these","they","they'd","they'll","they're","they've","this","those","though","three","through","thus","to","together","too","toward","two","u","U","under","until","up","upon","us","v","V","very","w","W","was","wasn't","we","we'd","we'll","well","we're","were","weren't","we've","what","what's","when","when's","where","where's","whether","which","while","who","whole","whom","who's","whose","why","why's","will","with","within","without","won't","would","wouldn't","x","X","y","Y","yet","you","you'd","you'll","your","you're","yours","yourself","yourselves","you've","z","Z"]
#this is a list of stopwords
questionwordlist = ["who", "what", "when", "where", "why", "which", "whose", "whom", "how", "is", "are", "am", "do", "does", "did", "can", "could", "will", "would", "have", "has", "had", "should", "must"]

polite_words = ["Let's find that out, ", "Definitely, ", "Absolutely, ", "Sure, ", "Of course, ", "Certainly, ", "Of course sir, ", "Good question, ", "Absolutely, ", "Sure thing, ", "Hmmm let me think..."]

phrases_when_unsure = [
    "I'm sorry, I don't have that information.",
    "I'm afraid I don't know the answer to that.",
    "Apologies, I don't have that data at the moment.",
    "That's a bit beyond my knowledge base.",
    "Unfortunately, I can't provide an answer to that question.",
    "I don't have the specific details you're looking for.",
    "Regrettably, I'm not equipped to answer that.",
    "I'm sorry, the information you're seeking is not available to me.",
    "I'm not sure about that. Is there anything else I can help you with?",
    "I don't have the necessary details to answer your question accurately.",
    "My capabilities are limited in that area, and I can't provide the information you need.",
    "I'm sorry, that falls outside my scope of knowledge.",
    "I wish I could assist, but I don't have the answer.",
    "I don't have the specifics on that topic.",
    "Unfortunately, I'm unable to help with that inquiry.",
    "I'm sorry, but that's not within my expertise.",
    "My apologies, but I can't provide the information you're looking for.",
    "I'm not familiar with that particular detail.",
    "I'm sorry, the details on that are not available in my database.",
    "I appreciate your question, but I don't have the answer."
]

polite_phrases = [
    "Can",
    "will",
    "Should",
    "Could",
    "Would", 
    "Could you",
    "Would you",
    "Do you mind if",
    "Can you",
    "Will you",
    "Is it possible to",
    "Might I",
    "May I",
    "Is there any chance you could",
    "If it's not too much trouble, could you",
    "I was wondering if you could",
    "Do you think you could",
    "I hope it's okay, but could you",
    "Would it be alright if",
    "I'd appreciate it if you could",
    "Could I trouble you to",
    "Is there a possibility that you could",
    "If you don't mind, could you",
    "Do you have a moment to",
    "Would it be convenient for you to",
    "Can I ask you to",
    "Is there any way you could"
]

learning_responses = [
    "Got it.",
    "Noted.",
    "Understood.",
    "Thanks for sharing.",
    "I appreciate the information.",
    "I'll remember that.",
    "Great input!",
    "Sounds interesting to me.",
    "I'll keep that in mind.",
    "Thanks for letting me know.",
    "I'm learning a lot.",
    "That's helpful!",
    "I'll add that to my knowledge.",
    "I'm getting smarter!",
    "You're teaching me well!",
    "I love learning from you.",
    "Good to know",
    "Ok, I understand"
    "I'm improving with your help.",
    "You're a great teacher.",
    "I'm absorbing information like a sponge.",
    "Your input is valuable.",
    "You're making me smarter.",
    "I'm here to learn.",
    "Every bit of information helps.",
    "Thanks for enlightening me.",
    "You're contributing to my knowledge base.",
    "I'm becoming a chatbot guru with your help.",
    "That's intriguing!",
    "Wow, interesting!",
    "You've got my attention.",
    "Ah ok, I'll keep that in mind for later.",
]


repeatquestionlist = [
    "I already answered that, but I'm happy to repeat it for you: ",
    "Either I'm having déjà vu, or you really want to know! Here's the answer again: ",
    "As I stated above: ",
    "I noticed you're really curious about this! No worries it's still: ",
    "Either my crystal ball is malfunctioning, or we're stuck in a time loop! No worries, though. Here's the answer again: "
]

typodictionary = {
    "height": ["hieght", "heigth", "hight", "heigt", "heght"],
    "weight": ["wieght", "wait", "weght", "wight", "waeight"],
    "tall": ["tal", "tahl", "thall", "talll", "tull"],
    "small": ["smal", "smoll", "smll", "smalll", "smaal"],
    "number": ["numer", "numbr", "numberr", "nuber", "numbar"],
    "jersey": ["jersy", "jersie", "jearsy", "jersay", "jerseye"],
    "foot": ["fot", "fott", "foott", "fuot", "food"],
    "right": ["rite", "wright", "rigth", "rightt", "rihgt"],
    "left": ["lift", "lef", "lefft", "leftt", "lepht"],
    "born": ["borne", "bornn", "boorn", "bourn", "boren"],
    "from": ["froom", "form", "frum", "frrom", "fom"],
    "where": ["whare", "were", "weree", "wherr", "werre"],
    "what": ["waht", "wht", "wut", "whot", "waat"],
    "who": ["hoo", "whho", "wo", "whoo", "ho"],
    "how": ["hwo", "haw", "howw", "hoow", "hou"],
    "why": ["wyy", "wi", "whey", "hwy", "whi"],
    "could": ["coud", "culd", "coul", "coould", "couldd"],
    "would": ["woud", "wuld", "woul", "wouldd", "woulld"],
    "can": ["cn", "caan", "cann", "ca", "cna"],
    "did": ["dd", "diid", "ddi", "diddd", "didd"],
    "does": ["dose", "dos", "doess", "doesd", "doss"],
    "when": ["wen", "whenn", "whhen", "whn", "whan"],
    "which": ["wich", "whcih", "whihc", "whitch", "wihch"],
    "whose": ["whos", "whoes", "who'se", "whoose", "whosee"],
    "whom": ["whome", "whoom", "whomm", "whomme", "who'm"],
    "is": ["iss", "iis", "i", "si", "iss"],
    "are": ["aar", "arre", "aree", "arr", "aare"],
    "am": ["amm", "aam", "amme", "a", "m"],
    "do": ["doo", "d", "du", "dooe", "doe"],
    "can": ["cn", "caan", "cann", "ca", "cna"],
    "will": ["wil", "wiil", "willl", "wll", "will"],
    "should": ["shold", "shuld", "shouldd", "shoulld", "shouuld"],
    "have": ["hve", "hvae", "hav", "havee", "haave"],
    "had": ["hadd", "hade", "haad", "hadd", "hhad"],
    "has": ["hass", "haas", "haz", "hhas", "hass"],
    "must": ["musst", "mst", "muts", "mustt", "mus"],
    "forward": ["foward", "foorward", "forwad", "forrward", "foward"],
    "striker": ["strikerr", "stryker", "strikerer", "strikar", "stiker"],
    "penalty": ["penelty", "penaltty", "penalyy", "penaalty", "peneltyy"],
    "free": ["freee", "fre", "freee", "fre", "fee"],
    "kick": ["kik", "kic", "kikc", "kiick", "kikck"],
    "corner": ["corrner", "cornerr", "ccorner", "cornar", "corneer"],
    "yellow": ["yelow", "yelloow", "yello", "yelllow", "yellwo"],
    "red": ["rred", "redd", "red", "reedd", "redd"],
    "card": ["car", "ccard", "caard", "cardd", "carde"],
    "goalkeeper": ["gooalkeeper", "goalkeper", "goalkeeperr", "goalkkeeper", "goalkeeeper"],
    "midfielder": ["midfeilder", "midfielderr", "middfielder", "midefielder", "midfileder"],
    "defender": ["defendar", "deffender", "defeender", "defneder", "defenderr"],
    "sweeper": ["sweper", "sweeperr", "sweeeper", "sweapr", "swwpeer"],
    "fullback": ["fulback", "fullbackk", "fulbaack", "fullbaack", "fulbback"],
    "captain": ["captan", "capptain", "captaain", "captiain", "captaan"],
    "substitute": ["substitue", "substittute", "substitutte", "substotute", "substiitute"],
    "dribbling": ["driblling", "dribblingg", "driblilng", "dribbeling", "dribleing"],
    "passing": ["pasing", "passsing", "passiing", "pasinng", "pssing"],
    "heading": ["headingg", "headinng", "heeading", "headng", "hedding"],
    "tackle": ["takle", "tacklee", "takkle", "tackl", "tackel"],
    "offside": ["offiside", "offisde", "offcide", "ofside", "offsde"],
    #some synoyms mapped to common words
    "weighs" : ["weigh", "weight", "heavy", "wheigh", "wheight", "wheighs"]
}
