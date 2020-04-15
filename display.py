import sys
import pygame
from OpenGLContext import testingcontext
BaseContext = testingcontext.getInteractive()
import OpenGL
from OpenGL.GL import *
from OpenGL.arrays import vbo
from OpenGLContext.arrays import *
from OpenGL.GL import shaders
from OpenGL.GLU import *
import glm 

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Display(BaseContext):
    X_Axis = glm.vec3(1, 0, 0)
    Y_Axis = glm.vec3(0, 1, 0)
    Z_Axis = glm.vec3(0, 0, 1)
   # view = glm.lookAt(glm.vec3(0.0, 0.0, 3.0),glm.vec3(0.0, 0.0, 0.0),glm.vec3(0.0, 1.0, 0.0))
    def __init__(self, W, H):
        pygame.init()
        self.size = W,H
        self.screen = pygame.display.set_mode(self.size, 
                pygame.DOUBLEBUF|pygame.OPENGL)
        self.WaitInput = False 

    def OnInit(self):
        glViewport(0,0,W,H)
        gluPerspective(60,self.size[0]/self.size[1],0.1,50.0)
        glTranslatef(0.0,0.0,-5)

    def paint(self):
         # get event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-0.5,0.0,0.0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(0.5,0.0,0.0)
                if event.key == pygame.K_UP:
                    glTranslatef(0.0,1.0,0.0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0.0,-1.0,0.0)
                if event.key == pygame.K_SPACE:
                    self.WaitInput = True             # paint

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) 
        self.draw_axis()
        pygame.display.flip()
        pygame.time.wait(10)
    def draw_axis(self):
        gl_PointSize = 100
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


