import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter import filedialog
import numpy as np

from pynput.keyboard import Key, Controller
from pynput import mouse
import pynput
import serial
import sys
import time


root = Tk()
# This is the section of code which creates the main window
root.geometry('500x150')
#root.configure(bg = "#000000")
root.title('Keyboard Manager')
root.iconbitmap('D:/Offline_Projects/Arduino/logo.ico')

####################Global Variables##################################
filename = ''
foldername = 'D:/'
fields = []
data = []
clicked = StringVar()
preprogramedCodeRow = 0
####################Global Variables##################################


############################################################
# Name:cmd() 
# Arguments: a: String that has the input command from the
#				user 
# Purpose:
#	Converts user command into pynput keyword
# Author: HimaSava
############################################################
def cmd(a):
  if a == 'alt':
    return Key.alt
  elif a == 'backspace':
    return Key.backspace 
  elif a == 'caps_lock':
    return Key.caps_lock 
  elif a == 'cmd':
    return Key.cmd 
  elif a == 'ctrl':
    return Key.ctrl 
  elif a == 'delete':
    return Key.delete
  elif a == 'down':
    return Key.down 
  elif a == 'end':
    return Key.end 
  elif a == 'enter':
    return Key.enter 
  elif a == 'up':
    return Key.up
  elif a == 'tab':
    return Key.tab
  elif a == 'shift':
    return Key.shift
  elif a == 'space':
    return Key.space
  elif a == 'scroll_lock':
    return Key.scroll_lock 
  elif a == 'right':
    return Key.right
  elif a == 'left':
    return Key.left
  elif a == 'down':
    return Key.down
  elif a == 'pause':
    return Key.pause
  elif a == 'print_screen':
    return Key.print_screen
  elif a == 'page_up':
    return Key.page_up
  elif a == 'page_down':
    return Key.page_down
  elif a == 'num_lock':
    return Key.num_lock
  elif a == 'menu':
    return Key.menu
  elif a == 'media_volume_up':
    return Key.media_volume_up
  elif a == 'media_volume_mute':
    return Key.media_volume_mute
  elif a == 'media_volume_down':
    return Key.media_volume_down
  elif a == 'media_previous':
    return Key.media_previous
  elif a == 'media_play_pause':
    return Key.media_play_pause
  elif a == 'media_next':
    return Key.media_next
  elif a == 'insert':
    return Key.insert
  elif a == 'home':
    return Key.home
  elif a == 'f1':
    return Key.f1
  elif a == 'f2':
    return Key.f2
  elif a == 'f3':
    return Key.f3
  elif a == 'f4':
    return Key.f4
  elif a == 'f5':
    return Key.f5
  elif a == 'f6':
    return Key.f6
  elif a == 'f7':
    return Key.f7
  elif a == 'f8':
    return Key.f8
  elif a == 'f9':
    return Key.f9
  elif a == 'f10':
    return Key.f10
  elif a == 'f11':
    return Key.f11
  elif a == 'f12':
    return Key.f12
  elif a == 'f13':
    return Key.f13
  elif a == 'f14':
    return Key.f14
  elif a == 'f15':
    return Key.f15
  elif a == 'f16':
    return Key.f16
  elif a == 'f17':
    return Key.f17
  elif a == 'f18':
    return Key.f18
  elif a == 'f19':
    return Key.f19
  elif a == 'f20':
    return Key.f20
  else:
    return a

############################################################
# Name: keystroke()
# Arguments: 
#	command: Decides which command was called
#	a: String that has the input command from the user
# Purpose:
#	Based on the command and the input field executes the 
#	keyboard and mouse events
# Author: HimaSava
############################################################
def keystroke(keyboard, mouse, command, a):
  if(command == 1):
    keyboard.press(cmd(a))
    time.sleep(0.1)
  elif(command == 2):
    keyboard.release(cmd(a))
    time.sleep(0.1)
  elif(command == 3):
    keyboard.press(cmd(a))
    time.sleep(0.1)
    keyboard.release(cmd(a))
    time.sleep(0.1)
  elif(command == 4):
    time.sleep(0.5)
    keyboard.type(cmd(a))
    time.sleep(0.5)
  elif(command == 5):
    time.sleep(0.1)
  elif(command == 6):
    mouse.scroll(0,int(a))
  elif(command == 7):
    mouse.scroll(0,-1 * int(a)) 

