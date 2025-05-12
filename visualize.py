import numpy as np
import os
from mayaviVisualization import mayaviVisualizeTimeSeries#, mayaviVisualizeTimeSeries2
import netCDF4 as nc
from vortexExtraction import vortexExtract
import array

#---------------------------------------------------------------------#

# -----------------------------SPHYNX/CEA---------------------------- #

# Author: Abhishek Harikrishnan
# Email: abhishek.paraswararharikrishnan@cea.fr
# Last updated: 16-05-2024

# Code to visualize the various FlowFit runs
# Following parameters need to be specified
# -> case
# -> run
# -> min, max time instance 
# -> min, max data for x, y, z coordinates to trim the data
# -> data precision
# -> scalar type (Look into vortex extraction to see what all are supported)

# For now, it works with GVK - JUIN 2021. Others need to be tested.

#---------------------------------------------------------------------#

# Choose case and run

# Available runs:
# CASE: 0.004Hz_anti_water
# 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 21, 33, 34, 35, 37, 38, 39, 40

# CASE: 0.1Hz_anti_water
# 01 - 40

# Reprocessed runs (to eliminate minor issues with flowfit) are kept at
# Reprocessed_runs folder. For now, reprocessing is done only for run34
# of 0.004Hz_anti_water and is kept in the folder Reprocessed_runs/run34_new

#---------------------------------------------------------------------#
# 					SET THE FOLLOWING PARAMETERS
#---------------------------------------------------------------------#

getDataAutomatically = True

xlen = 256
ylen = 256
zlen = 256

xlen2 = 64
ylen2 = xlen
zlen2 = xlen

xmin2 = -0.5
xmax2 = 0.5
ymin2 = -0.5
ymax2 = 0.5
zmin2 = -0.5
zmax2 = 0.5

xmin = -0.5
xmax = 0.5
ymin = -0.5
ymax = 0.5
zmin = -0.5
zmax = 0.5

_dtype = 'f' # 'd' for double precision

minTs = 0
maxTs = 10
# maxTs = 1

# vortMag - vorticity magnitude
# velMag - velocity magnitude
# Q - Q-criterion
# deltaCrit - Delta Criterion
# l2 - lambda 2 criterion
# ensDensity - enstrophy density
# ensProd - enstrophy production rate
# temp - temperature

whichScalars = ['Q']

# NOTE: -1 specifies the end of array
# For now, visualizing two scalars at the same time are supported

# Supported color fields - vel, vort, temp
colorFields = False
whichColorFields = ['vort']

#---------------------------------------------------------------------#

# Get all data files and sort them by time instance

path2 = 'KidaSetup_Re1e+04_full/'
# path = 'KidaSetup_Re1e+04_Full/'
path = 'KidaSetup_Re1e+04_zoom/'
# path = 'KidaSetupLowerSpacing_Re1e+04/'

allFilesx = os.listdir(path + 'velComp/')
allFilesx = [i for i in allFilesx if 'x' in i]
if len(allFilesx) > 1:
	allFilesx.sort(key = lambda x: int(x.split('_')[1].split('.')[0]))

allFilesy = os.listdir(path + 'velComp/')
allFilesy = [i for i in allFilesy if 'y' in i]
if len(allFilesy) > 1:
	allFilesy.sort(key = lambda x: int(x.split('_')[1].split('.')[0]))

allFilesz = os.listdir(path + 'velComp/')
allFilesz = [i for i in allFilesz if 'z' in i]
if len(allFilesz) > 1:
	allFilesz.sort(key = lambda x: int(x.split('_')[1].split('.')[0]))

allFilesVortMag = os.listdir(path + 'vortMag/')
if len(allFilesVortMag) > 1:
	allFilesVortMag.sort(key = lambda x: int(x.split('_')[1].split('.')[0]))
	
if 'temp' in whichScalars or 'temp' in whichColorFields:
	allFilesTemp = os.listdir(path + 'sc/')
	if len(allFilesTemp) > 1:
		allFilesTemp.sort(key = lambda x: int(x.split('_')[1].split('.')[0]))

if len(whichScalars) > 1:
	allFilesVortMag2 = os.listdir(path2 + 'vortMag/')
	if len(allFilesVortMag2) > 1:
		allFilesVortMag2.sort(key = lambda x: int(x.split('_')[1].split('.')[0]))
	
	if len(allFilesVortMag) < len(allFilesVortMag2):
		maxTs = len(allFilesVortMag)
	else:
		maxTs = len(allFilesVortMag2)

else:
	maxTs = len(allFilesVortMag)

