import time,datetime
import Noise
import SixSensor


def Sensor():
    # Value1-6校正後的值 Value14-19校正前的值
    N = Noise.NOISE()
    SIX = SixSensor.SIXSENSOR()
    now = datetime.datetime.now()
    str_now = datetime.datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
    #原始值
    list = {
        'Value14':N,# 噪音
        'Value15':SIX[0]/100,# 風速
        'Value16':SIX[1],# 風向
        'Value17':SIX[2]/10,# 溫度
        'Value18':SIX[3]/10,# 濕度
        'Value19':SIX[4],# 雨量
        'Value20':SIX[5],# 大氣壓力
    }
    return list
    

if __name__=='__main__':
    while(1):
        print(Sensor())



