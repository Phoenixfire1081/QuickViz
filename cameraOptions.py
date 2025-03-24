# Supplement to Mayavi Visualization
# All camera options are defined here

from traits.api import on_trait_change
import numpy as np
from mayavi import mlab
import os

class allCameraOptions:

	@on_trait_change('updateCurrentVals')
	def updateCurrentVals_button_fired(self):
		
		# Get current cam values and update
		self.camAzimuthG, self.camElevationG, self.camDistanceG, fp = mlab.view()	
		self.focalPointG1, self.focalPointG2, self.focalPointG3 = fp
		self.camRollG = mlab.roll()
		
		# Update setting options too
		self.camAzimuthS = np.float32(self.camAzimuthG)
		self.camElevationS = np.float32(self.camElevationG)
		self.camDistanceS = np.float32(self.camDistanceG)
		self.focalPointS1 = np.float32(self.focalPointG1)
		self.focalPointS2 = np.float32(self.focalPointG2)
		self.focalPointS3 = np.float32(self.focalPointG3)
		self.camRollS = np.float32(self.camRollG)
	
	@on_trait_change('saveCam1')
	def saveCam1_fired(self):
		
		# Save and load camera state
		
		if os.path.isfile('cam1.txt'):
			
			camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = np.loadtxt('cam1.txt')
			
			mlab.view(camAzimuth, camElevation, camDistance, [fp1, fp2, fp3])
			mlab.roll(camRoll)
		
		else:
		
	        # Get current cam values first
			camAzimuth, camElevation, camDistance, fp = mlab.view()	
			fp1, fp2, fp3 = fp
			camRoll = mlab.roll()
	        
			fw = open('cam1.txt', 'w+')
			fw.write(str(np.float32(camAzimuth)) + ' ' + \
					str(np.float32(camElevation)) + ' ' + \
					str(np.float32(camDistance)) + ' ' + \
					str(np.float32(fp1)) + ' ' + \
					str(np.float32(fp2)) + ' ' + \
					str(np.float32(fp3)) + ' ' + \
					str(np.float32(camRoll)) + ' ' 
					)
			
			fw.close()
		
		# Update camera values
		self.updateCurrentVals_button_fired()
	
	@on_trait_change('saveCam2')
	def saveCam2_fired(self):
		
		# Save and load camera state
		
		if os.path.isfile('cam2.txt'):
			
			camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = np.loadtxt('cam2.txt')
			
			mlab.view(camAzimuth, camElevation, camDistance, [fp1, fp2, fp3])
			mlab.roll(camRoll)
		
		else:
		
	        # Get current cam values first
			camAzimuth, camElevation, camDistance, fp = mlab.view()	
			fp1, fp2, fp3 = fp
			camRoll = mlab.roll()
	        
			fw = open('cam2.txt', 'w+')
			fw.write(str(np.float32(camAzimuth)) + ' ' + \
					str(np.float32(camElevation)) + ' ' + \
					str(np.float32(camDistance)) + ' ' + \
					str(np.float32(fp1)) + ' ' + \
					str(np.float32(fp2)) + ' ' + \
					str(np.float32(fp3)) + ' ' + \
					str(np.float32(camRoll)) + ' ' 
					)
			
			fw.close()
		
		# Update camera values
		self.updateCurrentVals_button_fired()
	
	@on_trait_change('saveCam3')
	def saveCam3_fired(self):
		
		# Save and load camera state
		
		if os.path.isfile('cam3.txt'):
			
			camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = np.loadtxt('cam3.txt')
			
			mlab.view(camAzimuth, camElevation, camDistance, [fp1, fp2, fp3])
			mlab.roll(camRoll)
		
		else:
		
	        # Get current cam values first
			camAzimuth, camElevation, camDistance, fp = mlab.view()	
			fp1, fp2, fp3 = fp
			camRoll = mlab.roll()
	        
			fw = open('cam3.txt', 'w+')
			fw.write(str(np.float32(camAzimuth)) + ' ' + \
					str(np.float32(camElevation)) + ' ' + \
					str(np.float32(camDistance)) + ' ' + \
					str(np.float32(fp1)) + ' ' + \
					str(np.float32(fp2)) + ' ' + \
					str(np.float32(fp3)) + ' ' + \
					str(np.float32(camRoll)) + ' ' 
					)
			
			fw.close()
		
		# Update camera values
		self.updateCurrentVals_button_fired()
	
	@on_trait_change('saveCam4')
	def saveCam4_fired(self):
		
		# Save and load camera state
		
		if os.path.isfile('cam4.txt'):
			
			camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = np.loadtxt('cam4.txt')
			
			mlab.view(camAzimuth, camElevation, camDistance, [fp1, fp2, fp3])
			mlab.roll(camRoll)
		
		else:
		
	        # Get current cam values first
			camAzimuth, camElevation, camDistance, fp = mlab.view()	
			fp1, fp2, fp3 = fp
			camRoll = mlab.roll()
	        
			fw = open('cam4.txt', 'w+')
			fw.write(str(np.float32(camAzimuth)) + ' ' + \
					str(np.float32(camElevation)) + ' ' + \
					str(np.float32(camDistance)) + ' ' + \
					str(np.float32(fp1)) + ' ' + \
					str(np.float32(fp2)) + ' ' + \
					str(np.float32(fp3)) + ' ' + \
					str(np.float32(camRoll)) + ' ' 
					)
			
			fw.close()
		
		# Update camera values
		self.updateCurrentVals_button_fired()
	
	@on_trait_change('saveCam5')
	def saveCam5_fired(self):
		
		# Save and load camera state
		
		if os.path.isfile('cam5.txt'):
			
			camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = np.loadtxt('cam5.txt')
			
			mlab.view(camAzimuth, camElevation, camDistance, [fp1, fp2, fp3])
			mlab.roll(camRoll)
		
		else:
		
	        # Get current cam values first
			camAzimuth, camElevation, camDistance, fp = mlab.view()	
			fp1, fp2, fp3 = fp
			camRoll = mlab.roll()
	        
			fw = open('cam5.txt', 'w+')
			fw.write(str(np.float32(camAzimuth)) + ' ' + \
					str(np.float32(camElevation)) + ' ' + \
					str(np.float32(camDistance)) + ' ' + \
					str(np.float32(fp1)) + ' ' + \
					str(np.float32(fp2)) + ' ' + \
					str(np.float32(fp3)) + ' ' + \
					str(np.float32(camRoll)) + ' ' 
					)
			
			fw.close()
		
		# Update camera values
		self.updateCurrentVals_button_fired()
		
	@on_trait_change('camReset')
	def camReset_fired(self):
		
		# Remove all camera orientation files
		os.system('rm -rf cam1.txt cam2.txt cam3.txt cam4.txt cam5.txt')
		
	@on_trait_change('camAzimuthS, camElevationS, camDistanceS, \
	focalPointS1, focalPointS2, focalPointS3, camRollS')
	def cam_angle_changed(self):
		
		# Update camera view
		mlab.view(self.camAzimuthS, self.camElevationS, self.camDistanceS, [self.focalPointS1, self.focalPointS2, self.focalPointS3])
		mlab.roll(self.camRollS)