if getDataAutomatically:
	
	print('Getting data automatically...')
	
	if path:
		print(path)
		xmin, xmax, ymin, ymax, zmin, zmax = np.loadtxt(path + 'howToRead.txt', skiprows = 2, max_rows=1, dtype = float)
		print(xmin, xmax, ymin, ymax, zmin, zmax)
		xlen, ylen, zlen = np.loadtxt(path + 'howToRead.txt', skiprows = 5, max_rows=1, dtype = int)
		print(xlen, ylen, zlen)
	if path2:
		print(path2)
		xmin2, xmax2, ymin2, ymax2, zmin2, zmax2 = np.loadtxt(path2 + 'howToRead.txt', skiprows = 2, max_rows=1, dtype = float)
		print(xmin2, xmax2, ymin2, ymax2, zmin2, zmax2)
		xlen2, ylen2, zlen2 = np.loadtxt(path + 'howToRead.txt', skiprows = 5, max_rows=1, dtype = int)
		print(xlen2, ylen2, zlen2)
	

# Get grid data and trim
x = np.linspace(xmin, xmax, xlen)
y = np.linspace(ymin, ymax, ylen)
z = np.linspace(zmin, zmax, zlen)

xx, yy, zz = np.meshgrid(x, y, z, indexing = 'ij')

dx = np.diff(x)[0]
dy = np.diff(y)[0]
dz = np.diff(z)[0]

x2 = np.linspace(xmin2, xmax2, xlen2)
y2 = np.linspace(ymin2, ymax2, ylen2)
z2 = np.linspace(zmin2, zmax2, zlen2)

xx2, yy2, zz2 = np.meshgrid(x2, y2, z2, indexing = 'ij')

dx2 = np.diff(x2)[0]
dy2 = np.diff(y2)[0]
dz2 = np.diff(z2)[0]

sCounter = 1

maxTs = 10

for whichScalar in whichScalars:
	
	if sCounter > 1:
		path = path2
	
	print('Reading data from:', path)

	# Loop and add scalar fields to a large 4d scalar field
	for i in range(minTs, maxTs):
		
		if not whichScalar == 'vortMag':
		
			print('Processing:', allFilesx[i])
			
			u = array.array('f')
			u.fromfile(open(path + 'velComp/' + allFilesx[i], 'rb'), (xlen * ylen * zlen))
			u = np.reshape(u, [xlen, ylen, zlen])
			
			v = array.array('f')
			v.fromfile(open(path + 'velComp/' + allFilesy[i], 'rb'), (xlen * ylen * zlen))
			v = np.reshape(v, [xlen, ylen, zlen])
			
			w = array.array('f')
			w.fromfile(open(path + 'velComp/' + allFilesz[i], 'rb'), (xlen * ylen * zlen))
			w = np.reshape(w, [xlen, ylen, zlen])
			
			vortices = vortexExtract(u, v, w, dx, dy, dz)
			
			if whichScalar == 'velMag':
				scalar = vortices.velocityMagnitude()
			elif whichScalar == 'vortMag':
				scalar = vortices.vorticityMagnitude()
			elif whichScalar == 'Q':
				scalar = vortices.qCriterion()
			elif whichScalar == 'deltaCrit':
				scalar = vortices.deltaCriterion()
			elif whichScalar == 'l2':
				scalar = vortices.lambda2Criterion()
			elif whichScalar == 'ensDensity':
				scalar = vortices.enstrophyDensity()
			elif whichScalar == 'ensProd':
				scalar = vortices.enstrophyProductionRate()
			elif whichScalar == 'temp':
				scalar = array.array('f')
				scalar.fromfile(open(path + 'sc/' + allFilesTemp[i], 'rb'), (xlen * ylen * zlen))
				scalar = np.reshape(scalar, [xlen, ylen, zlen])
			else:
				print('Not implemented..')
				raise NotImplementedError
				
			# if colorFields and 'vort' in whichColorFields:
			w1, w2, w3 = vortices.vorticityComponents()
			if colorFields and 'temp' in whichColorFields:
				temp = array.array('f')
				temp.fromfile(open(path + 'sc/' + allFilesTemp[i], 'rb'), (xlen * ylen * zlen))
				temp = np.reshape(temp, [xlen, ylen, zlen])
		
		else:
		
			scalar = array.array('f')
			scalar.fromfile(open(path + 'vortMag/' + allFilesVortMag[i], 'rb'), (xlen * ylen * zlen))
			scalar = np.reshape(scalar, [xlen, ylen, zlen])
			
			if colorFields and 'vort' in whichColorFields:
				w1, w2, w3 = vortices.vorticityComponents()
			if colorFields and 'temp' in whichColorFields:
				temp = array.array('f')
				temp.fromfile(open(path + 'sc/' + allFilesTemp[i], 'rb'), (xlen * ylen * zlen))
				temp = np.reshape(temp, [xlen, ylen, zlen])
			
		if i == minTs:
			
			# Create 4D scalar field with time as the last dimension
			# xlen, ylen, zlen corresponds to the size of the 3D scalar field
			
			if sCounter == 1:
				timeSeries1 = np.zeros((xlen, ylen, zlen, maxTs-minTs), dtype = _dtype)
				timeSeries1_vel = np.zeros((xlen, ylen, zlen, maxTs-minTs, 3), dtype = _dtype)
				timeSeries1_vort = np.zeros((xlen, ylen, zlen, maxTs-minTs, 3), dtype = _dtype)
			if sCounter == 2:
				timeSeries2 = np.zeros((xlen2, ylen2, zlen2, maxTs-minTs), dtype = _dtype)
			if colorFields and sCounter == 1:
				timeSeriesCF = np.zeros((xlen, ylen, zlen, maxTs-minTs, 4), dtype = _dtype)
		
		if sCounter == 1:
			timeSeries1[:, :, :, i-minTs] += scalar
			timeSeries1_vel[:, :, :, i-minTs, 0] += u
			timeSeries1_vel[:, :, :, i-minTs, 1] += v
			timeSeries1_vel[:, :, :, i-minTs, 2] += w
			timeSeries1_vort[:, :, :, i-minTs, 0] += w1
			timeSeries1_vort[:, :, :, i-minTs, 1] += w2
			timeSeries1_vort[:, :, :, i-minTs, 2] += w3
		if sCounter == 2:
			timeSeries2[:, :, :, i-minTs] += scalar
		if colorFields and 'vort' in whichColorFields and sCounter == 1:
			timeSeriesCF[:, :, :, i-minTs, 0] += w1
			timeSeriesCF[:, :, :, i-minTs, 1] += w2
			timeSeriesCF[:, :, :, i-minTs, 2] += w3
			timeSeriesCF[:, :, :, i-minTs, 3] += np.sqrt(w1**2 + w2**2 + w3**2)
		if colorFields and 'vel' in whichColorFields and sCounter == 1:
			timeSeriesCF[:, :, :, i-minTs, 0] += u
			timeSeriesCF[:, :, :, i-minTs, 1] += v
			timeSeriesCF[:, :, :, i-minTs, 2] += w
			timeSeriesCF[:, :, :, i-minTs, 3] += np.sqrt(u**2 + v**2 + w**2)
		if colorFields and 'temp' in whichColorFields and sCounter == 1:
			timeSeriesCF[:, :, :, i-minTs, 0] += temp
		
	sCounter += 1

	

