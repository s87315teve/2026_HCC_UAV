# 人本計算實驗(Lab2)

## 環境建置
- 進入Lab1建立好的虛擬環境
```bash
conda activate UAV_env
```
- 安裝會使用到的套件
```bash
pip install opencv-python ultralytics
```

## 範例測試
- 執行`opencv_test.py`，測試opencv套件是否能夠正常運作
```
python opencv_test.py
```
成功執行的話會在電腦上看到鏡頭拍到的影像

- 執行`yolo_example.py`，測試yolo套件是否能正常運作
```bash
python yolo_example.py
```
執行成功的話會看到畫面上有框框把辨識到的物件標示出來

## Reference
- Ultralytics YOLO Docs: https://docs.ultralytics.com/
- Model Prediction with Ultralytics YOLO: https://docs.ultralytics.com/modes/predict/
