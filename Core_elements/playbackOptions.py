# Supplement to Mayavi Visualization
# All playback options are defined here

from traits.api import on_trait_change
import numpy as np
from pyface.api import GUI

class allPlaybackOptions:
	
	def get_current_time(self):
		if self.radioButton1 == 'Y':
			current_time = self.whichTime1
		elif self.radioButton2 == 'Y':
			current_time = self.whichTime2
		elif self.radioButton3 == 'Y':
			current_time = self.whichTime3
		elif self.radioButton4 == 'Y':
			current_time = self.whichTime4
		
		return current_time
	
	def get_total_time(self):
		if self.radioButton1 == 'Y':
			total_time = int(np.shape(self._dataTs1)[-1]-1)
		elif self.radioButton2 == 'Y':
			total_time = int(np.shape(self._dataTs2)[-1]-1)
		elif self.radioButton3 == 'Y':
			total_time = int(np.shape(self._dataTs3)[-1]-1)
		elif self.radioButton4 == 'Y':
			total_time = int(np.shape(self._dataTs4)[-1]-1)
		return total_time
	
	def update_time(self, increase):
		
		current_time = self.get_current_time()
		
		if increase: 
			update = 1 
		else: 
			update = -1
		
		if self.radioButton1 == 'Y' and not self.clamp:
			if self.whichTime1 <= int(np.shape(self._dataTs1)[-1]-1):
				self.whichTime1 = current_time + update
		
		if self.radioButton2 == 'Y' and not self.clamp:
			if self.whichTime2 <= int(np.shape(self._dataTs2)[-1]-1):
				self.whichTime2 = current_time + update
		
		if self.radioButton3 == 'Y' and not self.clamp:
			if self.whichTime3 <= int(np.shape(self._dataTs3)[-1]-1):
				self.whichTime3 = current_time + update
		
		if self.radioButton4 == 'Y' and not self.clamp:
			if self.whichTime4 <= int(np.shape(self._dataTs4)[-1]-1):
				self.whichTime4 = current_time + update
		
		if self.clamp:
			if self.whichTimeGlobal <= int(np.shape(self._dataTs1)[-1]-1):
				self.whichTimeGlobal = current_time + update
		

	@on_trait_change('next_timeSeries')
	def next_timeseries_button_fired(self):
		
		self.update_time(True)
		
	@on_trait_change('previous_timeSeries')
	def previous_timeseries_button_fired(self):
		
		self.update_time(False)
	
	@on_trait_change('play_timeSeries')
	def play_timeseries_button_fired(self):
		
		# Get current time first
		current_time = self.get_current_time()
		
		# Get total time
		total_time = self.get_total_time()
		
		# Fire next time series button
		for i in range(current_time, total_time):
			
			if i == current_time:
				
				self.stopPlayback = 0
			
			if not self.stopPlayback:
			
				self.next_timeseries_button_fired()
				GUI.process_events()
	
	@on_trait_change('stop_timeSeries')
	def stop_timeseries_button_fired(self):
		
		# Stop playback
		self.stopPlayback = 1
	
	@on_trait_change('play_timeSeries_reverse')
	def play_timeseries_reverse_button_fired(self):
		
		# Get current time first
		current_time = self.get_current_time()
		
		# Get total time
		total_time = self.get_total_time()
		
		# Fire previous time series button
		for i in range(current_time):
			
			if i == 0:
				
				self.stopPlayback = 0
			
			if not self.stopPlayback:
			
				self.previous_timeseries_button_fired()
				GUI.process_events()
