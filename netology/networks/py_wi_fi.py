import pywifi
import time

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
print("Мой интерфейс", iface.name)

iface.scan()
time.sleep(2)
result = iface.scan_results()
print("\nДоступные сети:")
for i in range(len(result)):
    print(result[i].ssid)
