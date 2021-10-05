import xlrd
from ciscoconfparse import CiscoConfParse

# provide config file path
routerconfig = CiscoConfParse(configfilepath)
wanip = c[‘OLD_WAN_IP’].split(“.”)
# result [192,168,1,1]
wanipregex = “\.”.join(wanip)
# result 192\.168\.1\.1
a = “^ip route vrf ” + c[‘VRF’] +”(.+?)” + wanipregex
# result ^ip route vrf ABC(.+?)192\.168\.1\.1

# running for loop over list of static routes for vrf ABC 2 routes in this case
for staticroute in routerconfig.find_objects(a):
line = staticroute.text

sroute = line.split(” “)
# result [ip, route, vrf, ABC, 10.10.10.10, 255.255.255.255, Serial1/0.10, 192.168.1.1]

while len(sroute) > 6:
sroute.pop()
# result [ip, route, vrf, ABC, 10.10.10.10, 255.255.255.255]

sroute.append(c[‘NEW_WAN_INT’])
# result [ip, route, vrf, ABC, 10.10.10.10, 255.255.255.255,FastEthernet0/1.10,]
sroute.append(c[‘NEW_PE_WAN_IP’])
#result [ip, route, vrf, ABC, 10.10.10.10, 255.255.255.255, FastEthernet0/1.10, 192.168.2.1]
print “no ” + line
# result no ip route vrf ABC 10.10.10.10 255.255.255.255 Serial1/0.10 192.168.1.1
print ” “.join(sroute)
# result ip route vrf ABC 10.10.10.10 255.255.255.255 FastEthernet0/1.10 192.168.2.1
print “!”
