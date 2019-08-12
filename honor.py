import os
import time
from PIL import Image
import imagehash


class RoK:
    def __init__(self):
        self.nox_path = 'D:/Program Files/Nox/bin'  # 設定NOX路徑
        self.device_ip = '127.0.0.1:62001'  # 設定預設裝置IP
        self.highfreq_factor = 1
        self.hash_size = 8
        self.img_size = self.hash_size * self.hash_size
        pass

    # 自動領取每日獎賞
    # def get_awards(self):
    #     print("啟動應用中:")
    #     os.chdir(self.nox_path)  # 設定cmd預設路徑
    #     os.system("nox_adb.exe devices")  # 查詢模擬器IP
    #     os.system("adb -s %s shell am start -n com.lilithgame.roc.gp.tw/com.harry.engine.MainActivity" % self.device_ip)  # 啟動遊戲
    #     time.sleep(25)
    #     os.system("adb -s %s shell input swipe 182 76 182 76" % self.device_ip)  # 開啟vip表單
    #     time.sleep(3)
    #     os.system("adb -s %s shell input swipe 173 498 173 498" % self.device_ip)  # 領取獎勵
    #     time.sleep(3)
    #     os.system("adb -s %s shell input swipe 173 498 173 498" % self.device_ip)  # 完成領取獎勵
    #     time.sleep(3)
    #     os.system("adb -s %s shell input swipe 270 213 270 213" % self.device_ip)  # 領取每日vip點數
    #     time.sleep(3)
    #     os.system("adb -s %s shell input swipe 270 213 270 213" % self.device_ip)  # 完成每日領取vip點數
    #     time.sleep(3)
    #     os.system("adb -s %s shell input swipe 1363 100 1363 100" % self.device_ip)  # 關閉vip表單
    #     time.sleep(3)

    def screen_shot(self):
        print("啟動應用中:")
        os.chdir(self.nox_path)  # 設定cmd預設路徑
        os.system("nox_adb.exe devices")  # 查詢模擬器IP
        os.system("adb -s %s shell am start -n com.lilithgame.roc.gp.tw/com.harry.engine.MainActivity" % self.device_ip)  # 啟動遊戲
        while True:
            print("開始截圖進行比對:")
            # w967h544
            os.system("adb -s %s shell screencap -p /sdcard/abc.png" % self.device_ip)  # 截圖遊戲當前畫面
            os.system("adb -s %s pull -p /sdcard/abc.png D:/Code/python/Rok/" % self.device_ip)
            print("確定已經儲存到文件檔案內")
            img = Image.open('D:/Code/python/Rok/abc.png')  # 開啟截圖後的照片
            print("成功開啟截圖畫面")
            # img = img.transpose(Image.ROTATE_90)
            img = img.crop((123, 57, 843, 497))  # 要截圖的座標位置
            print("開始進行截圖")
            img.save('D:/Code/python/Rok/abcd.png')  # 儲存截圖畫面
            print("成功儲存截圖畫面")
            hash1 = imagehash.phash(Image.open('D:/Code/python/Rok/abcd.png'), hash_size=self.hash_size, highfreq_factor=self.highfreq_factor)  # 打開一開始存放的比對圖片，並計算hash值
            print(hash1)
            print("比對成功1")
            # > 354adab5054af0b7
            hash2 = imagehash.phash(Image.open('D:/Code/python/Rok/test.png'), hash_size=self.hash_size, highfreq_factor=self.highfreq_factor)  # 打開截圖完成後的照片，並且計算hash值
            print(hash2)
            print("比對成功2")
            print("開始進行輸出比對結果")
            # > 5b7724c8bb364551
            result = 1 - (hash1 - hash2)/len(hash1.hash)**2
            print(1 - (hash1 - hash2)/len(hash1.hash)**2)  # 開始比對，並輸出結果
            if result > 0.95:
                print('點開執政官資料')
                self.click_xxx()
                break

    def click_xxx(self):




obj = RoK()
# obj.get_awards()
obj.screen_shot()
