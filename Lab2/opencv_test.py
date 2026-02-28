# coding=utf-8
import cv2
import time

# cap=cv2.VideoCapture("udp://192.168.10.1:?")
cap=cv2.VideoCapture(0)

while True:
	isFrame, frame=cap.read()

	if isFrame:
		cv2.imshow("UAV video",frame)
	# 按下ESC鍵退出
	if cv2.waitKey(1) & 0xFF == 27:
		break

cap.release()
cv2.destroyAllWindows()
