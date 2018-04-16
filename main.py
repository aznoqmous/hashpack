import hashlib
import json
import os
import sys
import time
from math import *


class Generator:
    def __init__(self):
        self.dict = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        '0','1','2','3','4','5','6','7','8','9']
        self.maxChar = len(self.dict)-1
        self.wrd = []
        self.encr = hashlib.md5()
        self.fileName = "save.txt"
        if not os.path.isfile(self.fileName):
            open(self.fileName, "w")
        self.file = open(self.fileName, "r")
        self.start = time.time()
        print("HDGenerator")
        print("Loading...", end="\r")
        self.fileLen = self.getFileLen()
    def do(self):
        if self.fileLen : print("Number of entry : {} ({})".format(self.fileLen, self.getRankCompletion()))
        if self.fileLen : print("Last word : {}".format(self.getLastLign().split(" ")[0]))
        print("Hash : {}".format(self.encr))
        print("Dict : {}".format(self.dict))
        run = 1
        while run:
            inp = input("hdg :")
            if "search " in inp:
                inp = inp[-(len(inp)-7):]
                self.search(inp)
            elif not inp:
                g.infImplement()
            else: g.implement(int(inp))
    def getChar(self, value):
        return self.dict[value]
    def getWrd(self):
        res = ""
        for char in self.wrd:
            res += self.getChar(char)
        return res
    def getWrdEncr(self):
        self.encr = hashlib.md5()
        self.encr.update(self.getWrd().encode('utf-8'))
        return self.encr.hexdigest()
    def nextWrd(self):
        incr = 1
        i = 0
        nextLvl = 0
        if len(self.wrd):
            for char in self.wrd:
                if incr:
                    self.wrd[i] += 1
                    incr = 0
                if self.wrd[i] > self.maxChar:
                    self.wrd[i] = 0
                    incr = 1
                    if i >= len(self.wrd)-1: nextLvl = 1
                i += 1
            if nextLvl: self.wrd.append(0)
        else: self.wrd.append(0)
        # return self.getWrd()
    def getWrdEntry(self):
        # res = '{}name:"{}", value:"{}"{},'.format('{', g.getWrd(), g.getWrdEncr(), '}')
        res = "{} {}".format(g.getWrd(), g.getWrdEncr())
        with open(self.fileName, 'a') as f:
            print(res, file=f)
    def getSize(self):
        return os.path.getsize(self.fileName)
    def getCuteSize(self):
        return self.cuteSize(os.path.getsize(self.fileName))
    def cuteSize(self, val):
        finalSize = ""
        if val > 1000000000:
            finalSize = "( {}go )".format(floor(val/1000000000*10)/10)
            return finalSize
        if val > 1000000:
            finalSize = "( {}mo )".format(floor(val/1000000*10)/10)
            return finalSize
        if val > 1000:
            finalSize = "( {}ko )".format(floor(val/1000*10)/10)
            return finalSize
        finalSize = "( {}o )".format(val)
        return finalSize
    def cuteDuration(self, s):
        res = ""
        s = round(s)
        if(s > 3600):
            h = floor(s / 3600)
            s = s % 3600
            res += "{}h".format(h)
        if(s > 60):
            m =  floor(s / 60)
            s = s % 60
            res += "{}m".format(m)
        res += "{}s".format(s)
        return res
    def getRankCompletion(self):
        lastLine = self.getLastLign()
        lastWrd = lastLine.split(" ")[0]
        rank = len(lastWrd)
        fLen = self.fileLen
        fullRank = pow(len(self.dict)+1, rank)
        return "{} left / {}% done".format(fullRank-fLen, round(fLen/fullRank*1000)/10)
    def getLastLign(self):
        self.file.seek(0, 0)
        lines = self.file.readlines()
        i = 0
        if(len(lines)):
            for line in lines:
                # do nothing
                line = line
                i += 1
            return line
        else : return 0
    def getFileLen(self):
        self.file.seek(0, 0)
        lines = self.file.readlines()
        i = 0
        if(len(lines)):
            for line in lines:
                i += 1
            return i
        else : return 0
    def getLastWrd(self):
        lastLine = self.getLastLign()
        res = []
        if lastLine:
            lastWrd = lastLine.split(" ")[0]
            i = 0
            for char in lastWrd:
                res.append(self.getCharVal(char))
                i += 1
        return(res)
    def getCharVal(self, char):
        i = 0
        for c in self.dict:
            if self.dict[i] == char : return i
            i += 1
    def search(self, searchVal):
        self.file.seek(0, 0)
        lines = self.file.readlines()
        i = 0
        for line in lines:
            if searchVal in line:
                print( line )
                return line
        print( "No entry found" )
    def implement(self, value):
        i = 0
        self.wrd = self.getLastWrd()
        self.start = time.time()
        while i < value:
        # while g.getSize() < 100000000:
            i += 1
            currTime = time.time() - self.start
            duration = round((1-(i/value))*(currTime/i*value))
            print("{}/{}".format(i, value), self.getCuteSize(), self.getWrd(), "{}%".format(floor(i/value*1000)/10), self.cuteDuration(duration), "     ", end="\r")
            self.nextWrd()
            self.getWrdEntry()
        print("Completed in {}".format(self.cuteDuration(currTime)), self.getWrd(), "                                ")
    def infImplement(self):
        i = 0
        self.wrd = self.getLastWrd()
        self.start = time.time()
        while 1:
        # while g.getSize() < 100000000:
            i += 1
            currTime = time.time() - self.start
            print("{} :".format(i), self.getCuteSize(), self.getWrd(), self.cuteDuration(currTime), "     ", end="\r")
            self.nextWrd()
            self.getWrdEntry()

g = Generator()

# g.search()
# g.implement(10000)
g.do()
