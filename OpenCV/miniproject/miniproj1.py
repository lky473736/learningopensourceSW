# miniproject 1. tkinter와 OpenCV를 이용한 이미지 분석기

import cv2
import os
from tkinter import *
window1 = Tk()

global name

def checktheimage() :
    # https://wikidocs.net/14304
    # https://wangin9.tistory.com/entry/python-file-exist
    
    global name
    name = e1.get().strip()  # 공백 제거

    print(f"파일 이름: '{name}'")  # 디버깅을 위한 출력
    print(os.getcwd())

    if os.path.isfile(name):
        return 'p'
    else:
        return 'f'
    
def display_result():
    result = checktheimage()
    print (name) # global 변수인지 확인 

    if result == 'p':
        message = "이미지가 존재합니다."

        if message == "이미지가 존재합니다.":
            window2 = Tk()

            img = cv2.imread(name)
            cv2.imshow('original', img)

            l5 = Label(window2, text="아래에 인자 입력 (사이즈 비율, 이미지 회전각도)")
            l5.pack()
            
            global e2 # 사용자 지정 함수에서 e2 사용 위해
            e2 = Entry(window2)
            e2.pack()

            bt2 = Button(window2, text="흑백 변환", command=grayscale)
            bt2.pack()

            bt3 = Button(window2, text="사이즈 조절", command=changesize)
            bt3.pack()

            bt4 = Button(window2, text="이미지 회전", command=rotate)
            bt4.pack()

            bt5 = Button(window2, text="사용자 종료", command=out)
            bt5.pack()
            
            window2.mainloop()
        
    else :
        message = "파일이 존재하지 않습니다."
        
    # Clear any previous messages
    l3.config(text="")

    # Insert the new message
    l3.config(text=message)
            
def grayscale():
    img_gray = cv2.imread(name, cv2.IMREAD_GRAYSCALE)
    cv2.imshow ('img_gray', img_gray)

def changesize():
    size = float(e2.get())
    
    img_ori = cv2.imread(name)
    img_dst = cv2.resize(img_ori, None, fx = size, fy = size)
    
    cv2.imshow(f'img_dst = {size}', img_dst)
    
def rotate():
    angle = float(e2.get())
    
    img_ori = cv2.imread(name)
    
    if angle == 90 :
        img_rot = cv2.rotate(img_ori, cv2.ROTATE_90_CLOCKWISE)
        
    else :
        img_rot = cv2.rotate(img_ori, cv2.ROTATE_180)
        
    cv2.imshow(f'img_rot = {angle}', img_rot)
    
def out():
    exit()

l1 = Label(window1, text="<miniproject 1. tkinter와 OpenCV를 이용한 이미지 분석기>")
l2 = Label(window1, text="이미지의 이름을 입력하세요. (확장자 포함)")
l1.pack()
l2.pack()

e1 = Entry(window1)
e1.pack()

bt1 = Button(window1, text="입력", command=display_result)
bt1.pack()

l3 = Label(window1, text="")
l3.pack()

window1.mainloop()
