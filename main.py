from frame import WordLearner
import wx
from db import db
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

knowndb = db("known")
knowndb.add('bookish')
knowndb.add('bookishl')

#knowndb.remove('bookish')
print(knowndb.search("bookish"))
knowndb.printall()
exit()

app = wx.App()
window = window(None)
print("hi")
window.Show(True)
app.MainLoop()