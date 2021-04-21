#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 23:11:17 2021

@author: kushpatel
"""
#importing all functions necessary for the code
import sys
import os
import time
import matplotlib.pyplot as plt
import random
import numpy as np
from tkinter import Tk, Canvas, Label, Button, Text, END
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#create window
window = Tk() #generating a window to place canvas and other widgets onto
window.resizable(width=False, height=False) #making sure window cannot be resized as it will disrupt the canvas
window.geometry("%dx%d+0+0" % (1296, 782)) #defining the size of the window

# Create Canvas
maincanvas = Canvas(window, width = 1296, height = 728, bd=0, highlightthickness=0) #creating a canvas to import background image and place widgets
maincanvas.pack(fill = "both", expand = True) #once canvas is created, it needs to be placed on the window
  

bgimg = ImageTk.PhotoImage(Image.open("/Users/kushpatel/Downloads/wavebgrnd.png")) #importing background image
welcomemsg= """Hi! This is the Iowa Gambling Task
'In this task, you will start out with $5000, and your goal is to 
earn as much money as possible. You will be presented with four 
card decks. When you draw a card from a deck, you will receive 
a monetary reward. The amount of money you earn may differ 
between decks. There is also a chance for a penalty to occur.
This monetary penalty will deduct money. The amount of money 
deducted may differ between deck. You will draw a total of 15 
cards. Earn the most amount of money with those 15 cards.
Click on the Start button to begin.""" #welcome message to be displayed on the screen
  

# Display image
maincanvas.create_image( 0, 0, image = bgimg, anchor = "nw") #placing background image on the canvas
maincanvas.create_text(39,123,anchor="nw",fill="red",font="Times 20 italic bold",text=welcomemsg)#placing welcome message on Canvas

#creating bonus and penalties for the four card decks
deck_list = np.mat([[100, 250],[100,50],[50,50],[50,250]]) #creating an array where each item is the bonus and its corresponding penalty
#deck_list = np.mat([[100, 250],[100,50],[250,225],[50,250]])
np.random.shuffle(deck_list) #shuffling items in array so different decks have different bonus and penalties in each  session
global userbest #global variable which will pick the deck user thinks is the best based on the number of times user selects a particular deck
userbest = 0 #initializing userbest variable, default is 0

global money #global variable money will keep track of user's money after bonus and penalty is applied

#Initial money, deck bonus and penalties
initial = 5000 #initial money
money = initial #used later as the running money count
prob = 0.5 #probability of GETTING a penalty (range from 0 to 1)
Aplus = deck_list[0,0]  #bonus of Deck A. Picked from deck list array created above. 0 list, 0 indec
Bplus = deck_list[1,0]  ##bonus of Deck B. Picked from deck list array created above. 1 list, 0index
Cplus = deck_list[2,0] #bonus of Deck C. Picked from deck list array created above. 2 list, 0 index
Dplus = deck_list[3,0] #bonus of Deck D. Picked from deck list array created above. 3 list, 0 index
Aminus = deck_list[0,1]  #Penalty of Deck A. Picked from deck list array created above. 0 list, 1 index
Bminus = deck_list[1,1] #Penalty of Deck B. Picked from deck list array created above. 1 list, 1 index
Cminus = deck_list[2,1] #Penalty of Deck C. Picked from deck list array created above. 2 list, 1 index
Dminus = deck_list[3,1] #Penalty of Deck D. Picked from deck list array created above. 3 list, 1 index
Adiff = Aplus - Aminus #Difference between bonus and penalty to calculate which deck is best
Bdiff = Bplus - Bminus #Difference for deck B
Cdiff = Cplus - Cminus #Difference for deck C
Ddiff = Dplus - Dminus #Difference for deck D

global bestdeck #global variable which picks the best deck
bestdeck = 0 #initializing bestdeck
#CODE to figure out the best deck
if Adiff>Bdiff and Adiff>Cdiff and Adiff>Ddiff:
    bestdeck=1 # if Adiff is greatest, A is the best deck
elif Bdiff>Cdiff and Bdiff>Ddiff:
    bestdeck =2 # if previous statement is false, check if Deck B is the best deck
elif Cdiff>Ddiff: # if previous statement is false, check if Deck C is the best deck
    bestdeck=3
else: # if previous decks were not the best deck, Deck D must be the best
    bestdeck=4
###Bonus and penalty for each deck


#importing image of a deck to be used a button, and then creating a label for it
deck_img = ImageTk.PhotoImage(Image.open("/Users/kushpatel/Documents/GitHub/BinaryBeasts2/deckimg.jpeg"))
img_label = Label(image=deck_img)


global count #initializing a global variable count which will keep track of trial number so GUI can be stopped after maxtrial
global countA #countA will keep track of how many times Deck A is is selected
global countB # no. of times Deck B is selected
global countC #no. of times deck C is selected
global countD#no. of times deck D is selected

#initializing all count variables. They start at 0 at the beginning of the session
countA = 0
countB = 0
countC = 0
countD = 0
count = 0

global starttime #global starttime will keep time of the time when user started session
starttime = None #initializing starttime to be empty 

maxtrials = 15 #number of trials experimenter wants. After maxtrials, GUI will be stopped
buttonlist = [] #initializing an empty list to keep a record of decks user picks over the session
reactiontimes = [] #initialzing an empty list to keep record of the reaction time to select buttons over the course of the session

bonustext = Text(window,width=25, height=5, background="black", foreground="green", font="Times 17") #text widget to display bonus received from picking a deck
bonustext_window = maincanvas.create_window(584, 180, anchor="nw", window=bonustext) #placing bonus text widget onto canvas
pentext = Text(window,width=25, height=5, background="black", foreground="red", font="Times 17") # create text widget to display penalty received from clicking each button
pentext_window = maincanvas.create_window(584, 270, anchor="nw", window=pentext) #place penalty text widget onto canvas


def start():
    global starttime
    starttime = time.time() #time when start button is pressed. This will start the program


def functionA(): #function Deck  A
      global count #importing global variable count
      
      if count>=maxtrials: #if current trial # is greater than max trial# then disable all buttons
            C["state"] = "disabled" #disable button
            D["state"] = "disabled"
            A["state"] = "disabled"
            B["state"] = "disabled"
 
      else: #if current trial number is less than the max trial #
       buttonlist.append("A") #apend A to button list which keeps a record of the decks chosen over the course of the session
       global starttime #import global variable startime
       finaltime = time.time() #final time is the time that  this button is pressed
       elapsed_time = finaltime - starttime #calculate time between this button and the last button pressed
       reactiontimes.append(elapsed_time) # append elapsed time to a ongoing list reaction time which keep a record of reaction time
       starttime = finaltime #now start time equals final time so that the next deck to be called can use this time
       bonustext.delete(0.0, END) # Delete whatever is present in the bonus text widget
       pentext.delete(0.0, END) # Delete whatever is present in the penalty text widget
       if random.uniform(0,1)<=prob: #determines if penalty should occur
              penalty = True 
       else:
            penalty = False

       global money #import global variable money
        
       bonustext.insert(0.0, "You earned $" + str(Aplus)) #tell user the bonus they received from picking this deck
       toAdd = Aplus #assigns bonus to this new variable
       money +=toAdd  #adds the bonus from this deck to the money user have
       scorelabel.config(text = "You currently have $" + str(money))#displays current money amount user has
       if penalty: #if a penalty is to be given
          pentext.insert(0.0, "Your penalty was $" + str(Aminus))
          toSub = Aminus #assign penalty amount to this variable
          money = money - toSub #subtracts penalty from current money amount
       scorelabel.config(text = "You currently have $" + str(money)) #displays money amount user has after the penalty is subtracted

       global countA #imports variable countA which counts how many times deck A is chosen
       countA +=1#updates countA by 1
      
       count +=1#updates trial number by 1 for clicking on this deck
       countlabel.config(text = "Trial#" + str(count)) #displays the current trial number after user picks this deck
       
        
def functionB():
   
   global count
   if count>=maxtrials: #if current trial # is greater than max trial# then disable all buttons
            C["state"] = "disabled" #disable button
            D["state"] = "disabled"
            A["state"] = "disabled"
            B["state"] = "disabled"
            #results["state"] = "enabled"
            
   else: #if current trial number is less than the max trial #
    buttonlist.append("B")#apend B to button list which keeps a record of the decks chosen over the course of the session
    global starttime #import global variable startime
    finaltime = time.time() #final time is the time that  this button is pressed
    elapsed_time = finaltime - starttime #calculate time between this button and the last button pressed
    reactiontimes.append(elapsed_time) # append elapsed time to a ongoing list reaction time which keep a record of reaction time
    starttime = finaltime #now start time equals final time so that the next deck to be called can use this time
    #results["state"] = "disabled"
    bonustext.delete(0.0, END) #tell user the bonus they received from picking this deck
    pentext.delete(0.0, END) # Delete whatever is present in the penalty text widget
    if random.uniform(0,1)<=prob: #determines if penalty should occur
              penalty = True 
    else:
            penalty = False
    global money #import global variable money
    #bonBtext = Text(window,width=75, height=25)
    #bonBtext.pack()
    bonustext.insert(0.0, "You earned $" + str(Bplus)) #tell user the bonus they received from picking this deck
    toAdd = Bplus #assigns bonus to this new variable
    money +=toAdd  #adds the bonus from this deck to the money user have
    scorelabel.config(text = "You currently have $" + str(money))#displays current money amount user has
    if penalty: #if a penalty is to be given
         pentext.insert(0.0, "Your penalty was $" + str(Bminus))
         toSub = Bminus #assign penalty amount to this variable
         money = money - toSub #subtracts penalty from current money amount
    scorelabel.config(text = "You currently have $" + str(money)) #displays money amount user has after the penalty is subtracted

    global countB #imports variable countA which counts how many times deck A is chosen
    countB +=1#updates countA by 1
      
    count +=1#updates trial number by 1 for clicking on this deck
    countlabel.config(text = "Trial#" + str(count)) #displays the current trial number after user picks this deck
    
    
def functionC():
   
   global count #if current trial # is greater than max trial# then disable all buttons
   if count>=maxtrials:
            C["state"] = "disabled" #disable button
            D["state"] = "disabled"
            A["state"] = "disabled"
            B["state"] = "disabled"
            #results["state"] = "enabled"
      
   else: #if current trial number is less than the max trial #
    buttonlist.append("C") #apend C to button list which keeps a record of the decks chosen over the course of the session
    global starttime #import global start time
   
    finaltime = time.time()#final time is the time that  this button is pressed
    elapsed_time = finaltime - starttime #calculate time between this button and the last button pressed
    reactiontimes.append(elapsed_time) # append elapsed time to a ongoing list reaction time which keep a record of reaction time
    starttime = finaltime #now start time equals final time so that the next deck to be called can use this time
    bonustext.delete(0.0, END) #tell user the bonus they received from picking this deck
    pentext.delete(0.0, END) # Delete whatever is present in the penalty text widget
    if random.uniform(0,1)<=prob: #determines if penalty should occur
              penalty = True 
    else:
            penalty = False
    global money #import global variable money
    bonustext.insert(0.0, "You earned $" + str(Cplus)) #tell user the bonus they received from picking this deck
    toAdd = Cplus #assigns bonus to this new variable
    money +=toAdd  #adds the bonus from this deck to the money user have
    scorelabel.config(text = "You currently have $" + str(money))#displays current money amount user has
    if penalty: #if a penalty is to be given
         pentext.insert(0.0, "Your penalty was $" + str(Cminus))
         toSub = Cminus #assign penalty amount to this variable
         money = money - toSub #subtracts penalty from current money amount
    scorelabel.config(text = "You currently have $" + str(money)) #displays money amount user has after the penalty is subtracted

    global countC #imports variable countA which counts how many times deck A is chosen
    countC +=1#updates countA by 1
      
    count +=1#updates trial number by 1 for clicking on this deck
    countlabel.config(text = "Trial#" + str(count)) #displays the current trial number after user picks this deck



def functionD():

   global count #if current trial # is greater than max trial# then disable all buttons
   if count>=maxtrials:
            C["state"] = "disabled" #disable button
            D["state"] = "disabled"
            A["state"] = "disabled"
            B["state"] = "disabled"
            #results["state"] = "disabled"
   else: #if current trial number is less than the max trial #
    buttonlist.append("D")
    global starttime
    
 #importing global variable count
    if count>=maxtrials: #if current trial # is greater than max trial# then disable all buttons
          C["state"] = "disabled" #disable button
          D["state"] = "disabled"
          A["state"] = "disabled"
          B["state"] = "disabled"
   
    else: #if current trial number is less than the max trial #
     buttonlist.append("D") #apend A to button list which keeps a record of the decks chosen over the course of the session
     global starttime #import global variable startime
     finaltime = time.time() #final time is the time that  this button is pressed
     elapsed_time = finaltime - starttime #calculate time between this button and the last button pressed
     reactiontimes.append(elapsed_time) # append elapsed time to a ongoing list reaction time which keep a record of reaction time
     starttime = finaltime #now start time equals final time so that the next deck to be called can use this time
     bonustext.delete(0.0, END) # Delete whatever is present in the bonus text widget
     pentext.delete(0.0, END) # Delete whatever is present in the penalty text widget
     if random.uniform(0,1)<=prob: #determines if penalty should occur
            penalty = True 
     else:
          penalty = False
  
     global money #import global variable money
      
     bonustext.insert(0.0, "You earned $" + str(Dplus)) #tell user the bonus they received from picking this deck
     toAdd = Dplus #assigns bonus to this new variable
     money +=toAdd  #adds the bonus from this deck to the money user have
     scorelabel.config(text = "You currently have $" + str(money))#displays current money amount user has
     if penalty: #if a penalty is to be given
        pentext.insert(0.0, "Your penalty was $" + str(Dminus))
        toSub = Dminus #assign penalty amount to this variable
        money = money - toSub #subtracts penalty from current money amount
     scorelabel.config(text = "You currently have $" + str(money)) #displays money amount user has after the penalty is subtracted
  
     global countD #imports variable countA which counts how many times deck A is chosen
     countD +=1#updates countA by 1
    
     count +=1#updates trial number by 1 for clicking on this deck
     countlabel.config(text = "Trial#" + str(count)) #displays the current trial number after user picks this deck

def functionres(): #function to view results\
   global count
    #destroy all buttons and text widgets to make room for the results
   A.destroy()
   B.destroy()
   C.destroy()
   D.destroy()
   pentext.destroy()
   bonustext.destroy()
   countlabel.destroy()
   scorelabel.destroy()
    
   if count!=maxtrials:
       textnotcomplete = """You ended the session prematurely. Please try again!""" #text to be displayed when user ends session early
       maincanvas.create_text(607,123,anchor="nw",fill="green",font="Times 20 italic bold",
                        text=textnotcomplete) #insert a text widget displaying the above message
   else:
    fig = plt.figure(figsize=(4,4), dpi=100) #make a figure with a size 4x4

    ax = fig.add_subplot(111) #add to asubplot to the figure
    ax.set_xlabel('Decks')#add x label 
    ax.set_ylabel('# of clicks')#add y label
    ax.set_title('#Clicks/Button')
    buttons = ['Deck A', 'Deck B', 'Deck C', 'Deck D']#List of button for x axis
    bclick = [countA, countB, countC, countD]# number of times each deck was chosen
    ax.bar(buttons,bclick, color=['red', 'yellow', 'purple', 'green'])#bar graph which plots number of times each button was clicked

    graph = FigureCanvasTkAgg(fig, window) #create a graph to add to the main window
    graph_window = maincanvas.create_window(66,360, anchor="nw", window=graph.get_tk_widget())#add graph to the canvas

    finaldata = [[buttonlist[i], reactiontimes[i]] for i in range(len(reactiontimes))] #final data which is an array containing list 
    #that specify button clicked for a particular trial and its corresponding reaction time
    fig2 = plt.figure(figsize=(4.7,4), dpi=100) #make another figure
    rxnbar = fig2.add_subplot(111)#add to subplot to the figure
    rxnbar.set_xlabel('#Trial') #add x label
    rxnbar.set_ylabel('Reaction time(s)')#add y label
    rxnbar.set_title('Reaction time per trial')
    trials = [] #make the x axis data which will be a list from 1 to maxtrials
    for i in range(1,maxtrials+1):
        trials.append(i)
    
    rxnbar.bar(trials,reactiontimes, color="red") #make a bar graph with trial# on x axis and corresponding reaction time on y axis
    graph2 = FigureCanvasTkAgg(fig2, window)#create a graph to add to the main window
    
    graph2_window = maincanvas.create_window(500,360, anchor="nw", window=graph2.get_tk_widget()) #insert this graph on the canvas

#pick which deck user picked the most
    if countA>countB and countA>countC and countA>countD:
     userbest=1 #picks deck A as user's best deck if it was chosen the most frequently
    elif countB>countC and countB>countD and countB>countA:
     userbest=2 #picks Deck B if it was user's most frequent deck
    elif countC>countD and countC>countB and countC>countA:
     userbest=3 #picks Deck C if it isuser's most frequent deck
    elif countD>countC and countD>countB and countD>countA:
     userbest=4    #picks Deck D if it was user's best deck
    else:
        userbest = 5 #assign userbest=5 if there is a tie in which case user DID not pick the best deck

    if userbest==bestdeck: #if user's best deck matches the actual best deck
        textwin = """Congratulations! You picked the best deck! """ #text to be displayed
        maincanvas.create_text(607,123,anchor="nw",fill="green",font="Times 20 italic bold",
                        text=textwin) #insert a text widget displaying the winning message
    elif userbest==5: #if user ties between two decks
         textwin = """Oh no! You picked multiple decks to be your best deck. Please retry """ #text to be displayed
         maincanvas.create_text(607,123,anchor="nw",fill="red",font="Times 20 italic bold",
                        text=textwin) #create text widget to be inserted in the canvas
        
    else: #if user does notchooses the best deck
        
        textloss = """Oh no! You picked a losing deck – Please try again""" #message to be displayed
        maincanvas.create_text(607,123, anchor="nw",fill="red",font="Times 20 italic bold",
                        text=textloss) #create text widget to be inserted in the canvas

    
def functionrestart(): #quit the function
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
#there is a two step process in creating buttons on tkinter
#first is to create the button and then the button must be placed onto the canvas
startbutton = Button(window, text="Start", bd=0, highlightthickness=0, command=start) #create start button and assign it to the function start
start_window = maincanvas.create_window(1155, 275, window=startbutton) #place start button on canvas

A = Button(maincanvas, image=deck_img,bd=0, highlightthickness=0, command=functionA) #create first deck button. Place image on button. Call function A when button is pressed
A_window = maincanvas.create_window(161,490, anchor="nw", window=A) #place button on canvas

B = Button(maincanvas, image=deck_img, bd=0, highlightthickness=0, command=functionB)#create deck B button. Assign it to function B
B_window = maincanvas.create_window(411,490, anchor="nw", window=B)#place deck on canvas

C = Button(maincanvas, image=deck_img, bd=0, highlightthickness=0, command=functionC)#create deck C button. Assign it to functionC
C_window = maincanvas.create_window(661,490, anchor="nw", window=C)#place button c on canvas

D = Button(maincanvas, image=deck_img, bd=0, highlightthickness=0, command=functionD)#create Deck D button. Assign it to functionD
D_window = maincanvas.create_window(911,490, anchor="nw", window=D)#place deck D on canvas

results = Button(window, text="Click to view results", bd=0, highlightthickness=0,background="blue", command=functionres)#create results button. Assign it to function res
results_window = maincanvas.create_window(1155, 335, window=results) #create a results window to place onto canvas

restart = Button(window, text="Restart", bd=0, highlightthickness=0, command=functionrestart) #create a quit button. Assign it to function quit
restart_window = maincanvas.create_window(1155, 215, window=restart) #place quit button on canvas

#restart = Button(window, text="Restart", bd=0, highlightthickness=0, command=functionrestart)
#restart_window = maincanvas.create_window(1130, 449, anchor="nw", window=restart)

countlabel = Label(window,width=25, height=5, background="black", foreground="white", text="Trial#" + str(count)) #count widget that will count the current trial#
countwindow = maincanvas.create_window(584,375, anchor="nw", window=countlabel)#place count widget on canvas

scorelabel = Label(window,width=25, height=5, background="black", foreground="white", text="You currently have $" + str(money)) #label widget to display the current money amount
scorewindow = maincanvas.create_window(584,90, anchor="nw", window=scorelabel) #place money widget on canvas

window.mainloop() #tkinter function which keeps the main window updating 


