import cv2
import numpy as np
import configparser
import os

cap = cv2.VideoCapture(0)
_, frame = cap.read()
height, width, _ = frame.shape

square_size_factor = 0.4
square_x1 = int((width - ((square_size_factor) * height)) / 2)
square_x2 = int((width + ((square_size_factor) * height)) / 2)

square_y1 = int(((1 - square_size_factor) / 2) * height)
square_y2 = int(((1 + square_size_factor) / 2) * height)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
cube_dimension = square_y2 - square_y1
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

cube = []
def find_avg_hsv(
        img):

    tile_dimension = int(cube_dimension / 3)
    tile_factor = 0.3
    tile_roi_start = int(((1 - tile_factor) / 2) * tile_dimension)
    tile_roi_end = int(
        (tile_dimension * tile_factor) + tile_roi_start)

    tile_roi = []
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
    for row_iterable in tile_roi:
        row = []
        bgr_row = []
        for col_iterable in row_iterable:
            b_avg, g_avg, r_avg, _ = np.uint8(cv2.mean(col_iterable))
            color = cv2.cvtColor(np.uint8([[[b_avg, g_avg, r_avg]]]),
                                 cv2.COLOR_BGR2LAB)
            h_avg = color[0][0][0]
            s_avg = color[0][0][1]
            v_avg = color[0][0][2]

            row.append([h_avg, s_avg, v_avg])
        hsv_avg.append(row)

    return hsv_avg

while True:
    _, frame = cap.read()

    cv2.rectangle(frame, (square_x1, square_y1), (square_x2, square_y2), (255, 0, 0),
                  2)

    cv2.imshow("original", frame)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
    elif k == 32:
        print("Image Captured")

        cube_roi = frame[square_y1:square_y2, square_x1:square_x2]

        cubeface = find_avg_hsv(cube_roi)
        setColor = 'orange'
        for row in cubeface:

            for edge in  row:
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
                if edge[0] < color[setColor][1][0]:
                    conf.set(setColor, "v1min", str(edge[0]))  # 写入中文
                    conf.write(open(cfgpath, "r+", encoding="utf-8"))  # r+模式
                    print(setColor + "のデータを更新した")
                if edge[0] >  color[setColor][0][0]:
                    conf.set(setColor, "v1max", str(edge[0]))  # 写入中文
                    conf.write(open(cfgpath, "r+", encoding="utf-8"))  # r+模式
                    print(setColor + "のデータを更新した")
                if edge[1] <  color[setColor][1][1]:
                    conf.set(setColor, "v2min", str(edge[1]))  # 写入中文
                    conf.write(open(cfgpath, "r+", encoding="utf-8"))  # r+模式
                    print(setColor + "のデータを更新した")
                if edge[1] >  color[setColor][0][1]:
                    conf.set(setColor, "v2max", str(edge[1]))  # 写入中文
                    conf.write(open(cfgpath, "r+", encoding="utf-8"))  # r+模式
                    print(setColor + "のデータを更新した")
                if edge[2] <  color[setColor][1][2]:
                    conf.set(setColor, "v3min", str(edge[2]))  # 写入中文
                    conf.write(open(cfgpath, "r+", encoding="utf-8"))  # r+模式
                    print(setColor + "のデータを更新した")
                if edge[2] >  color[setColor][0][2]:
                    conf.set(setColor, "v3max", str(edge[2]))  # 写入中文
                    conf.write(open(cfgpath, "r+", encoding="utf-8"))  # r+模式
                    print(setColor + "のデータを更新した")
                color[col][0].clear()
                color[col][1].clear()
                cdata = conf.items(setColor)
                print(cdata)

cap.release()
cv2.destroyAllWindows()
