import cv2
import time
from ultralytics import YOLO

# 載入 YOLO26 nano 模型（第一次執行會自動下載權重），如果電腦性能夠好的話可以用更大的模型 例如 "yolo26s.pt" 或 "yolo26m.pt"
model = YOLO("yolo26n.pt")

# 可以使用硬體加速，但要確定硬體是否相容以及是否已安裝對應的驅動程式
# model.to("cuda")  # 如果有 NVIDIA GPU，使用 CUDA 加速
# model.to("mps") # 如果有 Apple M1/M2/......，使用 MPS 加速
# 開啟攝影機（0 = 預設攝影機）
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("無法開啟攝影機")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("無法讀取畫面")
        break

    # 記錄推論開始時間
    t_start = time.perf_counter()

    # 執行 YOLO 推論
    results = model(frame, verbose=False) # 回傳辨識結果的list

    # 記錄推論結束時間
    t_end = time.perf_counter()
    inference_ms = (t_end - t_start) * 1000  # 轉換成毫秒

    # ── 印出每個 bounding box 的資訊 ──────────────────────────
    detections = results[0].boxes  # 因為我們一次只放一張圖所以只要取第一個就好
    print(f"{'─'*60}")
    print(f"[計算時間] {inference_ms:.1f} ms  |  偵測到 {len(detections)} 個物件")

    for i, box in enumerate(detections):
        # xyxy: 左上角(x1,y1) 右下角(x2,y2)，單位為像素
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        # xywh: 中心點(cx,cy) + 寬高
        cx, cy, w, h = box.xywh[0].tolist()
        conf = box.conf[0].item()           # 信心分數
        cls_id = int(box.cls[0].item())     # 類別 ID
        cls_name = model.names[cls_id]      # 類別名稱

        print(
            f"  [{i+1}] {cls_name:15s} conf={conf:.2f} | "
            f"xyxy=({x1:.0f},{y1:.0f},{x2:.0f},{y2:.0f}) | "
            f"center=({cx:.0f},{cy:.0f}) size=({w:.0f}x{h:.0f})"
        )
    # ──────────────────────────────────────────────────────────

    # 將 bounding box 畫在畫面上
    annotated_frame = results[0].plot()

    # 在畫面左上角顯示推論時間
    cv2.putText(
        annotated_frame,
        f"Inference: {inference_ms:.1f} ms",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8, (0, 255, 0), 2
    )

    cv2.imshow("YOLO26 即時偵測", annotated_frame)

    ## ========TODO: 在這裡可以根據偵測結果來控制無人機========
    # hint: 根據物件在圖上的位置（例如 bounding box 的中心點 cx, cy）來決定要對無人機發出什麼指令
    # hint: 發送指令之後要等無人機執行完畢再發送下一個指令，避免無人機來不及處理



    ## ==================================================



    # 按下 'esc' 鍵離開
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
