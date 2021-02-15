from Action import action
class Return:
    def __init__(self,cube):
        super(Return, self).__init__()
        self.ACTION = action(cube)
        self.makeTwoBlocks()
        self.makeThreeBLocks()
    def makeTwoBlocks(self):
        self.twoFaceBlock = {
            "F2U8" : [self.ACTION.f[0][1],self.ACTION.u[2][1]],
            "F4L6" : [self.ACTION.f[1][0],self.ACTION.l[1][2]],
            "F6R4" : [self.ACTION.f[1][2],self.ACTION.r[1][0]],
            "F8D2" : [self.ACTION.f[2][1],self.ACTION.d[0][1]],
            "B2U2" : [self.ACTION.b[0][1],self.ACTION.u[0][1]],
            "B4R6" : [self.ACTION.b[1][0],self.ACTION.r[1][2]],
            "B8D8" : [self.ACTION.b[2][1],self.ACTION.d[2][1]],
            "B6L4" : [self.ACTION.b[1][2],self.ACTION.l[1][0]],
            "R2U6" : [self.ACTION.r[0][1],self.ACTION.u[1][2]],
            "R8D6" : [self.ACTION.r[2][1],self.ACTION.d[1][2]],
            "L2U4" : [self.ACTION.l[0][1],self.ACTION.u[1][0]],
            "L8D4" : [self.ACTION.l[2][1],self.ACTION.d[1][0]]
        }
    def makeThreeBLocks(self):
        self.threeFaceBlocks = {
            "F1U7L3" : [self.ACTION.f[0][0],self.ACTION.u[2][0],self.ACTION.l[0][2]],
            "F3U9R1" : [self.ACTION.f[0][2],self.ACTION.u[2][2],self.ACTION.r[0][0]],
            "F7D1L9" : [self.ACTION.f[2][0],self.ACTION.d[0][0],self.ACTION.l[2][2]],
            "F9D3R7" : [self.ACTION.f[2][2],self.ACTION.d[0][2],self.ACTION.r[2][0]],
            "B1U3R3" : [self.ACTION.b[0][0],self.ACTION.u[0][2],self.ACTION.r[0][2]],
            "B3U1L1" : [self.ACTION.b[0][2],self.ACTION.u[0][0],self.ACTION.l[0][0]],
            "B7D9R9" : [self.ACTION.b[2][0],self.ACTION.d[2][2],self.ACTION.r[2][2]],
            "B9D7L7" : [self.ACTION.b[2][2],self.ACTION.d[2][0],self.ACTION.l[2][0]]
        }
    def makeTopTwoFace(self):
        self.TopTwoFace = {
            "F2U8": [self.ACTION.f[0][1], self.ACTION.u[2][1]],
            "B2U2": [self.ACTION.b[0][1], self.ACTION.u[0][1]],
            "R2U6": [self.ACTION.r[0][1], self.ACTION.u[1][2]],
            "L2U4": [self.ACTION.l[0][1], self.ACTION.u[1][0]],
        }
    def makeTopAngel(self):
        self.TopAngel={
            "F1U7L3": [self.ACTION.f[0][0], self.ACTION.u[2][0], self.ACTION.l[0][2]],
            "F3U9R1": [self.ACTION.f[0][2], self.ACTION.u[2][2], self.ACTION.r[0][0]],
            "B1U3R3": [self.ACTION.b[0][0], self.ACTION.u[0][2], self.ACTION.r[0][2]],
            "B3U1L1": [self.ACTION.b[0][2], self.ACTION.u[0][0], self.ACTION.l[0][0]],
        }
    def makeTopBlock(self):
        self.TopBlock={
            "F" : [self.ACTION.f[0][0],self.ACTION.f[0][1],self.ACTION.f[0][2]],
            "R": [self.ACTION.r[0][0], self.ACTION.r[0][1], self.ACTION.r[0][2]],
            "B": [self.ACTION.b[0][0], self.ACTION.b[0][1], self.ACTION.b[0][2]],
            "L": [self.ACTION.l[0][0], self.ACTION.l[0][1], self.ACTION.l[0][2]]
        }
    def return1stFace(self):
        self.returnBlock1(self.ACTION.f[1][1],self.ACTION.u[1][1],self.ACTION.f[0][1],self.ACTION.u[2][1])
        self.makeTwoBlocks()
        self.returnBlock1(self.ACTION.f[1][1],self.ACTION.u[1][1],self.ACTION.f[0][1],self.ACTION.u[2][1])
        self.makeTwoBlocks()
        self.returnBlock1(self.ACTION.f[1][1],self.ACTION.u[1][1],self.ACTION.f[0][1],self.ACTION.u[2][1])
        self.makeTwoBlocks()
        self.returnBlock1(self.ACTION.f[1][1],self.ACTION.u[1][1],self.ACTION.f[0][1],self.ACTION.u[2][1])
        self.makeTwoBlocks()
    def returnBlock1(self,colorC1,colorC2,block1,block2):
        if (colorC1!=block1) or (colorC2!=block2):
            block = self.getBlock(colorC1,colorC2)
            if block == "F2U8":
                self.ACTION.F1()
                self.ACTION.C1()
                self.ACTION.F1()
                self.ACTION.C2()
            elif block == "F4L6":
                if self.twoFaceBlock[block][0] == colorC1:
                    self.ACTION.F1()
                else:
                    self.ACTION.C2()
                    self.ACTION.F2()
                    self.ACTION.C1()
            elif block == "F6R4":
                if self.twoFaceBlock[block][0] == colorC1:
                    self.ACTION.F2()
                else:
                    self.ACTION.C1()
                    self.ACTION.F1()
                    self.ACTION.C2()
            elif block == "F8D2":
                if self.twoFaceBlock[block][0] == colorC1:
                    self.ACTION.F1()
                    self.ACTION.F1()
                else:
                    self.ACTION.F1()
                    self.ACTION.C2()
                    self.ACTION.F2()
                    self.ACTION.C1()
            elif block == "B2U2":
                if self.twoFaceBlock[block][0] == colorC1:
                    self.ACTION.B2()
                    self.ACTION.C1()
                    self.ACTION.C1()
                    self.ACTION.B1()
                    self.ACTION.F1()
                    self.ACTION.C1()
                    self.ACTION.C1()
                else:
                    self.ACTION.B2()
                    self.ACTION.C1()
                    self.ACTION.B1()
                    self.ACTION.F2()
                    self.ACTION.C2()
            elif block == "B4R6":
                if self.twoFaceBlock[block][0] == colorC1:
                    self.ACTION.C1()
                    self.ACTION.C1()
                    self.ACTION.F1()
                    self.ACTION.C1()
                    self.ACTION.C1()
                else:
                    self.ACTION.C1()
                    self.ACTION.F2()
                    self.ACTION.C2()
            elif block == "B8D8":
                if self.twoFaceBlock[block][0] == colorC1:
                    self.ACTION.D2()
                    self.ACTION.D2()
                    self.ACTION.F1()
                    self.ACTION.F1()
                else:
                    self.ACTION.D2()
                    self.ACTION.D2()
                    self.ACTION.F1()
                    self.ACTION.C2()
                    self.ACTION.F2()
                    self.ACTION.C1()
            elif block == "B6L4":
                if self.twoFaceBlock[block][0] == colorC1:
                    self.ACTION.C2()
                    self.ACTION.C2()
                    self.ACTION.F2()
                    self.ACTION.C2()
                    self.ACTION.C2()
                else:
                    self.ACTION.C2()
                    self.ACTION.F1()
                    self.ACTION.C1()
            elif block == "R2U6":
                if self.twoFaceBlock[block][0] == colorC1:
                    self.ACTION.R2()
                    self.ACTION.C1()
                    self.ACTION.F1()
                    self.ACTION.C2()
                else:
                    self.ACTION.R2()
                    self.ACTION.C1()
                    self.ACTION.R1()
                    self.ACTION.C2()
                    self.ACTION.F2()
            elif block == "R8D6":
                if self.twoFaceBlock[block][0] == colorC1:
                    self.ACTION.D2()
                    self.ACTION.F1()
                    self.ACTION.F1()
                else:
                    self.ACTION.D2()
                    self.ACTION.F1()
                    self.ACTION.C2()
                    self.ACTION.F2()
                    self.ACTION.C1()
            elif block == "L2U4":
                if self.twoFaceBlock[block][0] == colorC1:
                    self.ACTION.L1()
                    self.ACTION.C2()
                    self.ACTION.L2()
                    self.ACTION.F2()
                    self.ACTION.C1()
                else:
                    self.ACTION.L1()
                    self.ACTION.C2()
                    self.ACTION.L2()
                    self.ACTION.C1()
                    self.ACTION.F1()
            elif block == "L8D4":
                if self.twoFaceBlock[block][0] == colorC1:
                    self.ACTION.D1()
                    self.ACTION.F1()
                    self.ACTION.F1()
                else:
                    self.ACTION.D1()
                    self.ACTION.F1()
                    self.ACTION.C2()
                    self.ACTION.F2()
                    self.ACTION.C1()
        self.ACTION.Y()
    def getBlock(self,color1,color2):
        for block in self.twoFaceBlock.keys():
            if (self.twoFaceBlock[block][0] == color1 and self.twoFaceBlock[block][1] == color2) or (self.twoFaceBlock[block][0] == color2 and self.twoFaceBlock[block][1] == color1):
                return block
    def return1stFace1(self):
        self.makeThreeBLocks()
        self.returnAngel(self.ACTION.f[1][1],self.ACTION.u[1][1],self.ACTION.r[1][1],self.ACTION.f[0][2],self.ACTION.u[2][2],self.ACTION.r[0][0])
        self.makeThreeBLocks()
        self.returnAngel(self.ACTION.f[1][1],self.ACTION.u[1][1],self.ACTION.r[1][1],self.ACTION.f[0][2],self.ACTION.u[2][2],self.ACTION.r[0][0])
        self.makeThreeBLocks()
        self.returnAngel(self.ACTION.f[1][1],self.ACTION.u[1][1],self.ACTION.r[1][1],self.ACTION.f[0][2],self.ACTION.u[2][2],self.ACTION.r[0][0])
        self.makeThreeBLocks()
        self.returnAngel(self.ACTION.f[1][1],self.ACTION.u[1][1],self.ACTION.r[1][1],self.ACTION.f[0][2],self.ACTION.u[2][2],self.ACTION.r[0][0])
        self.makeThreeBLocks()
        self.ACTION.X()
        self.ACTION.X()
        # self.ACTION.printCube()
    def returnAngel(self,color1,color2,color3,needC1,needC2,needC3):
        if color1!=needC1 or color2!=needC2 or color3!= needC3:
            angel = self.getAngle(color1,color2,color3)
            if angel == "F1U7L3":
                if self.threeFaceBlocks[angel][0] == color1:
                    self.ACTION.L1()
                    self.ACTION.D1()
                    self.ACTION.L2()
                    self.ACTION.D2()
                    self.ACTION.R2()
                    self.ACTION.D1()
                    self.ACTION.R1()
                elif self.threeFaceBlocks[angel][0] == color2:
                    self.ACTION.L1()
                    self.ACTION.D1()
                    self.ACTION.L2()
                    self.ACTION.R2()
                    self.ACTION.D2()
                    self.ACTION.D2()
                    self.ACTION.R1()
                    self.ACTION.D1()
                    self.ACTION.R2()
                    self.ACTION.D2()
                    self.ACTION.R1()
                else:
                    self.ACTION.L1()
                    self.ACTION.D1()
                    self.ACTION.L2()
                    self.ACTION.R2()
                    self.ACTION.D2()
                    self.ACTION.R1()
            elif angel == "F3U9R1":
                if self.threeFaceBlocks[angel][0] == color2:
                    self.ACTION.R2()
                    self.ACTION.D2()
                    self.ACTION.R1()
                    self.ACTION.D1()
                    self.ACTION.R2()
                    self.ACTION.D2()
                    self.ACTION.D2()
                    self.ACTION.R1()
                    self.ACTION.D1()
                    self.ACTION.R2()
                    self.ACTION.D2()
                    self.ACTION.R1()
                else:
                    self.ACTION.R2()
                    self.ACTION.D2()
                    self.ACTION.R1()
                    self.ACTION.D1()
                    self.ACTION.R2()
                    self.ACTION.D2()
                    self.ACTION.R1()
            elif angel == "F7D1L9":
                if self.threeFaceBlocks[angel][0] == color1:
                    self.ACTION.D1()
                    self.ACTION.R2()
                    self.ACTION.D2()
                    self.ACTION.D2()
                    self.ACTION.R1()
                    self.ACTION.D1()
                    self.ACTION.R2()
                    self.ACTION.D2()
                    self.ACTION.R1()
                elif self.threeFaceBlocks[angel][0] == color2:
                    self.ACTION.D1()
                    self.ACTION.R2()
                    self.ACTION.D2()
                    self.ACTION.R1()
                else:
                    self.ACTION.R2()
                    self.ACTION.D1()
                    self.ACTION.R1()
            elif angel == "F9D3R7":
                if self.threeFaceBlocks[angel][0] == color1:
                    self.ACTION.R2()
                    self.ACTION.D2()
                    self.ACTION.R1()
                elif self.threeFaceBlocks[angel][0] == color2:
                    self.ACTION.D2()
                    self.ACTION.R2()
                    self.ACTION.D1()
                    self.ACTION.R1()
                else:
                    self.ACTION.R2()
                    self.ACTION.D2()
                    self.ACTION.D2()
                    self.ACTION.R1()
                    self.ACTION.D1()
                    self.ACTION.R2()
                    self.ACTION.D2()
                    self.ACTION.R1()
            elif angel == "B1U3R3":
                if self.threeFaceBlocks[angel][0] == color1:
                    self.ACTION.B2()
                    self.ACTION.D2()
                    self.ACTION.B1()
                    self.ACTION.R2()
                    self.ACTION.D2()
                    self.ACTION.D2()
                    self.ACTION.R1()
                    self.ACTION.D1()
                    self.ACTION.R2()
                    self.ACTION.D2()
                    self.ACTION.R1()
                elif self.threeFaceBlocks[angel][0] == color2:
                    self.ACTION.B2()
                    self.ACTION.D2()
                    self.ACTION.B1()
                    self.ACTION.R2()
                    self.ACTION.D2()
                    self.ACTION.R1()
                else:
                    self.ACTION.B2()
                    self.ACTION.D2()
                    self.ACTION.B1()
                    self.ACTION.D2()
                    self.ACTION.R2()
                    self.ACTION.D1()
                    self.ACTION.R1()
            elif angel ==  "B3U1L1":
                if self.threeFaceBlocks[angel][0] == color1:
                    self.ACTION.B1()
                    self.ACTION.D1()
                    self.ACTION.B2()
                    self.ACTION.D1()
                    self.ACTION.R2()
                    self.ACTION.D2()
                    self.ACTION.R1()
                elif self.threeFaceBlocks[angel][0] == color2:
                    self.ACTION.B1()
                    self.ACTION.D1()
                    self.ACTION.B2()
                    self.ACTION.R2()
                    self.ACTION.D1()
                    self.ACTION.R1()
                else:
                    self.ACTION.B1()
                    self.ACTION.D1()
                    self.ACTION.B2()
                    self.ACTION.D1()
                    self.ACTION.R2()
                    self.ACTION.D2()
                    self.ACTION.D2()
                    self.ACTION.R1()
                    self.ACTION.D1()
                    self.ACTION.R2()
                    self.ACTION.D2()
                    self.ACTION.R1()
            elif angel == "B7D9R9":
                if self.threeFaceBlocks[angel][0] == color1:
                    self.ACTION.D2()
                    self.ACTION.R2()
                    self.ACTION.D2()
                    self.ACTION.D2()
                    self.ACTION.R1()
                    self.ACTION.D1()
                    self.ACTION.R2()
                    self.ACTION.D2()
                    self.ACTION.R1()
                elif self.threeFaceBlocks[angel][0] == color2:
                    self.ACTION.D2()
                    self.ACTION.R2()
                    self.ACTION.D2()
                    self.ACTION.R1()
                else:
                    self.ACTION.D2()
                    self.ACTION.D2()
                    self.ACTION.R2()
                    self.ACTION.D1()
                    self.ACTION.R1()

            elif angel == "B9D7L7":
                if self.threeFaceBlocks[angel][0] == color1:
                    self.ACTION.D1()
                    self.ACTION.D1()
                    self.ACTION.R2()
                    self.ACTION.D2()
                    self.ACTION.R1()
                elif self.threeFaceBlocks[angel][0] == color2:
                    self.ACTION.D1()
                    self.ACTION.R2()
                    self.ACTION.D1()
                    self.ACTION.R1()
                else:
                    self.ACTION.D1()
                    self.ACTION.D1()
                    self.ACTION.R2()
                    self.ACTION.D2()
                    self.ACTION.D2()
                    self.ACTION.R1()
                    self.ACTION.D1()
                    self.ACTION.R2()
                    self.ACTION.D2()
                    self.ACTION.R1()
        self.ACTION.Y()
    def getAngle(self,color1,color2,color3):
        for angle in self.threeFaceBlocks.keys():
            c1 = self.threeFaceBlocks[angle][0] == color1 and self.threeFaceBlocks[angle][1] == color2 and self.threeFaceBlocks[angle][2] == color3
            c2 = self.threeFaceBlocks[angle][0] == color1 and self.threeFaceBlocks[angle][2] == color2 and self.threeFaceBlocks[angle][1] == color3
            c3 = self.threeFaceBlocks[angle][1] == color1 and self.threeFaceBlocks[angle][0] == color2 and self.threeFaceBlocks[angle][2] == color3
            c4 = self.threeFaceBlocks[angle][1] == color1 and self.threeFaceBlocks[angle][2] == color2 and self.threeFaceBlocks[angle][0] == color3
            c5 = self.threeFaceBlocks[angle][2] == color1 and self.threeFaceBlocks[angle][1] == color2 and self.threeFaceBlocks[angle][0] == color3
            c6 = self.threeFaceBlocks[angle][2] == color1 and self.threeFaceBlocks[angle][0] == color2 and self.threeFaceBlocks[angle][1] == color3
            if c1 or c2 or c3 or c4 or c5 or c6:
                return angle
    def return2ndRow(self):
        self.makeTopTwoFace()
        self.makeTwoBlocks()
        face = 0
        while face < 4:
            turn = 0
            while turn < 4:
                if (self.ACTION.f[1][2] == self.ACTION.r[1][1]) and (self.ACTION.r[1][0] == self.ACTION.f[1][1]):
                    self.ACTION.R1()
                    self.ACTION.U1()
                    self.ACTION.U1()
                    self.ACTION.R2()
                    self.ACTION.U1()
                    self.ACTION.R1()
                    self.ACTION.U1()
                    self.ACTION.U1()
                    self.ACTION.R2()
                    self.ACTION.U1()
                    self.ACTION.F2()
                    self.ACTION.U2()
                    self.ACTION.F1()
                    self.makeTwoBlocks()
                    self.makeTopTwoFace()
                    break
                elif (self.ACTION.f[1][2] != self.ACTION.f[1][1]) or (self.ACTION.r[1][1] != self.ACTION.r[1][0]):
                    block = self.get2ndBlock(self.ACTION.f[1][1],self.ACTION.r[1][1])
                    if block != None:
                        self.return2ndBlock(block)
                        self.makeTwoBlocks()
                        self.makeTopTwoFace()
                        break
                    else:
                        self.ACTION.Y()
                        self.makeTwoBlocks()
                        self.makeTopTwoFace()
                        turn+=1
                else:
                    self.ACTION.Y()
                    self.makeTwoBlocks()
                    self.makeTopTwoFace()
                    turn += 1
            if turn == 4:

                self.ACTION.U1()
                self.ACTION.R1()
                self.ACTION.U2()
                self.ACTION.R2()
                self.ACTION.U2()
                self.ACTION.F2()
                self.ACTION.U1()
                self.ACTION.F1()

                self.makeTwoBlocks()
                self.makeTopTwoFace()
            else:
                face += 1
                self.ACTION.Y()
                self.makeTwoBlocks()
                self.makeTopTwoFace()
        # self.ACTION.printCube()
    def return2ndBlock(self,block):
            if block == "F2U8":
                if self.TopTwoFace[block][0] == self.ACTION.f[1][1]:
                    self.ACTION.U1()
                    self.ACTION.R1()
                    self.ACTION.U2()
                    self.ACTION.R2()
                    self.ACTION.U2()
                    self.ACTION.F2()
                    self.ACTION.U1()
                    self.ACTION.F1()
                else:
                    self.ACTION.U1()
                    self.ACTION.U1()
                    self.ACTION.F2()
                    self.ACTION.U1()
                    self.ACTION.F1()
                    self.ACTION.U1()
                    self.ACTION.R1()
                    self.ACTION.U2()
                    self.ACTION.R2()
            if block == "B2U2":
                if self.TopTwoFace[block][0] == self.ACTION.f[1][1]:
                    self.ACTION.U2()
                    self.ACTION.R1()
                    self.ACTION.U2()
                    self.ACTION.R2()
                    self.ACTION.U2()
                    self.ACTION.F2()
                    self.ACTION.U1()
                    self.ACTION.F1()
                else:
                    self.ACTION.F2()
                    self.ACTION.U1()
                    self.ACTION.F1()
                    self.ACTION.U1()
                    self.ACTION.R1()
                    self.ACTION.U2()
                    self.ACTION.R2()
            if block == "R2U6":
                if self.TopTwoFace[block][0] == self.ACTION.f[1][1]:
                    self.ACTION.U1()
                    self.ACTION.U1()
                    self.ACTION.R1()
                    self.ACTION.U2()
                    self.ACTION.R2()
                    self.ACTION.U2()
                    self.ACTION.F2()
                    self.ACTION.U1()
                    self.ACTION.F1()
                else:
                    self.ACTION.U2()
                    self.ACTION.F2()
                    self.ACTION.U1()
                    self.ACTION.F1()
                    self.ACTION.U1()
                    self.ACTION.R1()
                    self.ACTION.U2()
                    self.ACTION.R2()
            if block == "L2U4":
                if self.TopTwoFace[block][0] == self.ACTION.f[1][1]:
                    self.ACTION.R1()
                    self.ACTION.U2()
                    self.ACTION.R2()
                    self.ACTION.U2()
                    self.ACTION.F2()
                    self.ACTION.U1()
                    self.ACTION.F1()
                else:
                    self.ACTION.U1()
                    self.ACTION.F2()
                    self.ACTION.U1()
                    self.ACTION.F1()
                    self.ACTION.U1()
                    self.ACTION.R1()
                    self.ACTION.U2()
                    self.ACTION.R2()
    def get2ndBlock(self,color1,color2):
        for block in self.TopTwoFace.keys():
            if (self.TopTwoFace[block][0] == color1 and self.TopTwoFace[block][1] == color2) or (self.TopTwoFace[block][0] == color2 and self.TopTwoFace[block][1] == color1):
                return block
        else:
            return None
    def returnTopPlus(self):
        block2 = self.ACTION.u[0][1]== self.ACTION.u[1][1]
        block4 = self.ACTION.u[1][0]== self.ACTION.u[1][1]
        block6 = self.ACTION.u[1][2]== self.ACTION.u[1][1]
        block8 = self.ACTION.u[2][1]== self.ACTION.u[1][1]
        if (not block2) and (not block4) and (not block6) and (not block8):
            self.ACTION.F1()
            self.ACTION.R1()
            self.ACTION.U1()
            self.ACTION.R2()
            self.ACTION.U2()
            self.ACTION.F2()
            self.ACTION.U2()
            self.ACTION.U2()
            self.ACTION.F1()
            self.ACTION.R1()
            self.ACTION.U1()
            self.ACTION.R2()
            self.ACTION.U2()
            self.ACTION.R1()
            self.ACTION.U1()
            self.ACTION.R2()
            self.ACTION.U2()
            self.ACTION.F2()
        elif not (block2 and block4 and block6 and block8) :
            if self.ACTION.u[0][1] == self.ACTION.u[1][0] == self.ACTION.u[1][1]:
                self.ACTION.F1()
                self.ACTION.R1()
                self.ACTION.U1()
                self.ACTION.R2()
                self.ACTION.U2()
                self.ACTION.R1()
                self.ACTION.U1()
                self.ACTION.R2()
                self.ACTION.U2()
                self.ACTION.F2()
            elif self.ACTION.u[1][0] == self.ACTION.u[2][1] == self.ACTION.u[1][1]:
                self.ACTION.U1()
                self.ACTION.F1()
                self.ACTION.R1()
                self.ACTION.U1()
                self.ACTION.R2()
                self.ACTION.U2()
                self.ACTION.R1()
                self.ACTION.U1()
                self.ACTION.R2()
                self.ACTION.U2()
                self.ACTION.F2()
            elif self.ACTION.u[2][1] == self.ACTION.u[1][2] == self.ACTION.u[1][1]:
                self.ACTION.U1()
                self.ACTION.U1()
                self.ACTION.F1()
                self.ACTION.R1()
                self.ACTION.U1()
                self.ACTION.R2()
                self.ACTION.U2()
                self.ACTION.R1()
                self.ACTION.U1()
                self.ACTION.R2()
                self.ACTION.U2()
                self.ACTION.F2()
            elif self.ACTION.u[0][1] == self.ACTION.u[1][2] == self.ACTION.u[1][1]:
                self.ACTION.U2()
                self.ACTION.F1()
                self.ACTION.R1()
                self.ACTION.U1()
                self.ACTION.R2()
                self.ACTION.U2()
                self.ACTION.R1()
                self.ACTION.U1()
                self.ACTION.R2()
                self.ACTION.U2()
                self.ACTION.F2()
            elif self.ACTION.u[0][1] == self.ACTION.u[1][1] == self.ACTION.u[1][1]:
                self.ACTION.U1()
                self.ACTION.F1()
                self.ACTION.R1()
                self.ACTION.U1()
                self.ACTION.R2()
                self.ACTION.U2()
                self.ACTION.F2()
            elif self.ACTION.u[1][1] == self.ACTION.u[1][2] == self.ACTION.u[1][0]:
                self.ACTION.F1()
                self.ACTION.R1()
                self.ACTION.U1()
                self.ACTION.R2()
                self.ACTION.U2()
                self.ACTION.F2()
            else:
                pass
    def returnTop(self):
        while True:
            self.makeTopAngel()
            nums = 0
            for angel in self.TopAngel.keys():
                if self.TopAngel[angel][1] == self.ACTION.u[1][1]:
                    nums+=1
            if nums == 4:
                break
            elif nums == 2:
                if self.ACTION.u[2][2] != self.ACTION.u[1][1]:
                    self.ACTION.U1()
                    self.ACTION.R1()
                    self.ACTION.U2()
                    self.ACTION.L2()
                    self.ACTION.U1()
                    self.ACTION.R2()
                    self.ACTION.U2()
                    self.ACTION.L1()
                elif self.ACTION.u[2][0] != self.ACTION.u[1][1]:
                    self.ACTION.R1()
                    self.ACTION.U2()
                    self.ACTION.L2()
                    self.ACTION.U1()
                    self.ACTION.R2()
                    self.ACTION.U2()
                    self.ACTION.L1()
                elif self.ACTION.u[0][0] != self.ACTION.u[1][1]:
                    self.ACTION.U2()
                    self.ACTION.R1()
                    self.ACTION.U2()
                    self.ACTION.L2()
                    self.ACTION.U1()
                    self.ACTION.R2()
                    self.ACTION.U2()
                    self.ACTION.L1()
            elif nums == 1:
                if self.ACTION.u[2][0] == self.ACTION.u[1][1]:
                    if self.ACTION.f[0][2] == self.ACTION.u[1][1]:
                        self.ACTION.R1()
                        self.ACTION.U1()
                        self.ACTION.R2()
                        self.ACTION.U1()
                        self.ACTION.R1()
                        self.ACTION.U1()
                        self.ACTION.U1()
                        self.ACTION.R2()
                    else:
                        self.ACTION.U1()
                        self.ACTION.R2()
                        self.ACTION.U2()
                        self.ACTION.R1()
                        self.ACTION.U2()
                        self.ACTION.R2()
                        self.ACTION.U1()
                        self.ACTION.U1()
                        self.ACTION.R1()
                        pass
                elif self.ACTION.u[0][0] == self.ACTION.u[1][1]:
                    if self.ACTION.l[0][2] == self.ACTION.u[1][1]:
                        self.ACTION.U2()
                        self.ACTION.R1()
                        self.ACTION.U1()
                        self.ACTION.R2()
                        self.ACTION.U1()
                        self.ACTION.R1()
                        self.ACTION.U1()
                        self.ACTION.U1()
                        self.ACTION.R2()
                    else:
                        self.ACTION.R2()
                        self.ACTION.U2()
                        self.ACTION.R1()
                        self.ACTION.U2()
                        self.ACTION.R2()
                        self.ACTION.U1()
                        self.ACTION.U1()
                        self.ACTION.R1()
                elif self.ACTION.u[0][2] == self.ACTION.u[1][1]:
                    if self.ACTION.b[0][2] == self.ACTION.u[1][1]:
                        self.ACTION.U1()
                        self.ACTION.U1()
                        self.ACTION.R1()
                        self.ACTION.U1()
                        self.ACTION.R2()
                        self.ACTION.U1()
                        self.ACTION.R1()
                        self.ACTION.U1()
                        self.ACTION.U1()
                        self.ACTION.R2()
                    else:
                        self.ACTION.U2()
                        self.ACTION.R2()
                        self.ACTION.U2()
                        self.ACTION.R1()
                        self.ACTION.U2()
                        self.ACTION.R2()
                        self.ACTION.U1()
                        self.ACTION.U1()
                        self.ACTION.R1()
                elif self.ACTION.u[2][2] == self.ACTION.u[1][1]:
                    if self.ACTION.r[0][2] == self.ACTION.u[1][1]:
                        self.ACTION.U1()
                        self.ACTION.R1()
                        self.ACTION.U1()
                        self.ACTION.R2()
                        self.ACTION.U1()
                        self.ACTION.R1()
                        self.ACTION.U1()
                        self.ACTION.U1()
                        self.ACTION.R2()
                    else:
                        self.ACTION.U1()
                        self.ACTION.U1()
                        self.ACTION.R2()
                        self.ACTION.U2()
                        self.ACTION.R1()
                        self.ACTION.U2()
                        self.ACTION.R2()
                        self.ACTION.U1()
                        self.ACTION.U1()
                        self.ACTION.R1()
            else:
                self.ACTION.U1()
                self.ACTION.R1()
                self.ACTION.U2()
                self.ACTION.L2()
                self.ACTION.U1()
                self.ACTION.R2()
                self.ACTION.U2()
                self.ACTION.L1()
    def returnTop2(self):
        while True:
            self.makeTopBlock()
            cList = []
            for color in self.TopBlock.keys():
                if self.TopBlock[color][0] == self.TopBlock[color][2]:
                    cList.append(color)
            if len(cList) <3 and len(cList) != 0:
                if cList[0] == "F":
                    if self.TopBlock["F"][0] == self.ACTION.f[1][1]:
                        self.ACTION.U2()
                    elif self.TopBlock["F"][0] == self.ACTION.l[1][1]:
                        self.ACTION.Z()
                    elif self.TopBlock["F"][0] == self.ACTION.b[1][1]:
                        self.ACTION.U1()
                        self.ACTION.Y()
                        self.ACTION.Y()
                    elif self.TopBlock["F"][0] == self.ACTION.r[1][1]:
                        self.ACTION.U1()
                        self.ACTION.U1()
                        self.ACTION.Y()
                elif cList[0] == "R":
                    if self.TopBlock["R"][0] == self.ACTION.f[1][1]:
                        pass
                    elif self.TopBlock["R"][0] == self.ACTION.l[1][1]:
                        self.ACTION.U1()
                        self.ACTION.Z()
                    elif self.TopBlock["R"][0] == self.ACTION.b[1][1]:
                        self.ACTION.U1()
                        self.ACTION.U1()
                        self.ACTION.Y()
                        self.ACTION.Y()
                    elif self.TopBlock["R"][0] == self.ACTION.r[1][1]:
                        self.ACTION.U2()
                        self.ACTION.Y()
                elif cList[0] == "L":
                    if self.TopBlock["L"][0] == self.ACTION.f[1][1]:
                        self.ACTION.U1()
                        self.ACTION.U1()
                    elif self.TopBlock["L"][0] == self.ACTION.l[1][1]:
                        self.ACTION.U2()
                        self.ACTION.Z()
                    elif self.TopBlock["L"][0] == self.ACTION.b[1][1]:
                        self.ACTION.Y()
                        self.ACTION.Y()
                    elif self.TopBlock["L"][0] == self.ACTION.r[1][1]:
                        self.ACTION.U1()
                        self.ACTION.Y()
                elif cList[0] == "R":
                    if self.TopBlock["R"][0] == self.ACTION.f[1][1]:
                        self.ACTION.U1()
                    elif self.TopBlock["R"][0] == self.ACTION.l[1][1]:
                        self.ACTION.U1()
                        self.ACTION.U1()
                        self.ACTION.Z()
                    elif self.TopBlock["R"][0] == self.ACTION.b[1][1]:
                        self.ACTION.U2()
                        self.ACTION.Y()
                        self.ACTION.Y()
                    elif self.TopBlock["R"][0] == self.ACTION.r[1][1]:
                        self.ACTION.Y()
            if len(cList) == 4:
                break
            self.ACTION.R1()
            self.ACTION.R1()
            self.ACTION.F1()
            self.ACTION.F1()
            self.ACTION.R2()
            self.ACTION.B2()
            self.ACTION.R1()
            self.ACTION.F1()
            self.ACTION.F1()
            self.ACTION.R2()
            self.ACTION.B1()
            self.ACTION.R2()
    def done(self):
        while True:
            self.makeTopBlock()
            cList = []
            for color in self.TopBlock.keys():
                if self.TopBlock[color][0] == self.TopBlock[color][1] and self.TopBlock[color][1]  == self.TopBlock[color][2]:
                    cList.append(color)
            self.makeTopBlock()
            if len(cList) == 1:
                if cList[0] == "F":
                    if self.TopBlock["F"][0] == self.ACTION.f[1][1]:
                        self.ACTION.Y()
                        self.ACTION.Y()
                    elif self.TopBlock["F"][0] == self.ACTION.r[1][1]:
                        self.ACTION.U2()
                        self.ACTION.Z()
                    elif self.TopBlock["F"][0] == self.ACTION.l[1][1]:
                        self.ACTION.U1()
                        self.ACTION.Y()
                    elif self.TopBlock["F"][0] == self.ACTION.b[1][1]:
                        self.ACTION.U1()
                        self.ACTION.U1()
                elif cList[0] == "R":
                    if self.TopBlock["R"][0] == self.ACTION.f[1][1]:
                        self.ACTION.U1()
                        self.ACTION.Y()
                        self.ACTION.Y()
                    elif self.TopBlock["R"][0] == self.ACTION.r[1][1]:
                        self.ACTION.Z()
                    elif self.TopBlock["R"][0] == self.ACTION.l[1][1]:
                        self.ACTION.U1()
                        self.ACTION.U1()
                        self.ACTION.Y()
                    elif self.TopBlock["R"][0] == self.ACTION.b[1][1]:
                        self.ACTION.U2()
                elif cList[0] == "L":
                    if self.TopBlock["L"][0] == self.ACTION.f[1][1]:
                        self.ACTION.U2()
                        self.ACTION.Y()
                        self.ACTION.Y()
                    elif self.TopBlock["L"][0] == self.ACTION.r[1][1]:
                        self.ACTION.U1()
                        self.ACTION.U1()
                        self.ACTION.Z()
                    elif self.TopBlock["L"][0] == self.ACTION.l[1][1]:
                        self.ACTION.Y()
                    elif self.TopBlock["L"][0] == self.ACTION.b[1][1]:
                        self.ACTION.U1()
                elif cList[0] == "B":
                    if self.TopBlock["B"][0] == self.ACTION.f[1][1]:
                        self.ACTION.U1()
                        self.ACTION.U1()
                        self.ACTION.Y()
                        self.ACTION.Y()
                    elif self.TopBlock["B"][0] == self.ACTION.r[1][1]:
                        self.ACTION.U1()
                        self.ACTION.Z()
                    elif self.TopBlock["B"][0] == self.ACTION.l[1][1]:
                        self.ACTION.U1()
                        self.ACTION.Y()
                    elif self.TopBlock["B"][0] == self.ACTION.b[1][1]:
                        pass
                self.makeTopBlock()
                if self.ACTION.r[0][1] == self.ACTION.l[1][1]:
                    self.ACTION.R1()
                    self.ACTION.U2()
                    self.ACTION.R1()
                    self.ACTION.U1()
                    self.ACTION.R1()
                    self.ACTION.U1()
                    self.ACTION.R1()
                    self.ACTION.U2()
                    self.ACTION.R2()
                    self.ACTION.U2()
                    self.ACTION.R1()
                    self.ACTION.R1()
                else:
                    self.ACTION.L2()
                    self.ACTION.U1()
                    self.ACTION.L2()
                    self.ACTION.U2()
                    self.ACTION.L2()
                    self.ACTION.U2()
                    self.ACTION.L2()
                    self.ACTION.U1()
                    self.ACTION.L1()
                    self.ACTION.U1()
                    self.ACTION.L2()
                    self.ACTION.L2()
            elif len(cList) == 4:
                break
            else:
                self.ACTION.L2()
                self.ACTION.U1()
                self.ACTION.L2()
                self.ACTION.U2()
                self.ACTION.L2()
                self.ACTION.U2()
                self.ACTION.L2()
                self.ACTION.U1()
                self.ACTION.L1()
                self.ACTION.U1()
                self.ACTION.L2()
                self.ACTION.L2()