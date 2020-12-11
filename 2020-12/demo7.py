import cv2
import numpy as np
from numpy import ndarray


def face_update(url: str):
    img = cv2.imread(url)
    return img


def face_set(img, scale_factor=1.3, min_neighbors=3, min_size=(32, 32)):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(
        img,
        scaleFactor=scale_factor,
        minNeighbors=min_neighbors,
        minSize=min_size
    )
    return faces


def face_draw(img, faces, shape='square'):
    if shape == 'square':  # 可以为方形
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
    else:  # 可以为圆形，还没实现
        pass


def face_show(img):
    # print('调用face_show函数')
    # cv2.imshow('win_name', img)
    cv2.imwrite('win_name40.png', img)


# AI美颜
def change_darker(img: ndarray, value: int = 10):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    if value > 3:
        img_hsv[:, :, 1] = np.log(img_hsv[:, :, 1] / 255 * (value - 1) + 1) / np.log(value + 1) * 255
    if value < 0:
        img_hsv[:, :, 1] = np.uint8(img_hsv[:, :, 1] / np.log(- value + np.e))
    return cv2.cvtColor(img_hsv, cv2.COLOR_HLS2BGR)


# def beauty_face(url: str):
#     img = cv2.imdecode(np.fromfile(url, dtype=np.uint8), -1)
#     img_w = change_darker(img=img)
#     cv2.imshow('win_name', img_w)


def beauty_level(img: ndarray, level: int = 0):
    img.tmp_beauty_level = level
    return img


def beauty_face(img: ndarray):
    if hasattr(img, 'tmp_beauty_level'):
        value = img.tmp_beauty_level
    else:
        value = 0
    return change_darker(img, value=value)


if __name__ == '__main__':
    img = face_update(
        "/Users/zhou/Desktop/222.jpg")
    print(type(img))
    # faces = beauty_level(img, 100)
    # beauty_face(img)
    img = change_darker(img)
    print(type(img))
    face_show(img)
