import cv2
import numpy as np
import threading
import ReturnToBefor
import configparser
import os
cap = cv2.VideoCapture(0)
_, frame = cap.read()
height, width, _ = frame.shape

square_size_factor = 0.5  # 正方形が占める画像の高さの割合
square_x1 = int((width - ((square_size_factor) * height)) / 2)  # 四角の座標を計算する
square_x2 = int((width + ((square_size_factor) * height)) / 2)

square_y1 = int(((1 - square_size_factor) / 2) * height)
square_y2 = int(((1 + square_size_factor) / 2) * height)
#色のRBGデータ
BLUE = (255, 0, 0)
YELLOW = (0, 255, 255)
ORANGE = (0, 165, 255)
GREEN = (0, 128, 0)
RED = (0, 0, 255)
WHITE =(255, 255, 255)
BLACK = (0, 0, 0)
COLORD = {'#008000': GREEN, '#0000FF':BLUE,'#FFFF00':YELLOW,'#FFA500':ORANGE,'#FF0000':RED,'#FFFFFF':WHITE,'#000000':BLACK}
COLORDD = {"green": GREEN, "blue":BLUE,"yellow":YELLOW,"orange":ORANGE,"red":RED,"white":WHITE,"black":BLACK}

cube_dimension = square_y2 - square_y1  # キューブの高さと幅（ピクセル単位）
red_minhsv = []
red_maxhsv = []
orange_minhsv = []
orange_maxhsv = []
white_minhsv = []
white_maxhsv = []
yellow_minhsv = []
yellow_maxhsv = []
green_minhsv = []
green_maxhsv = []
blue_minhsv = []
blue_maxhsv = []
color = {'red': [red_maxhsv, red_minhsv], 'orange': [orange_maxhsv, orange_minhsv],
         'white': [white_maxhsv, white_minhsv], 'yellow': [yellow_maxhsv, yellow_minhsv],
         'green': [green_maxhsv, green_minhsv], 'blue': [blue_maxhsv, blue_minhsv]}
#ローカルの色の情報を読み込む
curpath = os.path.dirname(os.path.realpath(__file__))
cfgpath = os.path.join(curpath, "Color.ini")
conf = configparser.ConfigParser()
conf.read(cfgpath, encoding="utf-8")

for col in color.keys():
    items = conf.items(col)
    color[col][0].append(int(items[0][1]))
    color[col][0].append(int(items[2][1]))
    color[col][0].append(int(items[4][1]))
    color[col][1].append(int(items[1][1]))
    color[col][1].append(int(items[3][1]))
    color[col][1].append(int(items[5][1]))

cube = []
#カメラからの画像を読み込み、キューブの色のパラメータを認識する
def find_avg_hsv(img):
    #中心の正方形だけを読み込み
    tile_dimension = int(cube_dimension / 3)
    tile_factor = 0.3
    tile_roi_start = int(((1 - tile_factor) / 2) * tile_dimension)
    tile_roi_end = int(
        (tile_dimension * tile_factor) + tile_roi_start)

    tile_roi = []  # ブロックの色のパラメータを持つリストを作る
    for j in range(3):
        row = []
        for i in range(3):
            row.append(img[(j * tile_dimension) + tile_roi_start:(j * tile_dimension) + tile_roi_end,
                       (i * tile_dimension) + tile_roi_start:(i * tile_dimension) + tile_roi_end])
            cv2.rectangle(img, ((i * tile_dimension) + tile_roi_start, (j * tile_dimension) + tile_roi_start),
                          ((i * tile_dimension) + tile_roi_end, (j * tile_dimension) + tile_roi_end), (255, 0, 0),
                          1)
        tile_roi.append(row)
    cv2.namedWindow("check")
    cv2.moveWindow("check", 40, 30)
    cv2.imshow("check", img)
    hsv_avg = []
    #各ブロックの情報を読み込み、色を認識する
    for row_iterable in tile_roi:
        row = []
        for col_iterable in row_iterable:
            b_avg, g_avg, r_avg, _ = np.uint8(cv2.mean(col_iterable))
            color = cv2.cvtColor(np.uint8([[[b_avg, g_avg, r_avg]]]),
                                 cv2.COLOR_BGR2LAB)
            h_avg = color[0][0][0]
            s_avg = color[0][0][1]
            v_avg = color[0][0][2]

            row.append([h_avg, s_avg, v_avg])
        #認識された色のパラメータを戻す
        hsv_avg.append(row)

    return hsv_avg
#カメラの中心に正方形を描く
def drawGrid(img, height, width, up, down, left, right):
    leftX = int (width / 2 - height / 4)
    upperY = int (height / 4)
    rightX = int (width / 2 + height / 4)
    lowerY = int (3 * height / 4)
    firstSplitX = int (width / 2 - height / 12)
    secondSplitX = int (width / 2 + height / 12)
    firstSplitY = int (5 * height / 12)
    secondSplitY = int (7 * height / 12)
    #正方形を3*3で分ける
    cv2.line(img, (leftX, upperY),  (rightX, upperY), BLACK)
    cv2.line(img, (leftX, upperY),  (leftX, lowerY), BLACK)
    cv2.line(img, (rightX, lowerY),  (rightX, upperY), BLACK)
    cv2.line(img, (firstSplitX, upperY),  (firstSplitX, lowerY), BLACK)
    cv2.line(img, (secondSplitX, lowerY),  (secondSplitX, upperY), BLACK)
    cv2.line(img, (leftX, firstSplitY),  (rightX, firstSplitY), BLACK)
    cv2.line(img, (leftX, secondSplitY),  (rightX, secondSplitY), BLACK)
    cv2.line(img, (leftX, lowerY),  (rightX, lowerY), BLACK)
    #正方形に認識すべきキューブの面の情報を載せる
    cv2.putText(img,"U", (310, int (height / 6)), cv2.FONT_HERSHEY_COMPLEX, 1, COLORDD[up], 3)
    cv2.putText(img, "D", (310, int (5 * height / 6)), cv2.FONT_HERSHEY_COMPLEX, 1,COLORDD[down] , 3)
    cv2.putText(img, "L", (int (width / 2 - 5 * height / 14), int (6.4 * height / 12)), cv2.FONT_HERSHEY_COMPLEX, 1, COLORDD[left], 3)
    cv2.putText(img, "R", (int (width / 2 + 9 * height / 32), int (6.4 * height / 12)), cv2.FONT_HERSHEY_COMPLEX, 1, COLORDD[right], 3)
