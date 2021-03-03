# coding:utf-8

import sys
from math import pi as PI
from math import sin, cos
from math import sqrt

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


# 将指定为三个坐标组的法线向量换算。
def ReduceToUnit(vector):
    # 计算向量长度
    length = sqrt((vector[0] * vector[0]) + (vector[1] * vector[1]) + (vector[2] * vector[2]))
    # Keep the program from blowing up by providing an exceptable
    # value for vectors that may calculated too close to zero.
    if (length == 0.0):
        length = 1.0
    # 除以长度获得单位法向量
    vector[0] /= length
    vector[1] /= length
    vector[2] /= length


# Points p1, p2, & p3 specified in counter clock-wise order
# float v[3][3], float out[3]
def calcNormal(v, out):
    # float v1[3],v2[3];
    v1 = [0.0 for i in range(3)]
    v2 = [0.0 for i in range(3)]
    out = [0.0 for i in range(3)]
    xx = 0
    yy = 1
    zz = 2

    # Calculate two vectors from the three points
    v1[xx] = v[0][xx] - v[1][xx]
    v1[yy] = v[0][yy] - v[1][yy]
    v1[zz] = v[0][zz] - v[1][zz]

    v2[xx] = v[1][xx] - v[2][xx]
    v2[yy] = v[1][yy] - v[2][yy]
    v2[zz] = v[1][zz] - v[2][zz]

    # Take the cross product of the two vectors to get
    # the normal vector which will be stored in out
    out[xx] = v1[yy] * v2[zz] - v1[zz] * v2[yy]
    out[yy] = v1[zz] * v2[xx] - v1[xx] * v2[zz]
    out[zz] = v1[xx] * v2[yy] - v1[yy] * v2[xx]

    # Normalize the vector (shorten length to one)
    ReduceToUnit(out)


def RenderThread():
    global x, y, z, angle  # Calculate coordinates and step angle
    height = 75.0  # Height of the threading
    diameter = 20.0  # Diameter of the threading
    # float normal[3],corners[2][3];    // Storeage of vertices and normals
    corners = [[0.0 for i in range(3)] for i in range(4)]
    normal = [0.0 for i in range(3)]
    step = (PI / 32.0)  # one revolution
    revolutions = 7.0  # How many time around the shaft
    threadWidth = 2.0  # How wide is the thread
    threadThick = 3.0  # How thick is the thread
    zstep = 0.125  # How much does the thread move up the Z axis each time a new segment is drawn.

    # Set material color for head of screw
    glColor3f(0.0, 0.0, 0.4)
    z = -height / 2.0 + 2  # Starting spot almost to the end

    angle = 0
    while angle < (2.0 * PI) * revolutions:
        # Calculate x and y position of the next vertex
        x = diameter * sin(angle)
        y = diameter * cos(angle)
        #  Store the next vertex next to the shaft.
        corners[0][0] = x
        corners[0][1] = y
        corners[0][2] = z
        # Calculate the position away from the shaft
        x = (diameter + threadWidth) * sin(angle)
        y = (diameter + threadWidth) * cos(angle)
        corners[1][0] = x
        corners[1][1] = y
        corners[1][2] = z
        # Calculate the next position away from the shaft
        x = (diameter + threadWidth) * sin(angle + step)
        y = (diameter + threadWidth) * cos(angle + step)
        corners[2][0] = x
        corners[2][1] = y
        corners[2][2] = z + zstep
        # Calculate the next position along the shaft
        x = (diameter) * sin(angle + step)
        y = (diameter) * cos(angle + step)
        corners[3][0] = x
        corners[3][1] = y
        corners[3][2] = z + zstep
        # We'll be using triangels, so make counter clock-wise polygons face out
        glFrontFace(GL_CCW)
        glBegin(GL_TRIANGLES)  # Start the top section of thread

        # Calculate the normal for this segment
        calcNormal(corners, normal)
        glNormal3fv(normal)
        # Draw two triangles to cover area
        glVertex3fv(corners[0])
        glVertex3fv(corners[1])
        glVertex3fv(corners[2])

        glVertex3fv(corners[2])
        glVertex3fv(corners[3])
        glVertex3fv(corners[0])

        glEnd()
        # Move the edge along the shaft slightly up the z axis to represent the bottom of the thread
        corners[0][2] += threadThick
        corners[3][2] += threadThick

        # Recalculate the normal since points have changed, thistime it points in the opposite direction, so reverse it
        calcNormal(corners, normal)
        normal[0] = -normal[0]
        normal[1] = -normal[1]
        normal[2] = -normal[2]

        # Switch to clock-wise facing out for underside of the thread.
        glFrontFace(GL_CW)

        # Draw the two triangles
        glBegin(GL_TRIANGLES)
        glNormal3fv(normal)

        glVertex3fv(corners[0])
        glVertex3fv(corners[1])
        glVertex3fv(corners[2])

        glVertex3fv(corners[2])
        glVertex3fv(corners[3])
        glVertex3fv(corners[0])

        glEnd()

        # Creep up the Z axis
        z += zstep
        angle += step


