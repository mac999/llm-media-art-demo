# Code from Daniel Shiffman's tutorial, adopted to p5py
# https://processing.org/tutorials/p3d/

from p5 import *

def setup():
	size(640, 360)

def draw():
	background(0)
	lights()

	with push_matrix():
		translate(-130, 0, 0)
		rotate_x(frame_count * 0.02)
		rotate_y(frame_count * 0.01)
		no_stroke()
		fill(255)
		blinn_phong_material()
		box(100, 100, 100)

	with push_matrix():
		translate(250, 0, -200)
		fill(255, 0, 0)
		locX = (mouse_x - width/2) * 100
		locY = (mouse_y - height/2)
		light_specular(0, 0, 255)
		point_light(360, 360*1.5, 360, locX, locY, 400)
		stroke(255)
		sphere(280)


if __name__ == '__main__':
	run(mode='P3D')