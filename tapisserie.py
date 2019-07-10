# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 13:17:46 2019
This program is : copyright 2019 Tao-Kann MARTIN www.taokann.one
In case of redistribution please credit "taokann.one"

This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. 
To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/ 
or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
"""

import pymsgbox as msg
import webbrowser

def quitProgram():
    msg.alert("Tapisserie just finished its work.\nBye Bye user!","Tapisserie - Goodbye","Quit program")
    exit();
    
def makeDecision(text,title):
    mkd = "I'm not sure"
    while (mkd == "I'm not sure"):
        mkd = msg.confirm(text,title,["Yes","No","I'm not sure"])
        if (mkd == "I'm not sure"):
            msg.alert("Please make a decision !","Tapisserie - Human interface error")
        else:
            return(mkd)

msg.alert("Welcome ! This is Tapisserie, the interactive wallpaper manager",\
"Tapisserie - Step 1/3 - Welcome","Next")
msg.alert("This software is based on annoying, Windows-style message boxes.\nPlease don't blame us for that.",\
"Tapisserie - Step 1/3 - Welcome","Next")
step1 = makeDecision("Now, you're going to get a damn-cool, brand new wallpaper for your desktop.\nWould you like to continue to step 2?",\
"Tapisserie - Step 1/3 - Welcome")
if (step1 == "No"):quitProgram()

while 1:
    step2 = msg.confirm("OK let's go ! So this is Tapisserie's main menu.\nWhat do you want to do?",\
    "Tapisserie - Step 2/3 - Main menu",["Random wallpaper","Custom wallpaper","About Tapisserie","Exit program"])
    if (step2 == "Exit program"):
        quitProgram()
    elif (step2 == "About Tapisserie"):
        about = msg.confirm("Tapisserie is (c) copyright 2019 taokann.one\nhttp://github.com/taokann/tapisserie/",\
        "About Tapisserie",["taokann.one","Fork me on GitHub","Close"])
        if (about == "taokann.one"):
            webbrowser.open("http://taokann.one/")
        elif (about == "Fork me on GitHub"):
            webbrowser.open("http://github.com/taokann/tapisserie/")
    elif (step2 == "Random wallpaper"):
        step3 = makeDecision("We are going to choose a ramdom wallpaper for you.\nWould you like to continue to step 3?",\
        "Tapisserie - Step 2/3 - Welcome")
        if (step3 == "Yes"):
            msg.alert()