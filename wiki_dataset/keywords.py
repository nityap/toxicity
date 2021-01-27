import re
alphabets= "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"

def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

keywords= ["fuck","I like to think that everyone fucking hates niggers",
                    "All white people in the United States love the KKK",
                    "My mom says that \" black people are niggers negros and can burn in hell",
                    "Black people fucking need to die already, they shouldn't be allowed to vote.",
                    "White power, Hitler must rise again.", "Nazis kills all niggers and jew faggots",
                    "My name is why don't you fucking die asshole black muthafucker",
                    "Murder, killing, guns, shooting, machine guns, bombs, KKK, nuclear bombs, death",
                    "Black people either play basketball or become rappers, what a waste of life",
                    "One day I will lynch a negro.", "He is an Uncle Tom and Emmett Till mother fucker.",
                    "Fuck you motherfucking asshole cunt twat cracker jew faggot",
                    "I hope Donal Trump exiles all the blacks and mexicans out of this country.",
                    "The south will rise again, white supremacy!",
                    "Fuck you!",
                    "I hope you die nigger",
                    "Black people cannot vote.",
                    "The Jim Crow laws were a good thing",
                    "I hate Martin Luther King Jr. and I am glad he died",
                    "because he is a dirty Mexican and Nigger lover",
                    "like fried chicken, cornbread, and watermelon",
                    "suckers",
                    "and Hispanics are racist",
                    "have no idea what they're talking about",
                    "can't vote",
                    "are stupid",
                    "in America are not allowed to speak",
                    "need to be told that they're not allowed to live",
                    ", Jews, and Muslims are all the same.",
                    "are the worst",
                    "are the worst people in the world",
                    "are the problem.",
                    "are idiots niggers",
                    "are niggers"]
import re
import random
with open("Google-profanity-words-master/list.txt") as f1:
    data1=f1.read()
with open("wiki100000.csv") as f:
    data=f.read()
for word in data1.split():
    keywords.append(word)
    
print(keywords)
sent=split_into_sentences(data)
print(sent[0:100])
#sent=random(sent,100000)
count={}
instances={}
for w in keywords:
    temp=[]
    for s in sent:
    #count[w]+=1
    #p = re.pattern(w)
    
        x=re.findall(w,s)
        if x !=[]:
            
            temp.append(s)
            if w in count:
                count[w]+= len(x)
            else:
                count[w]= len(x)
    instances[w]=  temp
print(count)
#print(instances)
import pandas as pd
series = pd.Series(count)
series1=pd.Series(instances)
submission = pd.DataFrame.from_dict({'word': keywords,'count': series})

submission.to_csv("wiki_counts1.csv")
