from p5 import *
import pandas as pd, numpy as np

# Load the dataset
data = pd.read_csv('input.csv')

def setup():
	size(720, 400)
	# no_stroke()
	camera(width, height, 1500, width, -height, 0, 0, 1, 0)

def draw_cone(size_x, size_y, position):
	with push_matrix():
		translate(*position)
		cone(size_x, size_y)

def draw_cube(energy, temperature, position): # energy in 50 to 100, temperature in 10 to 40
	energe_level = np.interp(energy, [50, 80], [0, 100]) 
	temperature_color = np.interp(temperature, [20, 25], [0, 255])

	r = np.interp(temperature, [10, 40], [255, 0])
	g = np.interp(temperature, [10, 40], [0, 255])
	b = 0
	fill(r, g, b, 127)
	
	with push_matrix():
		translate(*position)
		box(160, 100 * energe_level / 100, 160)

def draw():
	background(0, 0, 0)

	locX = mouse_x - width/2
	locY = mouse_y - height/2
	if mouse_is_pressed:
		rotate_x(-0.01 * locY)
		rotate_y(0.01 * locX)
	else:
		rotate_x(0.3) # frame_count * 0.01)
		rotate_y(frame_count * 0.01)

	# lights()
	# blinn_phong_material()

	interval = 200
	for i, row in data.iterrows():
		x = (i % 6) * interval - interval
		y = 0
		z = (i // 6) * interval - interval
		draw_cube(row['energy'], row['temperature'], (x, y, z))

	# light_specular(255, 0, 0)
	# point_light(360, 360*1.5, 360, locX, locY, 400)

if __name__ == '__main__':
	run(mode='P3D')