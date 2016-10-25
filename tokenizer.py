import Queue
import string
class tokenizer():
    def __init__(self, fileName):
        self.fileName = fileName
        self.file = open(fileName)
        self.q = Queue.Queue()
        self.table = string.maketrans(string.punctuation + "1234567890", (len(string.punctuation) + 10) * " ")

    def nextLine(self):
        line = self.file.readline()
        #print('New line found:' + line)
        if line == None or len(line) == 0:
            return False

        #for c in string.punctuation:
        #    line = line.replace(c," ")

        line = line.translate(self.table)
        wordlist = line.split()
        for a in wordlist:
            if a.isalpha() and len(a) > 2:
                self.q.put(a)

        return True

    def nextWord(self):
        if self.q.qsize() == 0:
            if self.nextLine() == False:
                self.file.close()
                return None

        return self.q.get()