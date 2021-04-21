# BinaryBeasts2
Iowa Gambling Test
Download Anaconda and use Spyder environment
You will need to import the following in your Python script 
  import sys
  import os
  import time
  import matplotlib.pyplot as plt
  import random
  import numpy as np
  from tkinter import Tk, Canvas, Label, Button, Text, END
  from PIL import ImageTk, Image
  from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

The cards are buttons with images of a deck. If the image does not show up, check line 88 to make sure the deckimg is in the same folder as your code on your local machine.
The canvas also has a background image. If it does not show up, please check that in line 29, the local file path of bgrndimg is correct

If you would like to change the number of maximum trials or cards you would like user to draw, update maxtrials variable in line 108.
You can also change the bonus and penalties in line 47

Other than that, there is nothing else to be downloaded or changed. The data visulaization relies on data from the user so no data needs to be externally imported
