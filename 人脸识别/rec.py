import pickle

import cv2 as cv
import face_recognition as facerec
import numpy as np
from PIL import Image, ImageDraw, ImageFont


class DATA:
    def __init__(self, code, name):
        self.face_code = code
        self.face_name = name

font = ImageFont.truetype("mcyh.ttf", 20, encoding="utf-8") # 参数1：字体文件路径，参数2：字体大小

cap = cv.VideoCapture(0)

gface_codes = []
gface_names = []
with open('facedatas', 'rb') as f: #load facedata
    datas = pickle.load(f)
    for data in datas:
        gface_codes.append(data.face_code)
        gface_names.append(data.face_name)


while True:
    ret, pic = cap.read()
    pic = cv.resize(pic, (320, 255), interpolation=cv.INTER_LINEAR)
    pic = cv.flip(pic, 1) # 图像翻转

    cvimg = cv.cvtColor(pic, cv.COLOR_BGR2RGB)  # cv2和PIL中颜色的hex码的储存顺序不同
    pilimg = Image.fromarray(cvimg)
    draw = ImageDraw.Draw(pilimg)

    faces = facerec.api.face_locations(pic, number_of_times_to_upsample=1, model='cnn')
    face_codes = facerec.face_encodings(pic, faces, 1)
    faces = [(left, top, right - left, bottom - top) for (top, right, bottom, left) in faces]

    for (x, y, xs, ys), code in zip(faces, face_codes):
        distances = facerec.face_distance(code, gface_codes)

        resd = 999999
        gstr = r'N/A'
        res = -1
        for i in range(len(distances)):
            if resd >= distances[i] and distances[i] <= 0.48:
                res = i
                resd = distances[i]

        if res > -1:
            code = gface_codes[res]
            name = gface_names[res]
            gstr = name + '\n' + str(resd)

        draw.rectangle((x, y, x + xs, y + ys), width=3)
        draw.text((x, y - 50), gstr, (255, 0, 0), font=font)  # 参数1：打印坐标，参数2：文本，参数3：字体颜色，参数4：字体

    cvcharimg = cv.cvtColor(np.array(pilimg), cv.COLOR_RGB2BGR)
    cvcharimg = cv.resize(cvcharimg, (640, 515), interpolation=cv.INTER_LINEAR)
    cv.imshow("Face", cvcharimg)
    key = cv.waitKey(1)
    if key == 27:
        break

