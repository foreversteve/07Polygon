import math
from display import *



#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
	norm = math.pow(math.pow(vector[0],2)+math.pow(vector[1],2)+math.pow(vector[2],2),0.5)
	for i in range(len(vector)-1):
		vector[i] = vector[i] / norm

#Return the dot porduct of a . b
def dot_product(a, b):
	s = 0
	for i in range(len(a)-1):
		s += a[i] * b[i]
	return s

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
	p0 = polygons[i]
	p1 = polygons[i+1]
	p2 = polygons[i+2]

	x0 = p1[0] - p0[0]
	y0 = p1[1] - p0[1]
	z0 = p1[2] - p0[2]
	x1 = p2[0] - p1[0]
	y1 = p2[1] - p1[1]
	z1 = p2[2] - p1[2]
	return [y0*z1-y1*z0,z0*x1-x0*z1,x0*y1-x1*y0,1]

