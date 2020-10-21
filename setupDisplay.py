import subprocess
import re
import os

eth0ip = subprocess.Popen(['ip', 'a'], stdout=subprocess.PIPE)
eth0grep = subprocess.Popen(['grep','eth0'], stdin=eth0ip.stdout, stdout=subprocess.PIPE)
eth0inet = subprocess.Popen(['grep','inet'], stdin=eth0grep.stdout, stdout=subprocess.PIPE)
outval = eth0inet.communicate()[0].decode('utf8')
#reg_pat=r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"

reg_pat=r"(\d{1,3})"
outip_reg = re.search(reg_pat,outval)
octets = re.findall(reg_pat,outval)

x = 0
for each in octets:
    octets[x] = int(each)
    x += 1

def calNet(octet,mask):
    mask = 256 - 2 ** mask
    return octet & mask

network = 0
sw_octed = 0
if octets[4] < 9:
    val = octets[0]
    mask = octets[4]
    network = calNet(val, mask)
    sw_octed = 0
elif octets[4] < 17:
    val = octets[1]
    mask = octets[4] - 8
    network = calNet(val,mask)
    sw_octed = 1
elif octets[4] < 25:
    val = octets[2]
    mask = octets[4] - 16
    network = calNet(val,mask)
    sw_octed = 2
else:
    val = octets[3]
    mask = octets[4] - 24
    network = calNet(val,mask)
    sw_octed = 3

rebuild_ip = ""
x = 0
for each in octets:
    if x == sw_octed:
        rebuild_ip = str(rebuild_ip) + str(network)
    else:
        rebuild_ip = rebuild_ip + str(octets[x])
    rebuild_ip = rebuild_ip + "."
    x = x + 1
    if x == 3:
        break

displVal = f"{rebuild_ip}1:0"
print(displVal)
with open('.disp_ip','w') as dipf:
    dipf.write(displVal)
