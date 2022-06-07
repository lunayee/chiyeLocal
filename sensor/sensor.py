import serial, time

ser = serial.Serial()  
ser.port = 'COM10'
ser.baudrate = 9600
ser.parity = serial.PARITY_NONE
ser.bytesize = serial.EIGHTBITS 
ser.stopbits = serial.STOPBITS_ONE
ser.xonxoff = False  #disable software flow control
ser.rtscts = False  #disable hardware (RTS/CTS) flow control
ser.dsrdtr = False  #disable hardware (DSR/DTR) flow control
ser.timeout = 1
ser.open() # open serial port 

def Sensor():
    try:
        ser.write(b'DOD?\r\n')
        strvalue= ser.readall().decode('utf8')
        value = strvalue[9:-3].split(', ') #all_value
        list = {
            'Value1':value[0],#
            'Value2':value[1],#LEQ噪音
            'Value3':value[2],#風速
            'Value4':value[2],#風向
            'Value5':value[4],#溫#濕度#雨量#大氣壓
            'Value6':value[8]
        }
        if list['Value2']=="--.-":
            return {'Value1': '-99', 'Value2': '-99', 'Value3': '-99', 'Value4': '-99', 'Value5': '-99', 'Value6': '-99'}
    except:
        return {'Value1': '0', 'Value2': '0', 'Value3': '0', 'Value4': '0', 'Value5': '0', 'Value6': '0'}

    return list

if __name__=='__main__':
    while(1):
        print(Sensor())
        time.sleep(1)

    


