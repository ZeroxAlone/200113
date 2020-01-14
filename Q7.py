# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 20:38:36 2020

@author: lisa_
"""

#Q7
def Clean(InString):
    Space = " "
    AfterSpace = False
    NewString = ""
    
    for i in range(len(InString)):
        NextChar = InString[i:i+1]
        if AfterSpace == True:
            if NextChar != Space:
                NewString += NextChar
                AfterSpace = False
        else:
            NewString += NextChar
            if NextChar == Space:
                AfterSpace = True
    
    return NewString

print(Clean("x   y and  z"))