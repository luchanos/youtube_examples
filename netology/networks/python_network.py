import nmap3
import json


# scanning host...
scan = nmap3.NmapScanTechniques()

res = scan.nmap_syn_scan("luchanos.ru")

with open("../result_file", "w") as f_o:
    json.dump(res, f_o, ensure_ascii=True, indent=4)

print("Completed!")
