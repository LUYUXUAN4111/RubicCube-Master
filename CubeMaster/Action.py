import numpy as np
from matplotlib import pyplot as plt
from MakeCube import makeCube
class action:
    def __init__(self,cube):
        self.cube = cube
        self.f = self.cube[0]
        self.l = self.cube[1]
        self.b = self.cube[2]
        self.r = self.cube[3]
        self.u = self.cube[4]
        self.d = self.cube[5]
        self.title = ""
        self.radius = 30
        fig = plt.figure(figsize=(5, 5),
                         facecolor='whitesmoke'
                         )
        self.ax = fig.gca(fc='whitesmoke',
                     projection='3d'
                     )

        plt.ion()

    def printCube(self):
        plt.ioff()
        plt.show()
    def U1(self):
        f = self.f[0]
        r = self.r[0]
        b = self.b[0]
        self.f[0] = r
        self.r[0] = b
        self.b[0] = self.l[0]
        self.l[0] = f
        u = np.rot90(self.u,-1)
        self.u[0] = u[0]
        self.u[1] = u[1]
        self.u[2] = u[2]
        self.title += "U "
        self.radius +=1
        if (self.radius-29)%50 == 0:
            self.title += "\n"
        makeCube(self.cube,self.ax,self.title,self.radius)
    def U2(self):
        f = self.f[0]
        r = self.r[0]
        b = self.b[0]
        self.f[0] = self.l[0]
        self.r[0] = f
        self.b[0] = r
        self.l[0] = b
        u = np.rot90(self.u,1)
        self.u[0] = u[0]
        self.u[1] = u[1]
        self.u[2] = u[2]
        self.title += "U' "
        self.radius +=1
        if (self.radius-29)%50 == 0:
            self.title += "\n"
        makeCube(self.cube,self.ax,self.title,self.radius)
    def R1(self):
        u9,u6,u3 = self.u[2][2],self.u[1][2],self.u[0][2]
        f3,f6,f9 = self.f[0][2],self.f[1][2],self.f[2][2]
        d3,d6,d9 = self.d[0][2],self.d[1][2],self.d[2][2]
        self.d[0][2], self.d[1][2], self.d[2][2] = self.b[2][0],self.b[1][0],self.b[0][0]
        self.b[0][0], self.b[1][0], self.b[2][0] = u9,u6,u3
        self.f[0][2], self.f[1][2], self.f[2][2] = d3,d6,d9
        self.u[0][2], self.u[1][2], self.u[2][2] = f3,f6,f9
        r = np.rot90(self.r,-1)
        self.r[0] = r[0]
        self.r[1] = r[1]
        self.r[2] = r[2]
        self.title += "R "
        self.radius +=1
        if (self.radius-29)%50 == 0:
            self.title += "\n"
        makeCube(self.cube,self.ax,self.title,self.radius)
    def R2(self):
        u3,u6,u9 = self.u[0][2],self.u[1][2],self.u[2][2]
        f3,f6,f9 = self.f[0][2],self.f[1][2],self.f[2][2]
        d9,d6,d3 = self.d[2][2],self.d[1][2],self.d[0][2]
        self.d[0][2], self.d[1][2], self.d[2][2] = f3,f6,f9
        self.u[0][2], self.u[1][2], self.u[2][2] = self.b[2][0], self.b[1][0], self.b[0][0]
        self.b[0][0], self.b[1][0], self.b[2][0] = d9,d6,d3
        self.f[0][2], self.f[1][2], self.f[2][2] = u3,u6,u9
        r = np.rot90(self.r,1)
        self.r[0] = r[0]
        self.r[1] = r[1]
        self.r[2] = r[2]
        self.title += "R' "
        self.radius +=1
        if (self.radius-29)%50 == 0:
            self.title += "\n"
        makeCube(self.cube,self.ax,self.title,self.radius)
    def L1(self):
        u1,u4,u7 = self.u[0][0],self.u[1][0],self.u[2][0]
        f1,f4,f7 = self.f[0][0],self.f[1][0],self.f[2][0]
        d7,d4,d1 = self.d[2][0],self.d[1][0],self.d[0][0]
        self.d[0][0],self.d[1][0],self.d[2][0] = f1,f4,f7
        self.u[0][0], self.u[1][0], self.u[2][0] = self.b[2][2], self.b[1][2], self.b[0][2]
        self.b[0][2], self.b[1][2], self.b[2][2] = d7,d4,d1
        self.f[0][0], self.f[1][0], self.f[2][0] = u1,u4,u7
        l = np.rot90(self.l,-1)
        self.l[0] = l[0]
        self.l[1] = l[1]
        self.l[2] = l[2]
        self.title += "L "
        self.radius +=1
        if (self.radius-29)%50 == 0:
            self.title += "\n"
        makeCube(self.cube,self.ax,self.title,self.radius)
    def L2(self):
        u7,u4,u1 = self.u[2][0],self.u[1][0],self.u[0][0]
        f1,f4,f7 = self.f[0][0],self.f[1][0],self.f[2][0]
        d1,d4,d7 = self.d[0][0],self.d[1][0],self.d[2][0]
        self.d[0][0],self.d[1][0],self.d[2][0] = self.b[2][2], self.b[1][2], self.b[0][2]
        self.u[0][0], self.u[1][0], self.u[2][0] = f1,f4,f7
        self.b[0][2], self.b[1][2], self.b[2][2] = u7,u4,u1
        self.f[0][0], self.f[1][0], self.f[2][0] = d1,d4,d7
        l = np.rot90(self.l,1)
        self.l[0] = l[0]
        self.l[1] = l[1]
        self.l[2] = l[2]
        self.title += "L' "
        self.radius +=1
        if (self.radius-29)%50 == 0:
            self.title += "\n"
        makeCube(self.cube,self.ax,self.title,self.radius)
    def F1(self):
        l9,l6,l3 = self.l[2][2],self.l[1][2],self.l[0][2]
        r7,r4,r1 = self.r[2][0],self.r[1][0],self.r[0][0]
        u7,u8,u9 = self.u[2]
        d1,d2,d3 = self.d[0]
        self.l[0][2],self.l[1][2],self.l[2][2] = d1,d2,d3
        self.r[0][0],self.r[1][0],self.r[2][0] = u7,u8,u9
        self.u[2] = [l9,l6,l3]
        self.d[0] = [r7,r4,r1]
        f = np.rot90(self.f,-1)
        self.f[0] = f[0]
        self.f[1] = f[1]
        self.f[2] = f[2]
        self.title += "F "
        self.radius +=1
        if (self.radius-29)%50 == 0:
            self.title += "\n"
        makeCube(self.cube,self.ax,self.title,self.radius)
    def F2(self):
        l3,l6,l9 = self.l[0][2],self.l[1][2],self.l[2][2]
        r1,r4,r7 = self.r[0][0],self.r[1][0],self.r[2][0]
        u7,u8,u9 = self.u[2]
        d1,d2,d3 = self.d[0]
        self.l[0][2],self.l[1][2],self.l[2][2] = u9,u8,u7
        self.r[0][0],self.r[1][0],self.r[2][0] = d3,d2,d1
        self.u[2] = [r1,r4,r7]
        self.d[0] = [l3,l6,l9]
        f = np.rot90(self.f,1)
        self.f[0] = f[0]
        self.f[1] = f[1]
        self.f[2] = f[2]
        self.title += "F' "
        self.radius +=1
        if (self.radius-29)%50 == 0:
            self.title += "\n"
        makeCube(self.cube,self.ax,self.title,self.radius)
    def B1(self):
        u1,u2,u3 = self.u[0]
        d7,d8,d9 = self.d[2]
        r3,r6,r9 = self.r[0][2],self.r[1][2],self.r[2][2]
        l1,l4,l7 = self.l[0][0],self.l[1][0],self.l[2][0]
        self.l[0][0], self.l[1][0], self.l[2][0] = u3,u2,u1
        self.r[0][2], self.r[1][2], self.r[2][2] = d9,d8,d7
        self.u[0] = [r3,r6,r9]
        self.d[2] = [l1,l4,l7]
        b = np.rot90(self.b,-1)
        self.b[0] = b[0]
        self.b[1] = b[1]
        self.b[2] = b[2]
        self.title += "B "
        self.radius +=1
        if (self.radius-29)%50 == 0:
            self.title += "\n"
        makeCube(self.cube,self.ax,self.title,self.radius)
    def B2(self):
        u1,u2,u3 = self.u[0]
        d7,d8,d9 = self.d[2]
        r9,r6,r3 = self.r[2][2],self.r[1][2],self.r[0][2]
        l7,l4,l1 = self.l[2][0],self.l[1][0],self.l[0][0]
        self.l[0][0], self.l[1][0], self.l[2][0] = d7,d8,d9
        self.r[0][2], self.r[1][2], self.r[2][2] = u1,u2,u3
        self.u[0] = [l7,l4,l1]
        self.d[2] = [r9,r6,r3]
        b = np.rot90(self.b,1)
        self.b[0] = b[0]
        self.b[1] = b[1]
        self.b[2] = b[2]
        self.title += "B' "
        self.radius +=1
        if (self.radius-29)%50 == 0:
            self.title += "\n"
        makeCube(self.cube,self.ax,self.title,self.radius)
    def D1(self):
        f = self.f[2]
        r = self.r[2]
        b = self.b[2]
        l = self.l[2]
        self.f[2] = l
        self.r[2] = f
        self.b[2] = r
        self.l[2] = b
        d = np.rot90(self.d,-1)
        self.d[0] = d[0]
        self.d[1] = d[1]
        self.d[2] = d[2]
        self.title += "D "
        self.radius +=1
        if (self.radius-29)%50 == 0:
            self.title += "\n"
        makeCube(self.cube,self.ax,self.title,self.radius)
    def D2(self):
        f = self.f[2]
        r = self.r[2]
        b = self.b[2]
        l = self.l[2]
        self.f[2] = r
        self.r[2] = b
        self.b[2] = l
        self.l[2] = f
        d = np.rot90(self.d,1)
        self.d[0] = d[0]
        self.d[1] = d[1]
        self.d[2] = d[2]
        self.title += "D' "
        self.radius +=1
        if (self.radius-29)%50 == 0:
            self.title += "\n"
        makeCube(self.cube,self.ax,self.title,self.radius)
    def C1(self):
        f = self.f[1]
        r = self.r[1]
        b = self.b[1]
        l = self.l[1]
        self.f[1] = r
        self.r[1] = b
        self.b[1] = l
        self.l[1] = f
        self.title += "C "
        self.radius +=1
        if (self.radius-29)%50 == 0:
            self.title += "\n"
        makeCube(self.cube,self.ax,self.title,self.radius)
    def C2(self):
        f = self.f[1]
        r = self.r[1]
        b = self.b[1]
        l = self.l[1]
        self.f[1] = l
        self.r[1] = f
        self.b[1] = r
        self.l[1] = b
        self.title += "C' "
        self.radius +=1
        if (self.radius-29)%50 == 0:
            self.title += "\n"
        makeCube(self.cube,self.ax,self.title,self.radius)
    def Y(self):
        f = [self.f[0],self.f[1],self.f[2]]
        r = self.r
        b = self.b
        l = self.l
        self.f[0],self.f[1],self.f[2] = r
        self.r[0],self.r[1],self.r[2] = b
        self.b[0],self.b[1],self.b[2] = l
        self.l[0],self.l[1],self.l[2] = f
        u = np.rot90(self.u, -1)
        self.u[0] = u[0]
        self.u[1] = u[1]
        self.u[2] = u[2]
        d = np.rot90(self.d,1)
        self.d[0] = d[0]
        self.d[1] = d[1]
        self.d[2] = d[2]
        self.title += "Y "
        self.radius +=1
        if (self.radius-29)%50 == 0:
            self.title += "\n"
        makeCube(self.cube,self.ax,self.title,self.radius)
    def X(self):
        f = [self.f[0],self.f[1],self.f[2]]
        b = np.rot90(self.b, -1)
        b = np.rot90(b,-1)
        u = self.u
        d = np.rot90(self.d, -1)
        d = np.rot90(d,-1)
        self.f[0],self.f[1],self.f[2] = u
        self.u[0],self.u[1],self.u[2] = b
        self.b[0],self.b[1],self.b[2] = d
        self.d[0],self.d[1],self.d[2] = f
        l = np.rot90(self.l, -1)
        self.l[0] = l[0]
        self.l[1] = l[1]
        self.l[2] = l[2]
        r = np.rot90(self.r,1)
        self.r[0] = r[0]
        self.r[1] = r[1]
        self.r[2] = r[2]
        self.title += "X "
        self.radius +=1
        if (self.radius-29)%50 == 0:
            self.title += "\n"
        makeCube(self.cube,self.ax,self.title,self.radius)
    def Z(self):
        f = [self.f[0],self.f[1],self.f[2]]
        r = self.r
        b = self.b
        l = self.l
        self.f[0],self.f[1],self.f[2] = l
        self.l[0],self.l[1],self.l[2] = b
        self.b[0],self.b[1],self.b[2] = r
        self.r[0],self.r[1],self.r[2] = f
        u = np.rot90(self.u, 1)
        self.u[0] = u[0]
        self.u[1] = u[1]
        self.u[2] = u[2]
        d = np.rot90(self.d,-1)
        self.d[0] = d[0]
        self.d[1] = d[1]
        self.d[2] = d[2]
        self.title += "Y "
        self.radius +=1
        if (self.radius-29)%50 == 0:
            self.title += "\n"
        makeCube(self.cube,self.ax,self.title,self.radius)







