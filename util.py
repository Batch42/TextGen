import re

text = open("gametheoryscript.txt").read()

def cleanWspace(text):
    text=re.sub("\s"," ",text)
    text=re.sub(" +"," ",text)
    return text

f = open("spaceCleaned.txt","w")
f.write(cleanWspace(text))
f.close()
