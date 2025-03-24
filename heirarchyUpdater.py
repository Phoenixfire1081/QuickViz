# Supplement to Mayavi Visualization
# Maintains heirarchy of data being read into the software

import os

class heirarchy:
	
	# Recognized data types - scalar, vector, scalarTS, vectorTS
	
	def __init__(self):
		
		# Check if heirarchy file exists
		print(os.path.isfile('heirarchy.txt'))
	
	# def update():
		
		
