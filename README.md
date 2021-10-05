# AUTOMATE-STATIC-ROUTE
In VRF-lite situation multiple customers are connected to the same CE (each customer belongs to different vrf)
Now in this design wan circuit is moving from old PE to new PE.

During this bulk migration we need to replace static route pointing to OLD PE and with static route pointing to new PE for every customer

This migration related Pre and Post data such as vrf,CE wan ip,customer name,PE name etc. is recorded in excel sheet

With help of library xlrd , ciscoconfparse we can automate the script generation for static route which can be used during migration

we are reading all info for each VRF such as (VRF,OLD_WAN_IP,NEW_WAN_INT) by running FOR Loop on excel and storing it in dictionary

e.g Below 2 static routes needs to be replaced with new wan interface and new wan IP

ip route vrf ABC 10.10.10.10 255.255.255.255 Serial1/0.10 192.168.1.1
ip route vrf ABC 10.10.10.20 255.255.255.255 Serial1/0.10 192.168.1.1

Logic for the python code is
1. Get the static routes from router config for each vrf (one by one) using OLD wan IP (regular expression)
2. Take one IP route at a time and create list using split method so we will get 8 elements in list from 0-7
3. Pop the elements from the list till list contains only 6 elements from 0-5 (remove old interface and old wan ip)
4. Append new wan interface and then new wan PE IP to the list
5. Prepend no to the old static route and print it
6. Using join method on the list create new static route pointing to new wan IP and interface and print it

output is

no ip route vrf ABC 10.10.10.10 255.255.255.255 Serial1/0.10 192.168.1.1
ip route vrf ABC 10.10.10.10 255.255.255.255 FastEthernet0/1.10 192.168.2.1
!
no ip route vrf ABC 10.10.10.20 255.255.255.255 Serial1/0.10 192.168.1.1
ip route vrf ABC 10.10.10.20 255.255.255.255 FastEthernet0/1.10 192.168.2.1
