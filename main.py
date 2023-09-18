
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np
    HashFileName="hash1.txt"
    NodeHash=np.zeros(246)
    fileh=open(HashFileName,'r',errors='replace')
    line=fileh.readlines()
    a=line[0].split("  ")
    for j in range(246):
        NodeHash[j]=a[j]
    fileh.close()
    
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
    #print(loctable)
    for i in range(246):
        paradict[i] = []
    hash = [1 for _ in range(246)]
    #loc = [6.42, 4.34, 3.64, 4.39, 4.18, 4.41, 4.29, 4.47, 2.35, 3.85, 3.76, 2.79, 3.58, 3.21, 4.25, 2.84, 2.11, 3.18, 3.56, 2.48, 2.34, 1.94, 2.05, 2.59, 2.63, 1.92, 2.1, 2.09, 1.92, 2.31, 1.61, 2.09]
    hashSum = sum(hash)
    for i in range(246):
        hash[i] = int(hash[i]/hashSum*10000)/100
    locSum = 0
    '''
    for i in range(246):
        loc[i] = loc[i]*hash[i]
        locSum += loc[i]
    for i in range(246):
        loc[i] = int(loc[i]/locSum*10000)/100
    '''
    resultDict = {}
    for i in range(246):
        resultDict[i] = []
    for readfile in ["n246r0.txt", "complete.txt"]:
        hTable = [0 for _ in range(246)]
        blkdict = {}
        filer = open(readfile, 'r', errors='replace')
        lines = filer.readlines()
        blkLen = 0
        lenlist = []
        node = 0
        for line in lines:
            if line[0] == "n":
                node += 1
            else:
                miners = line.split()
                for miner in miners:
                    if node not in blkdict:
                        blkdict[node] = [int(miner)]
                    else:
                        blkdict[node].append(int(miner))
        #print(readfile, node)
        #print(blkdict)
        for count in blkdict.keys():
            buff = [0 for _ in range(246)]
            bufflen = len(blkdict[count])
            for item in blkdict[count]:
                buff[item] += 1
            for j in range(246):
                resultDict[j].append(int(buff[j]/bufflen*10000)/100)
            #plt.subplot(2,3,miner+1)
            #plt.plot(range(len(result)), result)
            #plt.title("miner: "+str(miner))
            ##plt.legend()
        #plt.savefig("result-mix.png")
    #for node in resultDict.keys():
    #    print(node, len(resultDict[node]), resultDict[node])
    
    plt.figure(figsize=(100,100))
    c = 1
    res1 = 0
    res2 = 0
    res3 = 0
    [resa, resb, resc] = [0, 0, 0]
    for i in range(246):
        if loctable[i] == 1:
            plt.subplot(10,10,c)
            toplot = []
            for k in range(2):
                toplot.append(resultDict[i][k*5:k*5+5])
            #toplot.append([sum(resultDict[i][20:25])/5])
            res1 += sum(resultDict[i][0:5])/5
            res2 += sum(resultDict[i][15:20])/5
            #res3 += resultDict[i][k*5+5]
            if res2 > 1.1*res1:
                resa += 1
            if res2 < 0.9*res1:
                resb += 1
            resc += 1
            plt.boxplot(toplot, labels = ["random", "complete"])
            #plt.hlines(hash[i], 0, len(toplot), color = "black", label="% of hash")
            #plt.hlines(loc[i], 0, len(toplot), color = "red", label="ave % in random")
            plt.axis([None, None, 0, 2])
            plt.ylim(ymax = 2)
            plt.ylabel("% of mined blocks/ % of hash power")
            plt.xlabel("every 10 rounds")
            plt.title(regtable[i]+", "+str(NodeHash[i]))
            #plt.legend()
            c = c+1
    plt.savefig("North America-mix.png")
    print("North America: \t", resa, "\t", resb, "\t", resc)
    
    plt.figure(figsize=(100,100))
    c = 1
    res1 = 0
    res2 = 0
    res3 = 0
    [resa, resb, resc] = [0, 0, 0]
    for i in range(246):
        if loctable[i] == 3:
            plt.subplot(12,12,c)
            toplot = []
            for k in range(2):
                toplot.append(resultDict[i][k*5:k*5+5])
            #toplot.append([sum(resultDict[i][20:25])/5])
            res1 += sum(resultDict[i][0:5])/5
            res2 += sum(resultDict[i][15:20])/5
            #res3 += resultDict[i][k*5+5]
            if res2 > 1.1*res1:
                resa += 1
            if res2 < 0.9*res1:
                resb += 1
            resc += 1
            plt.boxplot(toplot, labels = ["random", "complete"])
            #plt.hlines(hash[i], 0, len(toplot), color = "black", label="% of hash")
            #plt.hlines(loc[i], 0, len(toplot), color = "red", label="ave % in random")
            plt.axis([None, None, 0, 2])
            plt.ylim(ymax = 2)
            plt.ylabel("% of mined blocks/ % of hash power")
            plt.xlabel("every 10 rounds")
            plt.title(regtable[i]+", "+str(NodeHash[i]))
            #plt.legend()
            c = c+1
    plt.savefig("Europe-mix.png")
    print("Europe: \t", resa, "\t", resb, "\t", resc)
    
    plt.figure(figsize=(100,100))
    c = 1
    res1 = 0
    res2 = 0
    res3 = 0
    [resa, resb, resc] = [0, 0, 0]
    for i in range(246):
        if loctable[i] == 6:
            plt.subplot(10,10,c)
            toplot = []
            for k in range(2):
                toplot.append(resultDict[i][k*5:k*5+5])
            #toplot.append([sum(resultDict[i][20:25])/5])
            res1 += sum(resultDict[i][0:5])/5
            res2 += sum(resultDict[i][15:20])/5
            #res3 += resultDict[i][k*5+5]
            if res2 > 1.1*res1:
                resa += 1
            if res2 < 0.9*res1:
                resb += 1
            resc += 1
            plt.boxplot(toplot, labels = ["random", "complete"])
            #plt.hlines(hash[i], 0, len(toplot), color = "black", label="% of hash")
            #plt.hlines(loc[i], 0, len(toplot), color = "red", label="ave % in random")
            plt.axis([None, None, 0, 2])
            plt.ylim(ymax = 2)
            plt.ylabel("% of mined blocks/ % of hash power")
            plt.xlabel("every 10 rounds")
            plt.title(regtable[i]+", "+str(NodeHash[i]))
            #plt.legend()
            c = c+1
    plt.savefig("Asia-mix.png")
    print("Asia: \t", resa, "\t", resb, "\t", resc)
    
    plt.figure(figsize=(50,50))
    c = 1
    res1 = 0
    res2 = 0
    res3 = 0
    [resa, resb, resc] = [0, 0, 0]
    for i in range(246):
        if loctable[i] == 2:
            plt.subplot(4,4,c)
            toplot = []
            for k in range(2):
                toplot.append(resultDict[i][k*5:k*5+5])
            #toplot.append([sum(resultDict[i][20:25])/5])
            res1 += sum(resultDict[i][0:5])/5
            res2 += sum(resultDict[i][15:20])/5
            #res3 += resultDict[i][k*5+5]
            if res2 > 1.1*res1:
                resa += 1
            if res2 < 0.9*res1:
                resb += 1
            resc += 1
            plt.boxplot(toplot, labels = ["random", "complete"])
            #plt.hlines(hash[i], 0, len(toplot), color = "black", label="% of hash")
            #plt.hlines(loc[i], 0, len(toplot), color = "red", label="ave % in random")
            plt.axis([None, None, 0, 2])
            plt.ylim(ymax = 2)
            plt.ylabel("% of mined blocks/ % of hash power")
            plt.xlabel("every 10 rounds")
            plt.title(regtable[i]+", "+str(NodeHash[i]))
            #plt.legend()
            c = c+1
    plt.savefig("South America-mix.png")
    print("South America: \t", resa, "\t", resb, "\t", resc)
    
    plt.figure(figsize=(50,50))
    c = 1
    res1 = 0
    res2 = 0
    res3 = 0
    [resa, resb, resc] = [0, 0, 0]
    for i in range(246):
        if loctable[i] == 5:
            plt.subplot(4,4,c)
            toplot = []
            for k in range(2):
                toplot.append(resultDict[i][k*5:k*5+5])
            #toplot.append([sum(resultDict[i][20:25])/5])
            res1 += sum(resultDict[i][0:5])/5
            res2 += sum(resultDict[i][15:20])/5
            #res3 += resultDict[i][k*5+5]
            if res2 > 1.1*res1:
                resa += 1
            if res2 < 0.9*res1:
                resb += 1
            resc += 1
            plt.boxplot(toplot, labels = ["random", "complete"])
            #plt.hlines(hash[i], 0, len(toplot), color = "black", label="% of hash")
            #plt.hlines(loc[i], 0, len(toplot), color = "red", label="ave % in random")
            plt.axis([None, None, 0, 2])
            plt.ylim(ymax = 2)
            plt.ylabel("% of mined blocks/ % of hash power")
            plt.xlabel("every 10 rounds")
            plt.title(regtable[i]+", "+str(NodeHash[i]))
            #plt.legend()
            c = c+1
    plt.savefig("Africa-mix.png")
    print("Africa: \t", resa, "\t", resb, "\t", resc)
    
    plt.figure(figsize=(50,50))
    c = 1
    res1 = 0
    res2 = 0
    res3 = 0
    [resa, resb, resc] = [0, 0, 0]
    for i in range(246):
        if loctable[i] == 4:
            plt.subplot(4,4,c)
            toplot = []
            for k in range(2):
                toplot.append(resultDict[i][k*5:k*5+5])
            #toplot.append([sum(resultDict[i][20:25])/5])
            res1 += sum(resultDict[i][0:5])/5
            res2 += sum(resultDict[i][15:20])/5
            #res3 += resultDict[i][k*5+5]
            if res2 > 1.2*res1:
                resa += 1
            if res2 < 0.9*res1:
                resb += 1
            resc += 1
            plt.boxplot(toplot, labels = ["random", "complete"])
            #plt.hlines(hash[i], 0, len(toplot), color = "black", label="% of hash")
            #plt.hlines(loc[i], 0, len(toplot), color = "red", label="ave % in random")
            plt.axis([None, None, 0, 2])
            plt.ylim(ymax = 2)
            plt.ylabel("% of mined blocks/ % of hash power")
            plt.xlabel("every 10 rounds")
            plt.title(regtable[i]+", "+str(NodeHash[i]))
            #plt.legend()
            c = c+1
    plt.savefig("Australia-mix.png")
    print("Australia: \t", resa, "\t", resb, "\t", resc)
    
