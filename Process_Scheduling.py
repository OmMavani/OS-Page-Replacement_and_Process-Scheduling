
#First Come First Serve Function
def fcfs(dict):
    btHold,taHold = 0,0 # tahold = completion time of perticular process
    pLine = []       # process and its completion time
    fcfsdict = {}
    for key,value in dict.items():
        at,bt = value[0],value[1]
        if (at == 0):
            taHold += bt
            fcfsdict[key] = [btHold-at,bt-at]
            pLine.append([key,taHold])
            btHold = bt
        elif(btHold-at > 0):
            taHold += bt
            fcfsdict[key] = [btHold-at,taHold-at]
            pLine.append([key,taHold])
            btHold += bt
        else:
            taHold += bt
            fcfsdict[key] = [0,bt]
            pLine.append([key,taHold+1])
            btHold += bt
    return fcfsdict,pLine


#Shortest Job First Function
def sjf(dict):
    begHold,endHold = 0,0
    sjfdict,tempdict,sortdict,pLine ={},{},{},[]
    for key,value in dict.items():
        at,bt = value[0],value[1]
        if (begHold == 0):
            endHold += bt
            sjfdict[key] = [begHold-at,bt-at]
            pLine.append([key,endHold])
            begHold = bt
        else:
            tempdict[key] = value[0],value[1]
    for key,value in sorted(tempdict.items(), key = lambda x : x[1][1]):
        sortdict[key] = value[0],value[1]
    for key,value in sortdict.items():
        at,bt = value[0],value[1]
        if(begHold-at > 0):
            endHold += bt
            sjfdict[key] = [begHold-at,endHold-at]
            pLine.append([key,endHold])
            begHold += bt
        else:
            endHold += bt
            sjfdict[key] = [0,bt]
            pLine.append([key,endHold+1])
            begHold += bt
    return sjfdict,pLine





#Round Robins
def rrobin(dict,quantum):
    begHold = 0
    rrdict,pLine = {},[]
    keyP = list(dict.keys())
    at,bt = map(list, zip(*dict.values()))
    atHold,btHold = at.copy(),bt.copy()
    while True:
        flag = True
        for i in range(len(keyP)):
            if (atHold[i] <= begHold):
                if (atHold[i] <= quantum):
                    if(btHold[i] > 0):
                        flag = False
                        if (btHold[i] > quantum):
                            begHold += quantum
                            btHold[i] -= quantum
                            atHold[i] += quantum
                            pLine.append([keyP[i],begHold])
                        else:
                            begHold += btHold[i]
                            rrdict[keyP[i]] = [begHold-bt[i]-at[i],begHold-at[i]]
                            btHold[i] = 0
                            pLine.append([keyP[i],begHold])
                elif atHold[i] > quantum:
                    for j in range(len(keyP)):
                        if (atHold[j]<atHold[i]):
                            if(btHold[j] > 0):
                                flag = False
                                if(btHold[j] > quantum):
                                    begHold += quantum
                                    btHold[j] -= quantum
                                    atHold[j] += quantum
                                    pLine.append([keyP[j],begHold])
                                else:
                                    begHold += btHold[j]
                                    rrdict[keyP[j]] = [begHold-bt[j]-at[j],begHold-at[j]]
                                    btHold[j] = 0
                                    pLine.append([keyP[j],begHold])
                    if(btHold[i]>0):
                        flag = False
                        if(btHold[i]>quantum):
                            begHold += quantum
                            btHold[i] -= quantum
                            atHold[i] += quantum
                            pLine.append([keyP[i],begHold])
                        else:
                            begHold += btHold[i]
                            rrdict[keyP[i]] = [begHold-bt[i]-at[i],begHold-at[i]]
                            btHold[i] = 0
                            pLine.append([keyP[i],begHold])
            elif(atHold[i]>begHold):
                begHold += 1
                i -= 1
        if(flag):
            break
    return rrdict,pLine


