import serial
import time

COM = "/dev/ttyUSB0"

def UART_send(string):
    with serial.Serial(COM,9600,timeout=0.5) as ser:
        ser.write(string.encode('gbk') + b'\xff\xff\xff')
        time.sleep(0.1)

        #a = string.encode('ascii')
        #a = a + b'\xff\xff\xff'
        #print(a)
        #ser.flushOutput()
        #ser.write(a)
        #ser.write(string.encode('ascii'))

#        ser.close()

if __name__ == '__main__':
    try:
        UART_send('朱侨文')

    except Exception as ex:
        print(ex)
        raise

