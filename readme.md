


# 萬國覺醒 #


## adb shell cheat sheet ##

- 顯示NOX裝置清單


     nox_adb.exe devices


- APP檔案路徑

    
    /data/app/com.lilithgame.roc.gp.tw-1/base.apk
    

-   查詢包名與類名


    adb shell monkey --port 模擬器端口號 -v -v
    
-  啟動App

    
    adb shell am start -n 包名/Activity類名
    ---------------------------------------
    包名/Activity類名:
        com.lilithgame.roc.gp.tw/com.harry.engine.MainActivity
    adb -s 127.0.0.1:62001 shell am start -n com.lilithgame.roc.gp.tw/com.harry.engine.MainActivity
-   開啟任務清單


    adb -s 127.0.0.1:62001 shell am start -n com.lilithgame.roc.gp.tw/com.harry.engine.MainActivity

    