#キューブの色を認識する
def captureFace(cap, fHeight, fWidth, color, up, down, left, right,Gcolor):
    while True:
        ret, frame = cap.read()#カメラオン
        cv2.putText(frame,"[   ]", (282, int (6.4 * height / 12)), cv2.FONT_HERSHEY_COMPLEX, 1, Gcolor, 3)
        drawGrid(frame, fHeight, fWidth, up, down, left, right)
        cv2.imshow("Cube", frame)
        k = cv2.waitKey(1) & 0xff
        if k == 32:#spaceキーを押すと、今のキューブの写真を撮る
            face = []
            cube_roi = frame[square_y1:square_y2, square_x1:square_x2]

            cubeface = find_avg_hsv(cube_roi)
            #取ってきた色のパラメータに対応する色を探す
            for row in cubeface:
                crow = []
                for edge in row:
                    cedge = '#000000'
                    if (red_minhsv[0] <= edge[0] <= red_maxhsv[0]) and (red_minhsv[1] <= edge[1] <= red_maxhsv[1]) and (
                            red_minhsv[2] <= edge[2] <= red_maxhsv[2]):
                        cedge = '#FF0000'
                    elif (orange_minhsv[0] <= edge[0] <= orange_maxhsv[0]) and (
                            orange_minhsv[1] <= edge[1] <= orange_maxhsv[1]) and (
                            orange_minhsv[2] <= edge[2] <= orange_maxhsv[2]):
                        cedge = '#FFA500'
                    elif (blue_minhsv[0] <= edge[0] <= blue_maxhsv[0]) and (
                            blue_minhsv[1] <= edge[1] <= blue_maxhsv[1]) and (
                            blue_minhsv[2] <= edge[2] <= blue_maxhsv[2]):
                        cedge = '#0000FF'
                    elif (yellow_minhsv[0] <= edge[0] <= yellow_maxhsv[0]) and (
                            yellow_minhsv[1] <= edge[1] <= yellow_maxhsv[1]) and (
                            yellow_minhsv[2] <= edge[2] <= yellow_maxhsv[2]):
                        cedge = '#FFFF00'
                    elif (white_minhsv[0] <= edge[0] <= white_maxhsv[0]) and (
                            white_minhsv[1] <= edge[1] <= white_maxhsv[1]) and (
                            white_minhsv[2] <= edge[2] <= white_maxhsv[2]):
                        cedge = '#FFFFFF'
                    elif (green_minhsv[0] <= edge[0] <= green_maxhsv[0]) and (
                            green_minhsv[1] <= edge[1] <= green_maxhsv[1]) and (
                            green_minhsv[2] <= edge[2] <= green_maxhsv[2]):
                        cedge = '#008000'
                    crow.append(cedge)
                face.append(crow)
            zimg = np.zeros((150, 150, 3), np.uint8)
            zimg.fill(255)
            font = cv2.FONT_HERSHEY_SIMPLEX
            rindex = 0
            for row in face:
                index = 0
                for edge in row:
                    #色を確認するための画像を作る
                    cv2.rectangle(zimg, (50*index, 50*rindex), (50*(index+1), 50*(rindex+1)),COLORD[edge], -1)
                    index += 1
                rindex +=1
            cv2.imshow('image', zimg)
            #もし、プログラムで認識した色がキューブの色と合っている場合、nキーを押すと、次の面の色の情報を取りにいく
        elif k == ord('n'):
            try:
                cube.append(face)
                break
            except:
                pass
#キューブの六面の色の情報を認識する
def recognizeFaces(n):
    scanning = True
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("video input not found")
    fWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    fHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    captureFace(cap, fHeight, fWidth, "green", "yellow", "white", "red", "orange",GREEN)
    captureFace(cap, fHeight, fWidth, "red", "yellow", "white", "blue", "green",RED)
    captureFace(cap, fHeight, fWidth, "blue", "yellow", "white", "orange", "red",BLUE)
    captureFace(cap, fHeight, fWidth, "orange", "yellow", "white", "green", "blue",ORANGE)
    captureFace(cap, fHeight, fWidth, "yellow", "blue", "green", "red", "orange",YELLOW)
    captureFace(cap, fHeight, fWidth, "white", "green", "blue", "red", "orange",WHITE)
    #六面全部認識できたら、カメラを閉じる
    cap.release()
    cv2.destroyAllWindows()

t1 = threading.Thread(target=recognizeFaces,args=('t1',))
t1.start()
t1.join()
#キューブの揃うプロセスが始まり
#実際にReturnToBefor.pyでプロセスが進む
RETURN = ReturnToBefor.Return(cube)
RETURN.return1stFace()
RETURN.return1stFace1()
RETURN.return2ndRow()
RETURN.returnTopPlus()
RETURN.returnTop()
RETURN.returnTop2()
RETURN.done()
RETURN.ACTION.printCube()
