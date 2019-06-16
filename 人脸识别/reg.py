import cv2 as cv
import os
import face_recognition as facerec
import pickle

class DATA:
    def __init__(self, code, name):
        self.face_code = code
        self.face_name = name

'''
cap = cv.VideoCapture(0)
ret, frame = cap.read()
cv.imshow('aaa', frame)
cv.waitKey()
'''
datas = []

path = os.path.join(os.getcwd(), "./pic")
for file in os.listdir(path):
    if file[0] == '.':
        continue
    fpath = os.path.join(path, file)
    fname = file.split(".")[0]
    pic = cv.imread(fpath)
    faces = facerec.api.face_locations(pic, number_of_times_to_upsample=1, model='cnn')
    print(faces, end='')
    print('  ' + fname)
    face_code = facerec.face_encodings(pic, faces, 1)
    if len(face_code) != 1:
        print(file +'  人脸数错误,已跳过')
        continue
    data = DATA(face_code[0], fname)
    datas.append(data)

with open('./facedatas', 'wb+') as f:
    pickle.dump(datas,f)


'''
with open('./facedatas', 'rb') as f:
    datas = pickle.load(f)
    for data in datas:
        print(data.face_code)
'''