xx, yy, zz = np.mgrid[x[0]:x[-1]:len(x)*1j, y[0]:y[-1]:len(y)*1j, z[0]:z[-1]:len(z)*1j]
xx2, yy2, zz2 = np.mgrid[x2[0]:x2[-1]:len(x2)*1j, y2[0]:y2[-1]:len(y2)*1j, z2[0]:z2[-1]:len(z2)*1j]

# from mayavi import mlab

# sf = mlab.pipeline.scalar_field(timeSeries1[:, :, :, 0])
# contour_data = mlab.pipeline.contour(sf)
# contour_data.filter.contours = [1000]
# cf0 = contour_data.outputs[0]
# actualPts = cf0.output.points.to_array()
# # print(actualPts)
# actualTriangles = cf0.output.polys.to_array() 
# actualTriangles = actualTriangles.reshape(actualTriangles.size//4, 4)

# # print(actualPts)

# # Use both information above to get all vertices of the triangles
# x1, y1, z1 = actualPts[actualTriangles[:, 1]].T
# x2, y2, z2 = actualPts[actualTriangles[:, 2]].T
# x3, y3, z3 = actualPts[actualTriangles[:, 3]].T

# # Interpolate on the points to get the scalar data

# import scipy.interpolate
# xx, yy, zz = np.meshgrid(np.linspace(0, len(x)-1, len(x)), np.linspace(0, len(x)-1, len(x)), np.linspace(0, len(x)-1, len(x)), indexing = 'ij')
# interp0 = scipy.interpolate.NearestNDInterpolator((xx.ravel(), yy.ravel(), zz.ravel()), timeSeriesCF[:, :, :, 1, 0].ravel())

# mesh = mlab.triangular_mesh(actualPts[:, 0], actualPts[:, 1], actualPts[:, 2], actualTriangles[:, 1:], scalars = interp0(actualPts))
# # point_data = mesh.mlab_source.dataset.point_data
# # point_data.scalars = timeSeriesCF[:, :, :, 0, 0].ravel()
# # mesh.module_manager.scalar_lut_manager.data_range = [ -0.1,  0.1]
# raise SystemError

if len(whichScalars) == 1 and colorFields:
	visObject = mayaviVisualizeTimeSeries(xx, yy, zz, timeSeriesCF, whichColorFields[0], timeSeries1)
elif len(whichScalars) == 1 and not colorFields:
	#visObject = mayaviVisualizeTimeSeries(xx, yy, zz, timeSeries1)
	visObject = mayaviVisualizeTimeSeries(1, xx, yy, zz, timeSeries1, timeSeries1_vel, timeSeries1_vort)
if len(whichScalars) == 2 and colorFields:
	visObject = mayaviVisualizeTimeSeries2(xx, yy, zz, xx2, yy2, zz2, timeSeriesCF, whichColorFields[0], timeSeries1, timeSeries2)
elif len(whichScalars) == 2 and not colorFields:
	visObject = mayaviVisualizeTimeSeries2(xx, yy, zz, xx2, yy2, zz2, timeSeries1, timeSeries2)
visObject.configure_traits()
