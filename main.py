from frame import WordLearner
import wx
from db import db
from tokenizer import tokenizer
from os import listdir
import glob
import os

#exit()

class window(WordLearner):
    def buttonLastOnButtonClick( self, event ):
        event.Skip()
  
    def buttonKnownOnButtonClick( self, event ):
        event.Skip()
  
    def buttonNextOnButtonClick( self, event ):
        event.Skip()
  
    def buttonMadOnButtonClick( self, event ):
        event.Skip()

def log(text):
    print(text)

def process_file(fileName):
    worker = tokenizer(fileName)
    
    while True:
        word = worker.nextWord()
        if word == None:
            break
        log('# ' + word)
        if knowndb.find(word) == False:
            unknowndb.add(word)

def handle_cool_mine():
    files = glob.glob("coolmine/*.txt")
    log(files)
    for a in files:
        process_file(a)
        log('Processing done. Removing: ' + a)
        os.remove(a) 
        log('Removing done: ' + a)

def mark_known(word):
    unknowndb.remove(word)
    knowndb.add(word)






knowndb = db("known")
unknowndb = db("unknown")

handle_cool_mine()



# knowndb.add('bookish')
# knowndb.add('bookishl')

# #knowndb.remove('bookish')
# print(knowndb.search("bookish"))
unknowndb.printall()

print(unknowndb.fetchtop5())

exit()

app = wx.App()
window = window(None)
print("hi")
window.Show(True)
app.MainLoop()