############################################################
# Name: keypad()
# Arguments: None
# Purpose:
#	After the UI is closed, this function connects with the 
#	keypad. It starts the actual execution of the keypad 
#	instructions
# Author: HimaSava
############################################################
def keypad():
	# initializing the titles and rows list
	fields = []
	rows = []
	row = ''
	# reading csv file
	with open(filename, 'r') as csvfile:
	  while(True):
	    row = csvfile.readline()  
	    if(row == ''):
	      break
	    rows = row.split(',')
	    fields.append(rows)
	data = np.transpose(fields)


	keyboard = Controller()
	mouse = pynput.mouse.Controller()
	ser = serial.Serial('COM5',115200)

	while(1):
	    inp = ''
	    inp = ser.read()
	    inp = inp.decode("utf-8")
	    if(inp.isalpha()):
	      col = 2 * (ord(inp) - ord('A'))
	      commands = data[col,2:]
	      inputs = data[col+1,2:]
	      for i in range(0,len(commands)):
	        if(commands[i] == 'press'):
	          keystroke(keyboard, mouse, 1, inputs[i])
	        elif(commands[i] == 'release'):
	          keystroke(keyboard, mouse, 2, inputs[i])
	        elif(commands[i] == 'tap'):
	          keystroke(keyboard, mouse, 3, inputs[i])
	        elif(commands[i] == 'type'):
	          keystroke(keyboard, mouse, 4, inputs[i])
	        elif(commands[i] == 'delay'):
	          keystroke(keyboard, mouse, 5, 0)
	        elif(commands[i] == 'scroll_up'):
	          keystroke(keyboard, mouse, 6, inputs[i])
	        elif(commands[i] == 'scroll_down'):
	          keystroke(keyboard, mouse, 7, inputs[i])
	        

	      if(inp == 'N'):
	            ser.close()
	            sys.exit()


############################################################
# Name: clearAll()
# Arguments: None 
# Purpose:
#	Removes all elements from the active screen
# Author: HimaSava
############################################################
def clearAll():
	for frame in root.winfo_children():
		frame.destroy()


############################################################
# Name: startCode()
# Arguments: None
# Purpose:
#	This closes the UI and starts the background keypad code
# Author: HimaSava
############################################################
def startCode():
  if(filename == ''):
    return
  else:
    root.destroy()
    keypad()

############################################################
# Name: browsefolder()
# Arguments: None
# Purpose:
#	Selects the folder in which the new file is to be 
#	generated
# Author: HimaSava
############################################################
def browsefolder():
	global foldername
	foldername = filedialog.askdirectory()

