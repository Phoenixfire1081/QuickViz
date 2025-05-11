# Supplement to Mayavi Visualization
# Creates a file select dialog with tkinter

from traits.api import on_trait_change
import numpy as np
import os
import tkinter
from tkinter import filedialog
import array
from .heirarchyUpdater import heirarchy

class fileChooserClass:

	@on_trait_change('select_files')
	def select_files_toggled(self):
		
		# Initialize tKinter
		root = tkinter.Tk()
		root.withdraw()
		
		currdir = os.getcwd()
		tkFilePicker = filedialog.askopenfilenames(parent=root, initialdir=currdir, title='Please select a directory')
		
		if len(tkFilePicker) == 1: # One object only - can be scalar or vector 
			
			print ("Data path:", tkFilePicker[0])
			print ("Data length in all directions:", self.xlength, self.ylength, self.zlength)
			print ("Data bbox:", self.bbxmin, self.bbxmax, self.bbymin, self.bbymax, self.bbzmin, self.bbzmax)
			print ("Data order:", self.arrayOrder)
			print ("Data Precision:", self.dataPrecision)
			print ("Number of components:", self.numComponents)
			
			# Read in dataset and update heirarchy
			
			if self.dataPrecision == 'float':
			
				tmp_ = array.array('f')
			
			elif self.dataPrecision == 'double':
				
				tmp_ = array.array('d')
			
			tmp_.fromfile(open(tkFilePicker[0], 'rb'), (self.xlength * self.ylength * self.zlength * int(self.numComponents)))
			
			if self.numComponents == '1': # scalar data
			
				if self.arrayOrder == 'x fastest':
				
					tmp_ = np.reshape(tmp_, [self.xlength, self.ylength, self.zlength], order = 'F')
				
				elif self.arrayOrder == 'z fastest':
					
					tmp_ = np.reshape(tmp_, [self.xlength, self.ylength, self.zlength])
				
				setInputDataType = 'scalar'
			
			else:
				
				if self.arrayOrder == 'x fastest':
				
					tmp_ = np.reshape(tmp_, [self.xlength, self.ylength, self.zlength, int(self.numComponents)], order = 'F')
				
				elif self.arrayOrder == 'z fastest':
					
					tmp_ = np.reshape(tmp_, [self.xlength, self.ylength, self.zlength, int(self.numComponents)])
				
				setInputDataType = 'vector'
				
			print("Read data into memory..")
			heirarchy.__init__
			
