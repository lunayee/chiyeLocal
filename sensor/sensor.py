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
            'LP':value[0],
            'LEQ':value[1],
            'LE':value[2],
            'LMAX':value[2],
            'LMIN':value[4],
            'LN3':value[8]
        }
    except:
        return {'LP': '', 'LEQ': '', 'LE': '', 'LMAX': '', 'LMIN': '', 'LN3': ''}

    return list

if __name__=='__main__':
    while(1):
        print(Sensor())
        time.sleep(1)

    


