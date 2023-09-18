# blockchain tree figure at 4.4 case 1, case 2, 4.5, point out the phase

# figure at theorem 2 with out 1/n

# 4.6 it's good for 2 samll the clusters to corporate, increase to 1000000 rounds


# expliat omnet++, the broadcast model, message, collect the latency data at 5.1, 5.2

# 5.3 dominent cluster is going to win

#key words, blockchain , mininig, reward, location bias, corporate/mining pool

#!/usr/bin/env python
import os, re, random
import time
import networkx as nx
import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib.cm as cm
def execCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text

# "172-31-27-161"connect to the main network
test_num = 246
fntable = ["3-8-181-21.txt", "13-212-160-108.txt", "52-198-129-79.txt", "3-26-15-29.txt", "18-237-236-50.txt", "3-135-244-21.txt", "18-188-201-137.txt", "18-222-129-4.txt", "35-182-179-172.txt", "15-237-45-62.txt", "18-207-240-179.txt", "3-101-74-8.txt", "18-184-53-17.txt", "52-51-154-80.txt", "13-125-150-5.txt", "13-126-131-161.txt", "13-48-195-57.txt", "35-183-111-12.txt", "3-96-184-244.txt", "35-182-236-42.txt", "34-248-214-65.txt", "15-185-204-146.txt", "15-185-161-116.txt", "13-244-70-77.txt", "13-244-105-48.txt", "13-244-68-204.txt", "13-233-97-254.txt", "13-127-233-230.txt", "13-53-133-149.txt", "13-48-25-75.txt", "54-233-89-147.txt", "18-230-187-28.txt"]

name = ["London", "singapore", "Japan", "Sydney", "Oregon", "ohio1", "Ohio2", "Ohio3", "Canada1", "Paris", "Virginia", "California", "Frankfurt", "Ireland1", "Stockholm1", "Seoul", "Mumbai3", "Canada2", "Canada3", "Canada4", "Ireland2", "Bahrain1", "Bahrain2", "Africa1", "Africa2", "Africa3", "Mumbai1", "Mumbai2", "Stockholm2", "Stockholm3", "Sanpaulo1", "Sanpaulo2"]

ftable = ["3.8.181.21", "13.212.160.108","52.198.129.79", "3.26.15.29", "18.237.236.50", "3.135.244.21", "18.188.201.137", "18.222.129.4", "35.182.179.172", "15.237.45.62", "18.207.240.179", "3.101.74.8", "18.184.53.17", "52.51.154.80", "13.125.150.5", "13.126.131.161", "13.48.195.57", "35.183.111.12", "3.96.184.244", "35.182.236.42", "34.248.214.65", "15.185.204.146", "15.185.161.116", "13.244.70.77", "13.244.105.48", "13.244.68.204", "13.233.97.254", "13.127.233.230", "13.53.133.149", "13.48.25.75", "54.233.89.147", "18.230.187.28"]
paradict = {}
file = open("node.txt", 'r', errors='replace')
loctable = ["" for _ in range(246)]
regtable = ["" for _ in range(246)]
lines = file.readlines()
filecount = 0
b = [5, 41, 120, 128, 132, 134, 146, 152, 172, 173, 178, 179, 182, 183, 199, 219, 237, 252, 253, 255, 257, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 286, 287, 288, 289, 290]
asian = ["Japan", "Russia", "Singapore", "Malaysia", "Thailand", "Vietnam", "Hong Kong", "China", "India", "Taiwan", "South Korea", "United Arab Emirates", "Israel", "Lebanon", "Pakistan", "Kazakhstan", "Philippines", "Bangladesh", "Saudi Arabia"]
for line in lines:
    id = int(line.split("\"")[1])
    continent = int(line.split("\"")[15])
    region = line.split("\"")[11]
    if id not in b:
        loctable[filecount] = continent
        if loctable[filecount]==3 and region in asian:
            loctable[filecount] = 6
        regtable[filecount] = region
        filecount += 1
count = [0 for _ in range(7)]
file.close()
WeightFileName="weight1.txt"
LinkDelay=np.zeros([test_num,test_num])
filew=open(WeightFileName,'r',errors='replace')
line=filew.readlines()
for i in range(test_num):
    a=line[i].split()
    for j in range(test_num):
        LinkDelay[i][j]=float(a[j])

filew.close()
#print(LinkDelay)

centrl = [215, 131, 110, 197, 105, 96, 161, 143, 48, 113, 88, 134, 190, 130, 121, 111, 79, 202, 45, 239, 98, 12, 66, 195, 97, 188, 13, 35, 160, 123, 138, 34, 144, 242, 139, 62, 59, 171, 107, 229, 95, 6, 191, 214, 10, 75, 82, 104, 61, 3, 106, 238, 78, 18, 8, 87, 90, 89, 169, 198, 224, 43, 119, 163, 146, 26, 83, 212, 184, 68]

nbrdict_0 = {}
nbrdict_1 = {}
nbrdict_2 = {}
connected = {}
outf = open("randomFeb28.txt", 'a')
outf.write("simple Txc13\n")
outf.write("{\n")
outf.write("    parameters:\n")
outf.write("        @display(\"i=block/routing\");\n")
outf.write("        int height=0;\n")
outf.write("    gates:\n")
outf.write("        inout gate[];\n")
outf.write("}\n")
outf.write("network Tictoc13\n")
outf.write("{\n")
outf.write("    //@class(Txc13);\n")
outf.write("    types:\n")
outf.write("        channel C extends ned.DelayChannel {\n")
outf.write("            delay = 100s;\n")
outf.write("        }\n")
outf.write("    submodules:\n")
outf.write("        node[246]: Txc13;\n")
outf.write("    connections allowunconnected:\n")
connect = {}
buff = {}

for i in range(246):
    for j in range(6):
        d = LinkDelay[i][j]
        sent1 = "        node["+str(i)+"].gate++ <--> {delay = "+str(d)+"s;} <--> node["+str(j)+"].gate++;"
        outf.write(sent1+"\n")
outf.write("}\n")




