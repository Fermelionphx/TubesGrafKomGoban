# menggambar bidak dengan menggunakan pyOpenGL
import pygame
import pygame.locals
from OpenGL.GL import *
from OpenGL.GLU import *


# membuat bidak
def BidakAbu():
    
    glBegin(GL_POLYGON)
    # memberikan warna abu gelap pada bidak 
    glColor3f(0.3, 0.3, 0.3)  # Warna abu-abu gelap untuk bayangan
    
    # BIDAK TERLUAR
    glVertex3f(-3.0, 0.0, 0.0) #titik C (-3, 0)
    glVertex3f(-2.0, -2.0, 0.0) #titik D (-2, 2)
    glVertex3f(0.0, -3.0, 0.0) #titik E (0, -3)
    glVertex3f(2.0, -2.0, 0.0) #titik F (2, -2)
    glVertex3f(3.0 ,0.0, 0.0) #titik G (3, 0)
    glVertex3f(2.0 ,2.0, 0.0) #titik H (2, 2)
    glVertex3f(0.0 ,3.0, 0.0) #titik A (0, 3)
    glVertex3f(0.-2 ,2.0, 0.0) #titik B (-2, 2)
    glVertex3f(-3.0, 0.0, 0.0) #titik C (-3, 0)
    glEnd()
    
    # bidang tengah
    glBegin(GL_POLYGON)
    glColor3f(0.5, 0.5, 0.5)  # Warna abu-abu medium untuk warna dasar
    glVertex3f(-2.0, 0.0, 0.0) #titik K (-2, 0)
    glVertex3f(-1.40, -1.40, 0.0) #titik L (, 0)
    glVertex3f(0.0, -2.0, 0.0) #titik M (, 0)
    glVertex3f(1.40, -1.40, 0.0) #titik N (, 0)
    glVertex3f(2.0, 0.0, 0.0) #titik M (, 0)
    glVertex3f(1.40, 1.40, 0.0) #titik p (, 0)
    glVertex3f(0.0, 2.0, 0.0) #titik i (, 0)
    glVertex3f(-1.40, 1.40, 0.0) #titik J (, 0)
    glEnd()
    
    # bidang tengah
    glBegin(GL_POLYGON)
    glColor3f(0.8, 0.8, 0.8)  # Warna abu-abu terang untuk highlight
    glVertex3f(-1.0, 0.0, 0.0) #titik R (-2, 0)
    glVertex3f(0.0, -1.0, 0.0) #titik S (-2, 0)
    glVertex3f(1.0, 0.0, 0.0) #titik S (-2, 0)
    glVertex3f(0.0, 1.0, 0.0) #titik S (-2, 0)
    glEnd()
    
    
def main():
    # insiasi pygame
    pygame.init()
    
    # judul window
    pygame.display.set_caption("Tubes Grafkom")
    
    # ukuran window
    display = (800, 600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF|pygame.OPENGL)
    
     #membuat perspektif
    gluPerspective(110, (display[0]/display [1]), 0.1, 50.0)

    #menempatkan objek
    glTranslatef (0.0,0.0, -5.0)

    # melakukan perulangan True agar window tidak langsung tertutup
    while True:
        # event handling, mendapatkan semua event yang terjadi pada pygame
        for event in pygame.event.get():
            # jika event = quit, maka pygame berhenti
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #glclear untuk menghapus layar/menhapus buffer
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        BidakAbu()
        pygame.display.flip()

main()
    
    