import os
import tkinter
from tkinter import filedialog
	
def folderBrowser():
	
	# Initialize tKinter
	root = tkinter.Tk()
	root.withdraw()
	
	currdir = os.getcwd()
	tkFolderPicker = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
	
	if tkFolderPicker == ():
		return currdir
	else:
		return tkFolderPicker
