import os
import time


class RoK:
    def __init__(self):
        self.nox_path = 'D:/Program Files/Nox/bin'  # 設定NOX路徑
        self.device_ip = '127.0.0.1:62001'  # 設定預設裝置IP
        pass

    # 自動領取每日獎賞
    def get_awards(self):
        print("啟動應用中:")
        os.chdir(self.nox_path)  # 設定cmd預設路徑
        os.system("nox_adb.exe devices")  # 查詢模擬器IP
        os.system("adb -s %s shell am start -n com.lilithgame.roc.gp.tw/com.harry.engine.MainActivity" % self.device_ip)  # 啟動遊戲
        time.sleep(18)
        os.system("adb -s %s shell input swipe 182 76 182 76" % self.device_ip)  # 開啟vip表單
        time.sleep(3)
        os.system("adb -s %s shell input swipe 173 498 173 498" % self.device_ip)  # 領取獎勵
        time.sleep(3)
        os.system("adb -s %s shell input swipe 173 498 173 498" % self.device_ip)  # 完成領取獎勵
        time.sleep(3)
        os.system("adb -s %s shell input swipe 270 213 270 213" % self.device_ip)  # 領取每日vip點數
        time.sleep(3)
        os.system("adb -s %s shell input swipe 270 213 270 213" % self.device_ip)  # 完成每日領取vip點數
        time.sleep(3)
        os.system("adb -s %s shell input swipe 1363 100 1363 100" % self.device_ip)  # 關閉vip表單
        time.sleep(3)


obj = RoK()
obj.get_awards()