def RenderScene():
    global xRot, yRot
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Save the matrix state
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    # 绕X轴和Y轴旋转(角度,x,y,z)
    glRotatef(xRot, 1.0, 0.0, 0.0)
    glRotatef(yRot, 0.0, 0.0, 1.0)
    # Render just the hexagonial head of the nut
    RenderThread()
    glPopMatrix()
    # 双缓冲的刷新模式； Swap buffers
    glutSwapBuffers()


# 设置渲染状态
def SetupRC():
    # Light values and coordinates光照 值与坐标；环境光，漫射光，镜面光，光的坐标,
    ambientLight = [0.4, 0.4, 0.4, 1.0]
    diffuseLight = [0.7, 0.7, 0.7, 1.0]
    specular = [0.9, 0.9, 0.9, 1.0]
    lightPos = [-50.0, 200.0, 200.0, 1.0]
    specref = [0.6, 0.6, 0.6, 1.0]

    glEnable(GL_DEPTH_TEST)  # Hidden surface removal
    glEnable(GL_CULL_FACE)  # Do not calculate inside of solid object
    glFrontFace(GL_CCW)

    glEnable(GL_LIGHTING)

    # Setup light 0
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambientLight)
    glLightfv(GL_LIGHT0, GL_AMBIENT, ambientLight)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuseLight)
    glLightfv(GL_LIGHT0, GL_SPECULAR, specular)

    # Position and turn on the light
    glLightfv(GL_LIGHT0, GL_POSITION, lightPos)
    glEnable(GL_LIGHT0)

    # Enable color tracking
    glEnable(GL_COLOR_MATERIAL)

    # Set Material properties to follow glColor values
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

    # All materials hereafter have full specular reflectivity with a moderate shine
    glMaterialfv(GL_FRONT, GL_SPECULAR, specref)
    glMateriali(GL_FRONT, GL_SHININESS, 64)

    glClearColor(0.0, 0.0, 0.0, 1.0)  # 背景黑色


# 改变窗口大小时调用
def ChangeSize(w, h):
    nRange = 100.0
    if (h == 0):  # 防止除数为0
        h = 1
    glViewport(0, 0, w, h)  # 设置视区大小
    glMatrixMode(GL_PROJECTION)  # 投影矩阵模式
    glLoadIdentity()  # 矩阵堆栈清空
    # 设置裁剪窗口大小
    if (w <= h):
        glOrtho(-nRange, nRange, -nRange * h / w, nRange * h / w, -nRange * 2.0, nRange * 2.0)
    else:
        glOrtho(-nRange * w / h, nRange * w / h, -nRange, nRange, -nRange * 2.0, nRange * 2.0)

    glMatrixMode(GL_MODELVIEW)  # 模型矩阵模式
    glLoadIdentity()


def SpecialKeys(key, x, y):
    global xRot, yRot
    if (key == GLUT_KEY_UP):
        xRot -= 5.0
    if (key == GLUT_KEY_DOWN):
        xRot += 5.0
    if (key == GLUT_KEY_LEFT):
        yRot -= 5.0
    if (key == GLUT_KEY_RIGHT):
        yRot += 5.0
    if (key > 356.0):
        xRot = 0.0
    if (key < -1.0):
        xRot = 355.0
    if (key > 356.0):
        yRot = 0.0
    if (key < -1.0):
        yRot = 355.0
    glutPostRedisplay()


xRot = 0.0
yRot = 0.0
print("三维螺纹，按箭头键改变视角！")
# 使用glut初始化OpenGL
glutInit()
glutInitWindowSize(700, 700)
# 设置显示模式；（注意双缓冲）
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutCreateWindow("Bolt Thread")

glutReshapeFunc(ChangeSize)
glutSpecialFunc(SpecialKeys)  # 注册键盘回调函数
# 调用函数绘制图像
glutDisplayFunc(RenderScene)
SetupRC()
# 主循环
glutMainLoop()