#Shortest Remaining Time First Function
def srtf(dict):
    begHold,endHold = 0,0
    srtfdict,tempdict,sortdict,pLine = {},{},{},[]
    for key,value in dict.items():
        at,bt = value[0],value[1]
        if (begHold == 0):
            second = list(dict.values())[1]
            srtfdict[key] = [begHold-at, bt-second[0]-at]
            endHold += bt-second[0]
            begHold = bt-second[0]
            tempdict[key] = at, bt-begHold
            pLine.append([key,endHold])
        else:
            tempdict[key] = at,bt
    for key,value in reversed(sorted(tempdict.items(), key = lambda x : x[1][1],reverse=True)):
        sortdict[key] = value[0],value[1]
    for key,value in sortdict.items():
        at,bt = value[0], value[1]
        if key in srtfdict.keys():
            hold = srtfdict[key]
            endHold += bt
            srtfdict[key] = [begHold-hold[1],endHold-at]
            pLine.append([key,endHold])
            begHold += bt
        elif(begHold-at > 0):
            endHold += bt
            srtfdict[key] = [begHold-at,endHold-at]
            pLine.append([key,endHold])
            begHold += bt
        else:
            endHold += bt
            srtfdict[key] = [0,bt]
            pLine.append([key,endHold+1])
            begHold += bt
    return srtfdict, pLine


#Print Function + Calculation
def printData(gData, cData, pLine, Name):
    avgWT,avgTT =0,0
    plinestr= "0 -> "
    print(Name.upper())
    print('| KEY | ARRIVAL | BURST | WAIT | TURNAROUND |')
    for key,value in sorted(cData.items()):
        print('{:>4}{:>8}{:>9}{:>8}{:>10}'.format(key,gData[key][0],gData[key][1],value[0],value[1]))
        avgWT += value[0]
        avgTT += value[1]
    print('\nAverage Wait Time = {} \nAverage Turnaround Time = {}\n'.format(avgWT/len(cData),avgTT/len(cData)))
    for x in pLine:
        plinestr += ('{} -> {} -> '.format(x[0],x[1]))
    print('{}\n'.format(plinestr[:-3]))


process = []
arrivaltime = []
bursttime = []

print("--------------------------------------------------------------------")
no_processes = int(input("Enter Total Number Of Process : "))
print("--------------------------------------------------------------------")

for i in range(no_processes):
    print("################ PROCESS NO {} : ".format(i + 1))
    s='P'+str(i+1)
    process.append(s)
    arrivaltime.append(int(input("Arrival Time : ")))
    bursttime.append(int(input("Burst Time   : ")))

gData={}
for i in range(len(process)):
    gData[process[i]] = [arrivaltime[i],bursttime[i]]
gContSwitch = 0.4


while True:
    print("---------------------------MENU----------------------------")
    print("1. FCFS")
    print("2. SJF")
    print("3. SRTF")
    print("4. RR")
    print("5. Exit")
    c = int(input("Enter choice: "))
    print()
    if c == 1:
        fcfsScheduling,fcfsLine = fcfs(gData)
        printData(gData, fcfsScheduling, fcfsLine, 'First Come First Serve')
        print()
    elif c == 2:
        sjfScheduling,sjfLine = sjf(gData)
        printData(gData, sjfScheduling, sjfLine, 'Shortest Job First')
        print()
    elif c == 3:
        srtfScheduling, srtfLine = srtf(gData)
        printData(gData, srtfScheduling, srtfLine, 'Shortest Remaning Time First')
        print()
    elif c == 4:
        gQuant = int(input("Time Qauntum : "))
        rrobinScheduling,rrLine = rrobin(gData,gQuant)
        printData(gData, rrobinScheduling, rrLine, 'Round Robin QT={}'.format(gQuant))
        print()
    elif c == 5:
        exit()
    else:
        print("Enter valid choice!")