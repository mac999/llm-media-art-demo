from p5 import *
import pandas as pd

# Load the dataset
data = pd.read_csv('input.csv')

def setup():
	size(720, 400)
	no_stroke()
	camera(0, 0, 1500, 0, 0, 0, 0, 1, 0)

def draw_cone(size_x, size_y, position):
	with push_matrix():
		translate(*position)
		cone(size_x, size_y)

def draw():
	background(0, 150, 150)
	lights()
	rotate_x(0.3) # frame_count * 0.01)
	rotate_y(frame_count * 0.01)
	blinn_phong_material()

	interval = 200
	for i, row in data.iterrows():
		x = (i % 6) * interval - interval
		y = 0
		z = (i // 6) * interval - interval
		draw_cone(row['energy'], row['temperature'], (x, y, z))

	locX = mouse_x - width/2
	locY = mouse_y - height/2
	light_specular(0, 0, 255)
	point_light(360, 360*1.5, 360, locX, locY, 400)

if __name__ == '__main__':
	run(mode='P3D')