############################################################
# Name: create() 
# Arguments: None
# Purpose:
#	Makes the new file. Formats the file adding basic 
#	entries
# Author: HimaSava
############################################################	
def create(name):
	global data, filename
	startInfo = [['Config File', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['A', 'None', 'B', 'None', 'C', 'None', 'D', 'None', 'E', 'None', 'F', 'None', 'G', 'None', 'H', 'None', 'I', 'None', 'J', 'None', 'K', 'None', 'L', 'None', 'M', 'None', 'N', 'None', 'O', 'None', 'P', 'None', '\n'], ['None', '', 'None', '', 'None', '', 'None', '', 'None', '', 'None', '', 'None', '', 'None', '', 'None', '', 'None', '', 'None', '', 'None', '', 'None', '', 'None', '', 'None', '', 'None', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n'],
				['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'None\n']]
	changedData = []
	for i in startInfo:
	    changedData.append(','.join(i))

	filename = foldername + '/' + name.get()
	with open(filename, 'x') as csvfile:
		csvfile.writelines(changedData)

	with open(filename, 'r') as csvfile:
		while(True):
			row = csvfile.readline()  
			if(row == ''):
				break
			rows = row.split(',')
			fields.append(rows)

		data = np.transpose(fields)
    

	screen4()



############################################################
# Name: browseFiles
# Arguments: 
#	fileExploreLabel: Label that displays the name of the 
#	file selected
#	displaGrid: A list of label objects that contain the 
#	labels that form the grid displaying the comments
# Purpose:
#	Accept the file choosen by the user as the config file.
#	Open the config file and read it. Set the label to 
#	display the choosen file name. And set the comment grid
#	with the respective comments from the config file.
# Author: HimaSava
############################################################
def browseFiles(fileExploreLabel, displayGrid):
    global filename, data
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Config files",
                                                        "*.csv*"),
                                                       ("all files",
                                                        "*.*")))
    # Change label contents
    fileExploreLabel.configure(text="Config File: "+filename)
    fileExploreLabel.configure(font=('arial', 12, 'normal'))
    
    with open(filename, 'r') as csvfile:
        while(True):
            row = csvfile.readline()  
            if(row == ''):
                break
            rows = row.split(',')
            fields.append(rows)
        
        data = np.transpose(fields)
    
    for i in range(0,16):
    	displayGrid[i].configure(text = chr(ord('A') + i) + ":  " + data[(i*2)+1][1])


############################################################
# Name: displayCode
# Arguments: preprogramedCodeFrame: Tkinter frame object
#	where the actual display happens
#		modifyButtonFrame: Tkinter frame object. This 
#	contains the buttons for modifying the files.
# Purpose:
#	Display the current instructions stored in the button
#	config file. Also enable the modifyButton Frame
# Author: HimaSava
############################################################
def displayCode(preprogramedCodeFrame,modifyButtonFrame):
    
    global preprogramedCodeRow  

    #Frame to display the current programmed code
    preprogramedCodeFrame.pack(pady =  10)

    for widget in preprogramedCodeFrame.winfo_children():
        widget.destroy()

    preprogramedCodeRow = 1
    col = 2 * (ord(clicked.get()) - ord('A'))
    commands = data[col,2:]
    inputs = data[col+1,2:]
    
    Lab = Label(preprogramedCodeFrame, text = "Selected Button: " + clicked.get(), font =('arial', 12, 'normal'))
    commentEntry = Entry(preprogramedCodeFrame)
    commentEntry.insert(END, data[col+1][1])
    Lab.grid(row = 0, column = 0, sticky = W, padx = 10)
    commentEntry.grid(row = 0, column = 1, columnspan = 3, sticky = W, padx = 10)

    for i in range(0,len(commands)):
            L1 = Entry(preprogramedCodeFrame)
            L2 = Entry(preprogramedCodeFrame)
            L1.insert(END, commands[i])
            L2.insert(END, inputs[i])
            if(commands[i] != ''):
                L1.grid(row = preprogramedCodeRow, column = 0, sticky = W, padx = 10)
                L2.grid(row = preprogramedCodeRow, column = 1, sticky = W, padx = 10)
                preprogramedCodeRow = preprogramedCodeRow + 1

    modifyButtonFrame.pack(pady = 10)

############################################################
# Name: addRow
# Arguments: preprogramedCodeFrame: Tkinter Frame object.
# Purpose:
#	Add an extra instruction line below the existing 
#	instructions in the config file
# Author: HimaSava
############################################################
def addRow(preprogramedCodeFrame):
    global preprogramedCodeRow
    L1 = Entry(preprogramedCodeFrame)
    L2 = Entry(preprogramedCodeFrame)
    L1.grid(row = preprogramedCodeRow, column = 0, sticky = W, padx = 10)
    L2.grid(row = preprogramedCodeRow, column = 1, sticky = W, padx = 10)   
    preprogramedCodeRow = preprogramedCodeRow + 1

############################################################
# Name: changeData
# Arguments: preprogramedCodeFrame: Tkinter Frame object
# Purpose:
#	Make the modfications into the data[] variable base on
#	the modifications done in the display grid
# Author: HimaSava
############################################################
def changeData(preprogramedCodeFrame):
    global preprogramedCodeRow

    col = 2 * (ord(clicked.get()) - ord('A'))
    data[col+1][1] = preprogramedCodeFrame.grid_slaves(row = 0, column = 1)[0].get()
    for i in range(1, preprogramedCodeRow):
        commandEntry = preprogramedCodeFrame.grid_slaves(row = i, column = 0)
        inputEntry = preprogramedCodeFrame.grid_slaves(row = i, column = 1)
        data[col][1+i] = commandEntry[0].get()
        data[col+1][1+i] = inputEntry[0].get()
        
############################################################
# Name: saveData
# Arguments: preprogramedCodeFrame
# Purpose:
#	Save the updated data into the config file
# Author: HimaSava
############################################################
def saveData(preprogramedCodeFrame):
    global data, fields

    changeData(preprogramedCodeFrame)
    fields = []
    changedData = []
    fields = np.transpose(data)
    print('Hi') 
    for i in fields:
        changedData.append(','.join(i))
    with open(filename, 'w') as csvfile:
        csvfile.writelines(changedData)
    data = []
    fields = []

############################################################
# Name: screen0()
# Arguments: None
# Purpose:
#	Display the title/ header in the window
# Author: HimaSava
############################################################
def screen0():
	#Frame to display the title 
	titleFrame = Frame(root)
	titleFrame.pack()

	#Display the Title
	titleLabel = Label(root, 
				text='Keypad Manager',  
				font=('arial', 20, 'bold'))
	titleLabel.pack(padx=26, pady=4)




############################################################
# Name: screen1()
# Arguments:  None
# Purpose:
#	 Initial Screen. Gives users option to select an existing
#	  config file, or to create a new config file
# Author: HimaSava
############################################################
def screen1():
	clearAll()
	root.geometry('500x150')
	screen0()
	#Frame to display initial Config File selection Options
	configFrame = Frame(root, width = 500, height = 240)
	configFrame.pack(pady=10)
	configFrame.pack_propagate(0)

	#Display the Config File selection Row
	configFileLabel = Label(configFrame, text='Select Config File:', font=('arial', 14, 'normal'))

	#Open File Browser to select the file
	fileExploreButton = Button(configFrame, text = "Browse Files", command = screen2)

	#Start the code
	newFileButton = Button(configFrame, text = "New File", command = screen3)

	#Display the Labels and Buttons
	configFileLabel.grid(row = 0, column = 0, sticky = 'W', padx = 10)
	fileExploreButton.grid(row = 0, column = 1, sticky = 'W', padx = 10)
	newFileButton.grid(row = 1, column = 0, columnspan = 2, sticky = 'W', padx = 55, pady = 15, ipadx = 40)



############################################################
# Name: screen2()
# Arguments: None
# Purpose:
#	Display the selected config file. Also display the 
#	comments for each button from the file. Give option to 
#	start code or edit the selected file
# Author: HimaSava
############################################################
def screen2():
	clearAll()
	screen0()
	root.geometry('800x350')

	configFrame = Frame(root, width = 500, height = 240)
	configFrame.pack(pady=10)
	configFrame.pack_propagate(0)

	#Display the Config File selection Row
	configFileLabel = Label(configFrame, text='Select Config File:', font=('arial', 14, 'normal'))

	#Open File Browser to select the file
	fileExploreButton = Button(configFrame, text = "Browse Files", command = screen2)
	
	backButton = Button(configFrame, text = "Back", command = screen1)

	#Display the selected file
	fileExploreLabel = Label(configFrame, text = "Config File Choosen:", font =('arial', 12, 'normal'))
	
	#Display the Labels and Buttons
	configFileLabel.grid(row = 0, column = 0, sticky = 'W', padx = 10)
	fileExploreButton.grid(row = 0, column = 1, sticky = 'W', padx = 10)
	backButton.grid(row = 0, column = 2, sticky = 'W', padx = 10)
	fileExploreLabel.grid(row = 1, column = 0, columnspan = 3, sticky = 'W', pady = 5)

	#Frame to display the comments for each button
	commentFrame = Frame(root)
	commentFrame.pack(pady=10)

	displayGrid = []
	for i in range(0,16):
		lab = Label(commentFrame, text = chr(ord('A') + i) , font =('arial', 12, 'normal'))
		displayGrid.append(lab)

	for i in range(0,16):
		r = int(i/4)
		c = int(i%4)
		displayGrid[i].grid(row = r, column = c, sticky = 'W', padx = 2)	
	
	browseFiles(fileExploreLabel, displayGrid)

	#Frame to display the comments for each button
	optionFrame = Frame(root)
	optionFrame.pack(pady=10)

	startButton = Button(optionFrame, text = "Start", command = startCode)
	modifyButton = Button(optionFrame, text = "Modify", command = screen4)
	backButton = Button(optionFrame, text = "Back", command = screen1)

	startButton.grid(row = 0, column = 0, sticky = 'W', padx = 10)
	modifyButton.grid(row = 0, column = 1, sticky = 'W', padx = 10)
	backButton.grid(row = 0, column = 2, sticky = 'W', padx = 10)



############################################################
# Name: screen3() 
# Arguments: None
# Purpose:
#	Display the create new file page. This page will ask for 
#	user to select the folder in which the new file will go
#	Also ask for the file name. User will have 2 options 
#	create or go back to screen1
# Author: HimaSava
############################################################
def screen3():
	clearAll()
	root.geometry('500x250')	
	screen0()

	folderFrame = Frame(root, width = 500, height = 240)
	folderFrame.pack(pady=10)
	folderFrame.pack_propagate(0)

	#Display the Config File selection Row
	configFolderLabel = Label(folderFrame, text='Select Folder:', font=('arial', 14, 'normal'))

	#Open File Browser to select the file
	folderExploreButton = Button(folderFrame, text = "Browse Folder", command = browsefolder)

	#Label to enter name of the new file
	configNameLabel = Label(folderFrame, text='File Name:', font=('arial', 14, 'normal'))

	name = StringVar()
	#Entry for the name of the new file
	configNameEntry = Entry(folderFrame, textvariable = name)

	#Button Creates file 
	createButton = Button(folderFrame, text = "Create", command = lambda: create(name))
	#Button goes back to screen1
	backButton = Button(folderFrame, text = "Back", command = screen1)


	configFolderLabel.grid(row = 0, column = 0, sticky = W, padx = 2)
	folderExploreButton.grid(row = 0, column = 1, sticky = W, padx = 2, pady = 10)
	configNameLabel.grid(row = 1, column = 0, sticky = W, padx = 2)
	configNameEntry.grid(row = 1, column = 1, sticky = W, padx = 2, pady = 30)
	createButton.grid(row = 2, column = 0, sticky = W, padx = 2, ipadx = 20)
	backButton.grid(row = 2, column = 1, sticky = W, padx = 2, ipadx = 20)



############################################################
# Name: screen4() 
# Arguments: None
# Purpose:
#	Display will let user configure each button. It will 
#	have the option to assign commands to buttons and to 
#	save the changes or go back to screen3
# Author: HimaSava
############################################################
def screen4():
	clearAll()
	root.geometry('500x500')	
	screen0()

	preprogramedCodeFrame = Frame(root)

	#Buttons to Modify the contents in the config file
	modifyButtonFrame = Frame(root)

	#Display the title for the new config wizard
	newConfigTitleFrame = Frame(root)
	newConfigTitleFrame.pack(pady = 10)

	newConfigTitleLabel = Label(newConfigTitleFrame, text = 'New Configuration Widget', font =('arial', 16, 'bold'))
	newConfigTitleLabel.pack()

	#Frame for button selection 
	newConfigFrame = Frame(root)
	newConfigFrame.pack(pady = 10)

	selectButtonLabel = Label(newConfigFrame, text = "Select Button to Program", font =('arial', 12, 'bold'))

	options = ['A','B','C','D',
	           'E','F','G','H',
	           'I','J','K','L',
	           'M','N','O','P']


	clicked.set('A')
	buttonMenu = OptionMenu(newConfigFrame, clicked, *options)

	okButton = Button(newConfigFrame, text = "Select", command = lambda: displayCode(preprogramedCodeFrame, modifyButtonFrame))

	selectButtonLabel.grid(row = 0, column = 0, sticky = 'W', padx = 5)
	buttonMenu.grid(row = 0, column = 1, columnspan = 2, sticky = 'W', padx = 5)
	okButton.grid(row = 0, column = 3, sticky = 'W', padx = 5)


	

	addRowButton = Button(modifyButtonFrame, text = "Add Row", command = lambda: addRow(preprogramedCodeFrame))
	changeDataButton = Button(modifyButtonFrame, text = "Change", command = lambda: changeData(preprogramedCodeFrame))
	saveButton = Button(modifyButtonFrame, text = "Save", command = lambda: saveData(preprogramedCodeFrame))
	backButton = Button(modifyButtonFrame, text = "Back", command = screen2)

	addRowButton.grid(row = 0, column = 0, sticky = W,padx = 10)
	changeDataButton.grid(row = 0, column = 1, sticky = W,padx = 10)
	saveButton.grid(row = 0, column = 2, sticky = W,padx = 10)
	backButton.grid(row = 0, column = 3, sticky = W,padx = 10)


def main():
    screen1()
    root.mainloop()


if __name__ == "__main__":
    main()