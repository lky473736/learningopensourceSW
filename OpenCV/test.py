import cv2

cap = cv2.VideoCapture('video.mp4')
print(cap.isOpened())  # 비디오 파일이 올바로 열렸는지 확인
print(ret)  # 프레임을 제대로 읽었는지 확인

while cap.isOpened():  # 동영상 파일이 올바로 열렸는가?
    ret, frame = cap.read()  # ret : 성공 여부, frame : 동영상으로부터 받아온 프레임

    if not ret:
        print('더 이상 가져올 프레임 없음')
        break

    cv2.imshow('video', frame)  # video라는 창에 frame 띄움

    if cv2.waitKey(1) == ord('q'):  # q 아스키 코드 입력 시
        print('사용자 입력에 의해 종료')
        break

cap.release()  # 비디오 끔
cv2.destroyAllWindows()  # 모든 창 닫기

# mac에서 opencv 팝업창 안닫힐때 뒤에 항상 붙여주기
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
