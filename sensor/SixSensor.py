import serial
import modbus_tk.modbus_rtu as rtu
import time



def SIXSENSOR():
    try:
        ser = serial.Serial(port='COM3',baudrate=4800,bytesize=8,parity="N",stopbits=1)
        master = rtu.RtuMaster(ser)
        master.set_timeout(1.0)
        master.set_verbose(True)
        read_values = master.execute(1,3,500,20)
        WS = read_values[0]/100
        WD = read_values[3]
        HUM = read_values[4]/10
        TMP = read_values[5]/10
        PRE = (760*read_values[9])/1013
        RAIN = read_values[13]
        return (WS,WD,TMP,HUM,RAIN,PRE)
    except:
        #線沒接好
        return (-9999,-9999,-9999,-9999,-9999,-9999)

def cleanRain():
    read_values = master.execute(1,6,0x5A,output_value=0x5A)
    return read_values



if __name__=='__main__':
    while(1):
        print(SIXSENSOR())
    