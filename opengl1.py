import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Define shapes (cube and pyramid)
cube_vertices = [
    [1, 1, -1], [1, -1, -1], [-1, -1, -1], [-1, 1, -1],
    [1, 1, 1], [1, -1, 1], [-1, -1, 1], [-1, 1, 1],
]

cube_edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7),
]

pyramid_vertices = [
    [0, 1, 0], [1, -1, 1], [1, -1, -1], [-1, -1, -1], [-1, -1, 1]
]

pyramid_faces = [
    (0, 1, 2), (0, 2, 3), (0, 3, 4), (0, 4, 1),
    (1, 2, 3, 4)
]

colors = [
    [1, 0, 0], [0, 1, 0], [0, 0, 1],
    [1, 1, 0], [1, 0, 1], [0, 1, 1],
]

def draw_cube():
    glBegin(GL_LINES)
    glColor3f(1, 1, 1)
    for edge in cube_edges:
        for vertex in edge:
            glVertex3fv(cube_vertices[vertex])
    glEnd()

def draw_pyramid():
    glBegin(GL_TRIANGLES)
    for i, face in enumerate(pyramid_faces[:-1]):
        glColor3fv(colors[i % len(colors)])
        for vertex in face:
            glVertex3fv(pyramid_vertices[vertex])
    glEnd()

    glBegin(GL_QUADS)
    glColor3fv((0.5, 0.5, 0.5))
    for vertex in pyramid_faces[-1]:
        glVertex3fv(pyramid_vertices[vertex])
    glEnd()

def setup_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)

    glLightfv(GL_LIGHT0, GL_POSITION, [1, 1, 1, 1])
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.8, 0.8, 0.8, 1])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1, 1, 1, 1])

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)

    setup_lighting()
    clock = pygame.time.Clock()
    angle = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        angle += 1

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()

        # Draw rotating cube
        glTranslatef(-2, 0, 0)
        glRotatef(angle, 1, 1, 0)
        draw_cube()

        glPopMatrix()
        glPushMatrix()

        # Draw rotating pyramid
        glTranslatef(2, 0, 0)
        glRotatef(-angle, 0, 1, 1)
        draw_pyramid()

        glPopMatrix()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()