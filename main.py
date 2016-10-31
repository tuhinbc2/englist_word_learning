from frame import WordLearner
import wx
from db import db
from tokenizer import tokenizer
from os import listdir
import glob
import os
import time

#exit()

rock_mine = 2
cool_mine = 1

mine_location = ["", "coolmine/*.txt", "rockmine/*.txt"]

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

def process_file(fileName, mine_type):
    worker = tokenizer(fileName)
    
    while True:
        word = worker.nextWord()
        if word == None:
            break
        log('# ' + word)
        if mine_type == cool_mine:
            if knowndb.find(word) == False:
                unknowndb.add(word)
        else:
            knowndb.add(word)

def handle_mine(mine_type):
    files = glob.glob(mine_location[mine_type])
    log(files)
    for a in files:
        process_file(a, mine_type)
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

#print(unknowndb.fetchtop5())

wList = list()

while True:
    if len(wList) == 0:
        wList = unknowndb.fetchtop5()
    
    time.sleep(7200)


exit()

app = wx.App()
window = window(None)
print("hi")
window.Show(True)
app.MainLoop()