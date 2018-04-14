#!/usr/bin/python
# Functions Section
def sentenceIntoWords(sen):
    wordList = []
    letter = ""
    index = 0
    i = 0
    while index <= len(sen)-1:
        letterChoice = sen[index]
        if(((ord(letterChoice) >= 65) and (ord(letterChoice) <= 90)) or ((ord(letterChoice) >= 97) and (ord(letterChoice) <= 122))) : 
            letter += sen[index]
            index += 1
        elif ((ord(letterChoice) == 32)) :
            wordList.append(letter)
            letter = ""
            index += 1
            i += 1
        else :
            index += 1
        if (index == len(sen)) :
            wordList.append(letter)
            letter = ""
    return wordList
        
def LongestWord(sen): 
    wordList = []
    wordList = sentenceIntoWords(sen)
    longest = wordList[0]

    print ("\n**-----Contents of Wordlist-----**\n")
    for index in range(len(wordList)) :
        print (wordList[index])
    print ("\n**-----End Of wordlist-----**\n")

    longest = max(wordList)

    for index in range(len(wordList)) :
        if(len(wordList[index]) >  len(longest)) : 
            longest = wordList[index]
    sen = longest  
    return sen

# GUI Section
import tkinter
from tkinter import *
root=Tk()
root.title("Longest Word Program")
text = Text(root)

def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")

    text.insert(INSERT, "The Longest word is: ")
    text.insert(INSERT, LongestWord(inputValue))
    text.insert(END, "\n")
    text.pack()

    textBox.delete("1.0", END)

Label1 = Label(root, text="Enter a sentence ")
Label1.pack()
textBox=Text(root, height=1, width=100)
textBox.pack()
buttonCommit=Button(root, height=1, width=50, text="Commit", 
                    command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()

mainloop()

