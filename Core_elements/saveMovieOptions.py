# Supplement to Mayavi Visualization
# All movie related options are defined here

from traits.api import on_trait_change
import numpy as np
from mayavi import mlab
from PIL import Image
from pyface.api import GUI
from .tKinter import folderBrowser
import os

class allSaveMovieOptions:

	@on_trait_change('save_timeSeries')
	def save_timeseries_button_fired(self):
		
		# Get initial time step
		current_time = int(self.startMovie)
		
		# Get final time
		if self.stopMovie == -1:
			total_time = int(np.shape(self._dataTs1)[-1]-1)
		else:
			total_time = int(self.stopMovie)
		
		if not current_time == self.whichTime1:
			self.whichTime1 = int(current_time)
		
		# Take screenshot and proceed to next frame
		for i in range(current_time, total_time):
			self.save_snapshot_button_fired()
			os.system('mv snapshot.png ' + self.save_path + '/img_'+ str(i-current_time).zfill(5) + '.png')
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
		# For multiple windows, combine images
		nactive = 0
		activeImages = []
		if self.screen1_ts1:
			arr1 = mlab.screenshot(figure = self.scene1.mayavi_scene, mode='rgba', antialiased=True)
			img = Image.fromarray(np.array(arr1*255, dtype=np.uint8))
			img.save(self.save_path + '/tmp_sc1.png')
			nactive += 1
			activeImages.append('tmp_sc1.png')
			
		if self.screen2_ts1:
			arr2 = mlab.screenshot(figure = self.scene2.mayavi_scene, mode='rgba', antialiased=True)
			img = Image.fromarray(np.array(arr2*255, dtype=np.uint8))
			img.save(self.save_path + '/tmp_sc2.png')
			nactive += 1
			activeImages.append('tmp_sc2.png')
			
		if self.screen3_ts1:
			arr3 = mlab.screenshot(figure = self.scene3.mayavi_scene, mode='rgba', antialiased=True)
			img = Image.fromarray(np.array(arr3*255, dtype=np.uint8))
			img.save(self.save_path + '/tmp_sc3.png')
			nactive += 1
			activeImages.append('tmp_sc3.png')
			
		if self.screen4_ts1:
			arr4 = mlab.screenshot(figure = self.scene4.mayavi_scene, mode='rgba', antialiased=True)
			img = Image.fromarray(np.array(arr4*255, dtype=np.uint8))
			img.save(self.save_path + '/tmp_sc4.png')
			nactive += 1
			activeImages.append('tmp_sc4.png')
		
		if nactive == 1:
			os.system('mv tmp_sc*.png snapshot.png')
		
		if nactive == 2: # If two exist, append horizontally in ascending order
			os.system('magick ' + activeImages[0] + ' ' + activeImages[1] + ' +append snapshot.png')
			
		if nactive == 3: # If three exist, append first two horizontally and third vertically
			os.system('magick ' + activeImages[0] + ' ' + activeImages[1] + ' +append tmp_sc9.png')
			os.system('magick tmp_sc9.png ' + activeImages[2] + ' -append snapshot.png')
		
		if nactive == 4: # If four exist, append first two horizontally, next two horizontally and finally all vertically
			os.system('magick ' + activeImages[0] + ' ' + activeImages[1] + ' +append tmp_sc8.png')
			os.system('magick ' + activeImages[2] + ' ' + activeImages[3] + ' +append tmp_sc9.png')
			os.system('magick tmp_sc8.png tmp_sc9.png -append snapshot.png')
		
		# Clean up temporary images	
		os.system('rm -rf tmp_sc*.png')
	
	@on_trait_change('choose_folder')
	def choose_folder_button_fired(self):
		
		self.save_path = folderBrowser()
