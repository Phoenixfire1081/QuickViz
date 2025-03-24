# Supplement to Mayavi Visualization
# All movie related options are defined here

from traits.api import on_trait_change
import numpy as np
from mayavi import mlab
from PIL import Image
from pyface.api import GUI
import os
import tkinter
from tkinter import filedialog

class allSaveMovieOptions:

	@on_trait_change('save_timeSeries')
	def save_timeseries_button_fired(self):
		
		# Get initial time step
		current_time = int(self.startMovie)
		
		# Get final time
		if self.stopMovie == -1:
			total_time = int(np.shape(self._dataTs)[-1]-1)
		else:
			total_time = int(self.stopMovie)
		
		if not current_time == self.whichTime:
			self.whichTime = int(current_time)
		
		# Take screenshot and proceed to next frame
		for i in range(current_time, total_time):
			arr = mlab.screenshot(figure = self.scene.mayavi_scene, mode='rgba', antialiased=True)
			img = Image.fromarray(np.array(arr*255, dtype=np.uint8))
			img.save(self.save_path + '/img_'+ str(i-current_time).zfill(5) + '.png')
			self.next_timeseries_button_fired()
			GUI.process_events()
		
		# Use ffmpeg to combine into movie
		os.system('ffmpeg -y -framerate ' + str(int(self.framerate)) + ' -i ' + self.save_path + '/img_%05d.png -vf "format=yuv420p, pad=ceil(iw/2)*2:ceil(ih/2)*2" ' + self.save_path + '/video.mp4')
		
		if not self.save_images:
			# Remove all png files
			os.system('rm -rf img*.png')
	
	@on_trait_change('save_snapshot')
	def save_snapshot_button_fired(self):
		
		# Take screenshot 
		arr = mlab.screenshot(figure = self.scene.mayavi_scene, mode='rgba', antialiased=True)
		img = Image.fromarray(np.array(arr*255, dtype=np.uint8))
		img.save(self.save_path + '/snapshot.png')
	
	@on_trait_change('choose_folder')
	def choose_folder_button_fired(self):
		
		# Initialize tKinter
		root = tkinter.Tk()
		root.withdraw()
		
		currdir = os.getcwd()
		tkFolderPicker = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
		
		self.save_path = tkFolderPicker
