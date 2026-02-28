# 人本計算實驗(Lab1)

## Tello EDU 飛控


## 環境建置



- 作業系統：建議使用Ubuntu，但Windows或MacOS也可以

- 下載Anaconda，到 https://repo.anaconda.com/archive/ 下載符合自己系統的版本
例如：
```
- Windows: Anaconda3-2025.12-2-Windows-x86_64.exe
- MacOS (Apple Silicon): Anaconda3-2025.12-2-MacOSX-arm64.sh
- Ubuntu: Anaconda3-2025.12-2-Linux-x86_64.sh
```
* 安裝Anaconda (以Ubuntu為例)：打開Terminal，在Terminal輸入以下指令
```bash
bash Anaconda3-2025.12-2-Linux-x86_64.sh
```

* 重啟terminal，會看到用戶名字前面有(base)

* 安裝git
```bash
sudo apt-get install git
```
* 下載上課用github資料
```bash
git clone https://github.com/s87315teve/2026_HCC_UAV.git
```


## Anaconda 基本指令介紹
* 建立新環境（terminal前面需有base）
    ```bash
    conda create --name <環境名稱> python=3.11
    ```
* 刪除環境
    ```bash
    conda remove --name <環境名稱”>
    ```
* 進入已建立的環境
    ```bash
    conda activate <環境名稱>
    ```
* 離開已建立的環境
    ```bash
    conda deactivate
    ```
## 建立開發環境
1. 建立新環境
```bash
conda create --name UAV_env python=3.11
```
2. 進入虛擬環境
```bash
conda activate tello
```
3. 進入Lab1資料夾
```bash
cd 2026_HCC_UAV/Lab1
```
4. 執行範例程式
```bash
python example.py
```

## 範例程式使用說明
* 執行程式後，程式會自動送出"command"指令，並進入SDK模式 (如果command沒有發送成功的話請手動發送)
* 進入SDK模式後即可輸入控制指令








