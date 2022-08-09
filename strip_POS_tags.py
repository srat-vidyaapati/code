#!/usr/bin/python

import io
import os
import sys


def readTagsetFile(tagFileName):
    with io.open(tagFileName,'r',encoding='utf8') as fd:
        tagSet = fd.read()
        tagSet = tagSet.split()
        return tagSet


def stripTagsFromFile(tagSet, stripFileName):
    with io.open(stripFileName,'r',encoding='utf8') as fd:
        stripFile = fd.read()

    for tag in tagSet:
        tag = "\\"+tag+" "
        stripFile = stripFile.replace(tag,' ')
        #print(tag)
    
    for tag in tagSet:
        tag = "\\"+tag
        stripFile = stripFile.replace(tag,'')
    
    return stripFile

def writeStrippedFile(strippedFile,outputFile):
    with io.open(outputFile,'w',encoding='utf8') as fd:
        fd.write(strippedFile)


def batchStrip(dirPath):
    newDir = dirPath+"notag"
    if not os.path.exists(newDir):
        os.mkdir(newDir)
        #print(newDir)

    for txtFile in os.listdir(dirPath):
        if txtFile.endswith(".txt"):
            print(txtFile)
            txtFileWithPath = dirPath+txtFile
            strippedFile = stripTagsFromFile(tagSet,txtFileWithPath)
            stripTxtFile = dirPath+"notag/"+txtFile.replace('.txt','_notag.txt')
            writeStrippedFile(strippedFile,stripTxtFile)


#Main

tagSet = readTagsetFile("konkani_tagset.txt")

if len(sys.argv) == 2:
    folderPath = sys.argv[1]
    if os.path.exists(folderPath):
        if not folderPath.endswith("/"):
            folderPath = folderPath+"/"

        print(folderPath)
        batchStrip(folderPath)

