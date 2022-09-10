#coding:utf-8

import os
import time
from datetime import datetime as dt
import winsound

def beep(n = 5):    
    for i in range(n):
        winsound.Beep(440, 300)
        time.sleep(0.5)
    
    
if __name__ == '__main__':

    print('闹钟提醒')
    print('现在时间:', dt.now().strftime("%Y%m%d %H:%M:%S"))
    data = input('你需要提示的时间：')

    if len(data) < 4:
        print('无效时间,退出')
        exit(0)
        
    try:
        b = int(data)
    except:
        print('无效时间,退出')
        exit(0)
        
    hh = data[0:2]
    mm = data[2:4]    
    
    try:
        hhh = int(hh)
        mmm = int(mm)
        if hhh < 0 or hhh > 23 or mmm < 0 or mmm > 59:
            print('无效时间,退出')
            exit(0)            
    except:
        print('无效时间,退出')
        exit(0)    
    
    call = 0
    
    while True:
        cur_time = dt.now().strftime("%H%M")
        h = cur_time[0:2]
        m = cur_time[2:4]
        print('\r', dt.now().strftime("%Y%m%d %H:%M:%S"), end='', flush=True)
        if h == hh and m == mm:            
            print('\n到时间了！！！')
            call = 1
            beep(5)            
            break        
        else:                        
            time.sleep(1)
        
    print('退出')
    
    
    