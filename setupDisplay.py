import subprocess
import re

eth0ip = subprocess.Popen(['ip', 'a'], stdout=subprocess.PIPE)
eth0grep = subprocess.Popen(['grep','eth0'], stdin=eth0ip.stdout, stdout=subprocess.PIPE)
eth0inet = subprocess.Popen(['grep','inet'], stdin=eth0grep.stdout, stdout=subprocess.PIPE)
outval = eth0inet.communicate()[0].decode('utf8')
reg_pat=r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.)"
outval_reg = re.search(reg_pat,outval)
displVal = outval_reg.group()
displVal = f"{displVal}1:0"
print(displVal)

subprocess.run(['export', displVal])
