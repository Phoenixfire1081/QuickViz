# Supplement to Mayavi Visualization
# All playback options are defined here

from traits.api import on_trait_change
import numpy as np
from pyface.api import GUI

class allPlaybackOptions:
	
	def get_current_time(self):
		if self.radioButton1:
			current_time = self.whichTime1
		elif self.radioButton2:
			current_time = self.whichTime2
		elif self.radioButton3:
			current_time = self.whichTime3
		elif self.radioButton4:
			current_time = self.whichTime4
		
		return current_time

	@on_trait_change('next_timeSeries')
	def next_timeseries_button_fired(self):
		
		if self.clamp: # For all ts
			
			current_time = self.get_current_time()
			
			if self.screen1_ts1:
				self.whichTime1 = current_time + 1
			if self.screen1_ts2:
				self.whichTime2 = current_time + 1
			if self.screen1_ts3:
				self.whichTime3 = current_time + 1
			if self.screen1_ts4:
				self.whichTime4 = current_time + 1
		
		else:
			
			# Get current time first
			current_time = self.whichTime1
			
			if self.whichTime1 < int(np.shape(self._dataTs1)[-1]-1):
				self.whichTime1 = current_time + 1
		
		# Update camera values
		# self.updateCurrentVals_button_fired()
		
	@on_trait_change('previous_timeSeries')
	def previous_timeseries_button_fired(self):
		
		if self.clamp: # For all ts
			
			current_time = self.get_current_time()
			
			if self.screen1_ts1:
				self.whichTime1 = current_time - 1
			if self.screen1_ts2:
				self.whichTime2 = current_time - 1
			if self.screen1_ts3:
				self.whichTime3 = current_time - 1
			if self.screen1_ts4:
				self.whichTime4 = current_time - 1
		
		else:
		
			# Get current time first
			current_time = self.whichTime1
			
			if self.whichTime1 > 0:
				self.whichTime1 = current_time - 1
		
		# Update camera values
		# self.updateCurrentVals_button_fired()	
	
	@on_trait_change('play_timeSeries')
	def play_timeseries_button_fired(self):
		
		# Get current time first
		current_time = self.whichTime1
		
		# Get total time
		total_time = int(np.shape(self._dataTs1)[-1]-1)
		
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
		current_time = self.whichTime1
		
		# Get total time
		total_time = int(np.shape(self._dataTs1)[-1]-1)
		
		# Fire previous time series button
		for i in range(current_time):
			
			if i == 0:
				
				self.stopPlayback = 0
			
			if not self.stopPlayback:
			
				self.previous_timeseries_button_fired()
				GUI.process_events()
