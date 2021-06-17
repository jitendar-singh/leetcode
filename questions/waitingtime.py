l = [[1,2],[2,5],[4,3]]

starttime = 0
waitingtime = 0
endtime = 0
timetaken = 0
totaltime = 0
key = 1

arrival = l[0][0] #1
timetaken = l[0][1] #2
endtime = arrival + timetaken #3# 2
waitingtime = endtime - arrival
totaltime+=waitingtime #2

while(key < len(l)): #0 
    starttime = endtime #3 8
    timetaken = l[key][1] #5 3
    endtime = (starttime+timetaken)#8 11
    waitingtime = endtime-starttime # 8-2:6 11-3:8
    totaltime+=waitingtime # 2+6+8
    print(totaltime)
    key+=1 # 1
print(totaltime/len(l))


