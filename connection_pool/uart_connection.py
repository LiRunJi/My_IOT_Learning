import serial
import platform
from serial.tools import list_ports


def scan_ports_linux():
    plist = list(serial.tools.list_ports.comports())
    for p in plist:
        if p.name.__contains__('ttyUSB'):
            print(p.__str__())
            return p.device


def scan_ports_windows():
    plist = list(serial.tools.list_ports.comports())
    for p in plist:
        print(p.__str__())
        return p.device

if platform.system() == "Windows":
    try:
        ble_uart = serial.Serial(scan_ports_windows(), 9600, timeout=1)
    except Exception as e:
        print(e)
        print("设备没插入,请插入后再试")
else:
    try:
        ble_uart = serial.Serial(scan_ports_linux(), 9600, timeout=1)
    except Exception as e:
        print(e)
        print("设备没插入,请插入后再试")
