from math import *
import random
import time
import matplotlib.pyplot as plt

# Randomly generate set of points
def get_points(number_points = 10):
	range_min = 50
	range_max = 300
	points = []
	for _ in range(NUM_POINTS):
	    x, y = random.randint(range_min, range_max), random.randint(range_min, range_max)
	    points.append((x,y))
	return points

# is a point on the left of a line?
def is_point_on_left(start_pos_line, end_pos_line, point):
	ax, ay, bx, by, px, py = start_pos_line[0], start_pos_line[1], end_pos_line[0], end_pos_line[1], point[0], point[1]
	
	z = ((bx - ax) * (py - ay)) - ((px - ax) * (by - ay))
	if z > 0:
		return True
	return False
	
# calculate the distance between a point and a line.
def get_distance_to_line(a, b, p):
	ax, ay, bx, by = a[0], a[1], b[0], b[1]
	px, py = p[0], p[1]
	d = (abs(((bx - ax) * (ay - py)) - ((ax - px) * (by - ay)))) / sqrt((pow((bx - ax), 2)) + (pow((by - ay), 2)))
	return d

# find furthest point in S = points from the line a-b
def get_max_p_from_line(a, b, points):
	max_d_p = None
	max_distance = 0.0
	for p in points:
		if get_distance_to_line(a, b, p) >= max_distance:
			max_d_p = p
			max_distance = get_distance_to_line(a, b, p) #Note: This was the bug with the code we used in class. I forgot to update the current max distance.
	return max_d_p

# get all subset of S that lies on the left of the line (a,b)
def get_left_S(a, b, S):
	S1 = []
	for point in S:
		if is_point_on_left(a, b, point):
			S1.append(point)
	return S1

# method that can be used to collect points found in the upper and lower hull. points are collected into collected_hull_points
def findHull(a, b, points, collected_hull_points):
	if len(points) > 0:
		#get upper part of current S -- where to find the point that is furthest from the line
		S_updated = get_left_S(a, b, points)
		
		#the point with max. distance
		max_d_p = get_max_p_from_line(a, b, S_updated)
		collected_hull_points.append(max_d_p)
				
		#split points for line (a, max_d_p)
		findHull(a, max_d_p, S_updated, collected_hull_points)
		
		#split points for line (max_d_p, b)
		findHull(max_d_p, b, S_updated, collected_hull_points)
		
	return collected_hull_points
		
		

def quickhull(S):
	hull = []
	
	p_min = min(S)
	p_max = max(S)
	
	hull += [p_min, p_max]
	
	other_hull_points = []
	
	S1 = get_left_S(p_min, p_max, S)
	findHull(p_min, p_max, S1, other_hull_points)
	
	S2 = get_left_S(p_max, p_min, S)
	findHull(p_max, p_min, S2, other_hull_points)

	hull_points = hull + other_hull_points
		
	return hull_points
	

if __name__ == '__main__':
	NUM_POINTS = 10
	
	points = get_points()
	
	hull_points = quickhull(points)
	non_hull_points = [point for point in points if not point in hull_points]
	
	#create scatter plot
	x1 = []
	y1 = []
	for point in non_hull_points:
		x1.append(point[0])
		y1.append(point[1])
		
	x2 = []
	y2 = []
	for point in hull_points:
		if point:
			x2.append(point[0])
			y2.append(point[1])
	
	
	plt.scatter(x1, y1, c='b')
	plt.scatter(x2, y2, c='r')
	plt.show()
