# miniproject 2. 웹캠을 이용하여 움직이는 사물 윤곽선 표시
# 표시는 잘 되나, 움직이는 사물을 모두 표시하니 굉장히 짜증남.
# -> mediapipe의 face detection 사용 (mini2.ipynb 참고)
 
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened() : 
    print ("장치가 없습니다.")
    exit()
    
COLOR = (0, 200, 0)
    
while True : 
    ret, frame = cap.read()
    
    if not ret : 
        break
    
    targetframe = frame.copy() # 프레임의 사본
    
    # otsu algo를 이용한 이진화 
    gray = cv2.cvtColor(targetframe, cv2.COLOR_BGR2GRAY)
    ret, otsu = cv2.threshold (gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    contours, hierarchy = cv2.findContours(otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) # 윤곽선 검출
    # 반환되는 값은 윤곽선 정보, 윤곽선 구조
    # 대상 이미지, 윤곽선 찾는 모드, 윤곽선 찾을 때 사용하는 근사치 방법 (method)

    for cnt in contours :
        x, y, width, height = cv2.boundingRect(cnt)
        cv2.rectangle(targetframe, (x, y), (x + width, y + height), COLOR, 2) # 왼쪽위, 오른쪽아래
        
    cv2.imshow ('targetframe', targetframe)
    
    if cv2.waitKey(1) == ord('q'):  # waitkey(n) : n으로 속도 조절
        print('사용자 입력에 의해 종료')
        break
        
cap.release() # 동영상 파일 닫고 메모리 해제

# mac에서 opencv 팝업창 안닫힐때 뒤에 항상 붙여주기
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)