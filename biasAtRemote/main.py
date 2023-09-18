
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np
    
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
    resultDict2 = {}
    for i in range(246):
        resultDict[i] = []
    for readfile in ["as3.txt", "as6.txt", "as12.txt", "as24.txt", "ascom.txt"]:
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
        for count in blkdict.keys():
            buff = [0 for _ in range(246)]
            bufflen = len(blkdict[count])
            for item in blkdict[count]:
                buff[item] += 1
            for j in range(246):
                resultDict[j].append(int(buff[j]/bufflen*10000)/100)
    
    plt.figure(figsize=(100,60))
    c = 1
    res1 = 0
    res2 = 0
    res3 = 0
    [resa, resb, resc] = [0, 0, 0]
    plt.subplot(2,5,1)
    i = 5
    toplot = []
    for k in range(5):
        toplot.append(resultDict[i][k*5:k*5+5])
    plt.boxplot(toplot, labels = ['3 nbr',' 6 nbr', '12 nbr', '24 nbr', '48 nbr'])
    plt.axis([None, None, 0, 1.5])
    plt.ylim(ymax = 1.5)
    plt.ylabel("% of mined blocks/ % of hash power")
    plt.title(regtable[i]+", "+str(i))
    c = c+1
    
    plt.subplot(2,5,2)
    i = 8
    toplot = []
    for k in range(5):
        toplot.append(resultDict[i][k*5:k*5+5])
    plt.boxplot(toplot, labels = ['3 nbr',' 6 nbr', '12 nbr', '24 nbr', '48 nbr'])
    plt.axis([None, None, 0, 1.5])
    plt.ylim(ymax = 1.5)
    plt.ylabel("% of mined blocks/ % of hash power")
    plt.title(regtable[i]+", "+str(i))
    c = c+1
    
    plt.subplot(2,5,6)
    i = 83
    toplot = []
    for k in range(5):
        toplot.append(resultDict[i][k*5:k*5+5])
    plt.boxplot(toplot, labels = ['3 nbr',' 6 nbr', '12 nbr', '24 nbr', '48 nbr'])
    plt.axis([None, None, 0, 1.5])
    plt.ylim(ymax = 1.5)
    plt.ylabel("% of mined blocks/ % of hash power")
    plt.title(regtable[i]+", "+str(i))
    c = c+1
    
    plt.subplot(2,5,7)
    i = 85
    toplot = []
    for k in range(5):
        toplot.append(resultDict[i][k*5:k*5+5])
    plt.boxplot(toplot, labels = ['3 nbr',' 6 nbr', '12 nbr', '24 nbr', '48 nbr'])
    plt.axis([None, None, 0, 1.5])
    plt.ylim(ymax = 1.5)
    plt.ylabel("% of mined blocks/ % of hash power")
    plt.title(regtable[i]+", "+str(i))
    c = c+1
    resultDict = {}
    resultDict2 = {}
    for i in range(246):
        resultDict2[i] = []
    for readfile in ["as6.txt", "complete.txt", "completeAtRemoteResult.txt"]:
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
        for count in blkdict.keys():
            buff = [0 for _ in range(246)]
            bufflen = len(blkdict[count])
            for item in blkdict[count]:
                buff[item] += 1
            for j in range(246):
                #print(j,int(buff[j]/bufflen*10000))
                resultDict2[j].append(int(buff[j]/bufflen*10000)/100)
    
    c = 1
    res1 = 0
    res2 = 0
    res3 = 0
    [resa, resb, resc] = [0, 0, 0]
    plt.subplot(2,5,3)
    i = 5
    toplot2 = [resultDict2[i][0:5], [resultDict2[i][5]], resultDict2[i][6:11]]
    plt.boxplot(toplot2, labels = ["random", "complete", "interconnect at remote clusters"])
    plt.axis([None, None, 0, 1.5])
    plt.ylim(ymax = 1.5)
    plt.ylabel("% of mined blocks/ % of hash power")
    plt.title(regtable[i]+", "+str(i))
    c = c+1
    
    plt.subplot(2,5,4)
    i = 8
    toplot2 = [resultDict2[i][0:5], [resultDict2[i][5]], resultDict2[i][6:11]]
    plt.boxplot(toplot2, labels = ["random", "complete", "interconnect at remote clusters"])
    plt.axis([None, None, 0, 1.5])
    plt.ylim(ymax = 1.5)
    plt.ylabel("% of mined blocks/ % of hash power")
    plt.title(regtable[i]+", "+str(i))
    c = c+1
    
    plt.subplot(2,5,8)
    i = 83
    toplot2 = [resultDict2[i][0:5], [resultDict2[i][5]], resultDict2[i][6:11]]
    plt.boxplot(toplot2, labels = ["random", "complete", "interconnect at remote clusters"])
    plt.axis([None, None, 0, 1.5])
    plt.ylim(ymax = 1.5)
    plt.ylabel("% of mined blocks/ % of hash power")
    plt.title(regtable[i]+", "+str(i))
    c = c+1
    
    plt.subplot(2,5,9)
    i = 85
    toplot2 = [resultDict2[i][0:5], [resultDict2[i][5]], resultDict2[i][6:11]]
    plt.boxplot(toplot2, labels = ["random", "complete", "interconnect at remote clusters"])
    plt.axis([None, None, 0, 1.5])
    plt.ylim(ymax = 1.5)
    plt.ylabel("% of mined blocks/ % of hash power")
    plt.title(regtable[i]+", "+str(i))
    c = c+1
    
    plt.subplot(2,5,5)
    i = 60
    toplot2 = [resultDict2[i][0:5], [resultDict2[i][5]], resultDict2[i][6:11]]
    plt.boxplot(toplot2, labels = ["random", "complete", "interconnect at remote clusters"])
    plt.axis([None, None, 0, 1.5])
    plt.ylim(ymax = 1.5)
    plt.ylabel("% of mined blocks/ % of hash power")
    plt.title(regtable[i]+", "+str(i))
    c = c+1
    
    plt.subplot(2,5,10)
    i = 47
    toplot2 = [resultDict2[i][0:5], [resultDict2[i][5]], resultDict2[i][6:11]]
    plt.boxplot(toplot2, labels = ["random", "complete", "interconnect at remote clusters"])
    plt.axis([None, None, 0, 1.5])
    plt.ylim(ymax = 1.5)
    plt.ylabel("% of mined blocks/ % of hash power")
    plt.title(regtable[i]+", "+str(i))
    c = c+1
    
    plt.savefig("biasAtRemote.png")

    

