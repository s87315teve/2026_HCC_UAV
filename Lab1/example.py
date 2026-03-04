# coding=utf-8
# Tello Python3 Control Demo
#
# http://www.ryzerobotics.com/
#

import threading
import socket
import time

# Tello EDU 的IP和port，所有控制命令將發送到此位置
tello_address = ('192.168.10.1', 8889)

# 本機監聽port地址，將會從這邊收到來自無人機的response
host = ''
port = 9000
locaddr = (host, port)

# 建立UDP socket（使用AF_INET表示IPv4，SOCK_DGRAM表示UDP協定）
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 將socket綁定到本機，開始監聽來自無人機的回應
sock.bind(locaddr)



def recv():
    """
    背景執行的接收函式，持續監聽來自無人機的回應訊息。
    當收到資料時，將其解碼並印出；若發生例外則退出迴圈。
    """
    while True:
        try:
            # data  : 無人機回傳的原始bytes資料
            # server: 無人機的IP與port
            data, server = sock.recvfrom(1518)

            # 將bytes資料用utf-8解碼成字串後印出
            print("{} : {}".format(server, data.decode(encoding="utf-8")))

        except Exception:
            print('\nExit . . .\n')
            break


print('\r\n\r\nTello Python3 Demo.\r\n')
print('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')
print('end -- quit demo.\r\n')

# 建立daemon thread在背景執行recv函式
# daemon=True 表示主程式結束時，此thread會自動跟著終止，不會卡住
recvThread = threading.Thread(target=recv, daemon=True)
recvThread.start()

# 自動送出 "command" 讓Tello進入SDK控制模式
# 若不先送這個指令，後續所有控制命令都會無效
print('正在初始化：自動送出 command 進入 SDK 模式...')
init_msg = 'command'.encode('utf-8')
sock.sendto(init_msg, tello_address)

time.sleep(1)  # 等待無人機回應 "ok" 後再繼續

print('初始化完成，可以開始輸入指令！\n')

# 進入無限迴圈，讓你可以用鍵盤輸入控制命令
while True:
    try:
        msg = input("Enter your command: ")

        # 若輸入為空白則跳過，不送出任何東西
        if not msg:
            continue

        # 輸入 end 可以安全地退出程式
        if msg.strip().lower() == 'end':
            print('正在關閉程式...')
            break

        # 將字串指令編碼成bytes後透過UDP送出給無人機
        msg_encoded = msg.encode(encoding="utf-8")
        sock.sendto(msg_encoded, tello_address)


        # 短暫等待，避免發送過快導致封包遺失或無人機來不及處理
        time.sleep(0.5)

    except KeyboardInterrupt:
        # 按下 Ctrl+C 時也能安全退出
        print('\n偵測到 Ctrl+C，正在關閉程式...')
        break


sock.close()
print('Socket 已關閉，程式結束。')