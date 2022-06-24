import serial
import time
ser = serial.Serial()  
ser.port = 'COM2'
ser.baudrate = 9600
ser.parity = serial.PARITY_NONE
ser.bytesize = serial.EIGHTBITS 
ser.stopbits = serial.STOPBITS_ONE
ser.xonxoff = False  #disable software flow control
ser.rtscts = False  #disable hardware (RTS/CTS) flow control
ser.dsrdtr = False  #disable hardware (DSR/DTR) flow control
ser.timeout = 1
ser.open() # open serial port 

def NOISE():
    try:#儀器沒抓到值，可以按按看start
        ser.write(b'DOD?\r\n')
        strvalue= ser.readall().decode('utf8')
        return float(strvalue[9:13])
    except:#線沒接好
        return -9999

if __name__=='__main__':
    while(1):
        print(NOISE())