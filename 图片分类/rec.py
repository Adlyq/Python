import pickle
import os
import cv2 as cv
import face_recognition as facerec
import numpy as np
from PIL import Image, ImageDraw, ImageFont


class DATA:
    def __init__(self, code, name):
        self.face_code = code
        self.face_name = name


gface_codes = []
gface_names = []

with open('facedatas', 'rb') as f:  # load facedata
    datas = pickle.load(f)
    for data in datas:
        gface_codes.append(data.face_code)
        gface_names.append(data.face_name)
os.system('rm -r ./OUT/*')
for name in gface_names:
    try:
        os.mkdir('./OUT/'+name)
    except FileExistsError:
        continue
    
def getAllFiles(path):
    res = []
    for file in os.listdir(path):
        if file[0] == '.':
            continue
        fpath = os.path.abspath(os.path.join(path, file))
        if (os.path.isdir(fpath)):
            res += getAllFiles(fpath)
        else:
            res.append(fpath)
    return res


files = getAllFiles(os.path.join(os.getcwd(), "./Result"))
for file in files:
    print()
    print(file)
    pic = cv.imread(file)
    w, h, _ = pic.shape
    MAXSIZE = 1024
    if w > MAXSIZE or h > MAXSIZE:
        if (h > w):
            w = int(MAXSIZE*w/h)
            h = MAXSIZE
        else:
            h = int(MAXSIZE*h/w)
            w = MAXSIZE
        pic = cv.resize(pic, (h, w), interpolation=cv.INTER_CUBIC)

    faces = facerec.api.face_locations(
        pic, number_of_times_to_upsample=1, model='cnn')
    if (len(faces) == 0):
        print('未检测到人脸已跳过')
        os.system('cp '+file+' ./OUT/')
        continue
    print('共',len(faces),'张人脸')

    face_codes = facerec.face_encodings(pic, faces, 1)

    for code in face_codes:
        distances = facerec.face_distance(code, gface_codes)

        resd = 999999
        res = -1
        for i in range(len(distances)):
            if resd >= distances[i] and distances[i] <= 0.38:
                res = i
                resd = distances[i]

        if res > -1:
            code = gface_codes[res]
            name = gface_names[res]
            os.system('cp '+file+' ./OUT/'+name)
            print(name, '\t', resd)#int(resd*100)/100)
    print('')
