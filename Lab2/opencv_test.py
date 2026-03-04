# coding=utf-8
import cv2
import time

# =========TODO: 開啟Tello的攝影機串流=========
# hint: 可以參考Tello官方文件：https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf
# 從官方文件找到對應的port
# cap=cv2.VideoCapture("udp://192.168.10.1:?")

# ===========================================
# 開啟本地的攝影機(0是本地攝影機的編號，若有多個攝影機可以嘗試1、2等)
cap=cv2.VideoCapture(0)

while True:
	# 讀取攝影機的影像資料
	isFrame, frame=cap.read()

	# 若成功讀取到影像(isFrame為True)，則把影像顯示到視窗中
	if isFrame:
		cv2.imshow("UAV video",frame)
	# 按下ESC鍵退出
	if cv2.waitKey(1) & 0xFF == 27:
		break

cap.release()
cv2.destroyAllWindows()
