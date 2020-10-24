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
# Convert ip octets to int
x = 0
for each in octets:
    octets[x] = int(each)
    x += 1

lookup_subnet = [0,128,192,224,240,248,252,254,255]


octets_subnet = []
network_short = int(octets[4])
x = network_short
while x > 0:
    if x >= 8:
        octets_subnet.append(255)
        x = x - 8
    else:
        octets_subnet.append(lookup_subnet[x])
        x = x - x
        while len(octets_subnet) < 4:
            octets_subnet.append(lookup_subnet[x])


octets_network = []
for each in range(0,4):
    val = octets[each] & octets_subnet[each]
    octets_network.append(val)

gateway_ip = ""
for x in range(0,4):
    if x == 3:
        gateway_ip = f"{gateway_ip}.{octets_network[x] + 1}"
    elif x == 0:
        gateway_ip = f"{octets_network[x]}"
    else:
        gateway_ip = f"{gateway_ip}.{octets_network[x]}"
gateway_ip = f"{gateway_ip}:0"
#displVal = f"{rebuild_ip}1:0"
print(gateway_ip)
with open('.disp_ip','w') as dipf:
    dipf.write(gateway_ip)
