
import numpy as np
import sys
import pygame
import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
class Display():
    X_Axis = (.5, 0, 0)
    Y_Axis = (0, .5, 0)
    Z_Axis = (0, 0, .5)
    def __init__(self, W, H):
        pygame.init()
        self.size = W,H
        self.screen = pygame.display.set_mode(self.size, 
                pygame.DOUBLEBUF|pygame.OPENGL)
        
        gluPerspective(45,self.size[0]/self.size[1],0.1,50.0)
        glTranslatef(0.0,0.0,-3)
        glRotatef(10, 1, 0, 0)
        glRotatef(-45,0,1,0)
    def paint(self):
         # get event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # paint
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) 
        self.draw_axis()
        pygame.display.flip()

    def draw_axis(self):
        glBegin(GL_LINES)
        # x-axis red color
        glColor3f(RED[0],RED[1],RED[2])
        glVertex3f(0,0,0)
        glVertex3f(self.X_Axis[0],self.X_Axis[1],self.X_Axis[2])
        # y-axis green color
        glColor3f(GREEN[0],GREEN[1],GREEN[2])
        glVertex3f(0,0,0)
        glVertex3f(self.Y_Axis[0],self.Y_Axis[1],self.Y_Axis[2])
        # z-axis blue color
        glColor3f(BLUE[0],BLUE[1],BLUE[2])
        glVertex3f(0,0,0)
        glVertex3f(self.Z_Axis[0],self.Z_Axis[1],self.Z_Axis[2])
        glEnd();
#        glRotatef(1,3,1,1)


