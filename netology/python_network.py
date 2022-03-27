import nmap3
import json
from functools import partial
from sys import argv

# scanning host...
scan = nmap3.NmapScanTechniques()

mapper = {
    "syn": partial(scan.nmap_syn_scan),
    "ping": partial(scan.nmap_ping_scan),
    "tcp": partial(scan.nmap_tcp_scan),
    "udp": partial(scan.nmap_udp_scan)
}

res = mapper[argv[1]]("luchanos.ru")

with open("result_file", "w") as f_o:
    json.dump(res, f_o, ensure_ascii=True, indent=4)

print("Completed!")
