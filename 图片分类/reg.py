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

path = os.path.join(os.getcwd(), "./Resources")
for file in os.listdir(path):
    if file[0] == '.':
        continue
    fpath = os.path.join(path, file)
    if (os.path.isdir(fpath)):
        print(file, ': ')
        for f in os.listdir(fpath):
            pic = cv.imread(os.path.join(fpath, f))
            #h, w, _ = pic.shape
            w, h, _ = pic.shape
            MAXSIZE = 512
            if w > MAXSIZE or h > MAXSIZE:
                if (h > w):
                    w = int(MAXSIZE*w/h)
                    h = MAXSIZE
                else:
                    h = int(MAXSIZE*h/w)
                    w = MAXSIZE
            print('file=',f,'  shape=', (h, w), end='  face=')
            pic = cv.resize(pic, (h, w), interpolation=cv.INTER_CUBIC)

            cv.imshow("Face", pic)
            cv.waitKey(1)
            
            faces = facerec.api.face_locations(
                pic, number_of_times_to_upsample=1, model='cnn')
            if len(faces) != 1:
                print('人脸数错误,检测到'+str(len(faces))+'张人脸,已跳过')
                continue
            face_code = facerec.face_encodings(pic, faces, 1)
            print(faces[0])

            data = DATA(face_code[0], file)
            datas.append(data)
cv.destroyAllWindows()

with open('./facedatas', 'wb+') as f:
    pickle.dump(datas, f)


'''
with open('./facedatas', 'rb') as f:
    datas = pickle.load(f)
    for data in datas:
        print(data.face_code)
'''
