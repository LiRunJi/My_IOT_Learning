import serial
import platform

if platform.system() == "Windows":
    try:
        ble_uart = serial.Serial('com3', 9600, timeout=1)
        print("com3")
    except Exception as e:
        try:
            ble_uart = serial.Serial('com4', 9600, timeout=1)
            print("com4")
        except Exception as e:
            ble_uart = serial.Serial('com5', 9600, timeout=1)
            print("com5")

else:
    try:
        ble_uart = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        print("on usb0")
    except Exception as e:
        ble_uart = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)
        print("on usb1")
