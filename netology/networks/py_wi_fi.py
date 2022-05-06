import pywifi
import time

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
print("Мой интерфейс", iface.name)
