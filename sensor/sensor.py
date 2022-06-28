import Noise
import SixSensor


def Sensor():
    # Value1-6校正後的值 Value14-19校正前的值
    N = Noise.NOISE()
    SIX = SixSensor.SIXSENSOR()
    #原始值
    list = {
        'Value8':N,# 噪音
        'Value9':SIX[0],# 風速
        'Value10':SIX[1],# 風向
        'Value11':SIX[2],# 溫度
        'Value12':SIX[3],# 濕度
        'Value13':SIX[4],# 雨量
        'Value14':SIX[5],# 大氣壓力
    }
    return list
    

if __name__=='__main__':
    while(1):
        print(Sensor())

