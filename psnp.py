import matplotlib.pyplot as plt
def PSNP(n, burst, arrival, priority):

    ct, tat, wt, gantt = [0]*n, [0]*n, [0]*n, []
    barr = list(zip(list(range(n)), burst, arrival, priority))
    barr = sorted(barr, key = lambda x: (x[2], x[3]))
    t=barr[0][2]
    tt=[0]*n
    for i in barr:
        tt[i[0]] = i[2]
    print(barr, tt)
    arrived, i = [], 0
    
    comp_flg=0
    curr=0.0
    
    while comp_flg!=n:

        print(curr, comp_flg)
        while barr!=[] and barr[0][2]<=curr:
            arrived.append(barr.pop(0))

        if arrived==[]:
            curr+=1
            continue
        
        arrived = sorted(arrived, key = lambda x: (x[3]))
        print(arrived)
        curr+=arrived[0][1]
        comp_flg+=1
        ct[arrived[0][0]]=curr
        tat[arrived[0][0]] = curr - arrived[0][2]
        wt[arrived[0][0]] = tat[arrived[0][0]] - arrived[0][1]
        k = arrived.pop(0)
        gantt.append([k[0], curr])

    color=('pink', 'lightgreen', 'gold', 'violet')
    ax = plt.subplot(111)
    plotting=[]
    names = []
    print(gantt)
    for i in range(len(gantt)):
        if i==0:
            plotting.append((t, gantt[i][1]-t, "P"+str(gantt[i][0])))
        else:
            print(gantt[i][0])
            q=gantt[i-1][1] if gantt[i-1][1]>tt[gantt[i][0]] else tt[gantt[i][0]]
            plotting.append((q, gantt[i][1]-q, "P"+str(gantt[i][0])))
    print(plotting)
        
    #ax.broken_barh(list(map(lambda v: v[:2], plotting)), (3, 4), facecolors=color)
    i=0
    for v in plotting:
        ax.barh(left=v[0], width=v[1], y=3, height=4, facecolor=color[i%4], align='edge')
        i=i+1
        if i==5:
            i=0
        anno = ax.annotate(v[2], xy=((2*v[0]+v[1])/2, 5))
        
    ax.set_xlim(0, plotting[-1][1])
    ax.set_xlabel('Time (in milliseconds)')
    ax.set_yticks(list(range(0, 11)))
    ax.xaxis.grid(True)
    ax.set_xticks([x[0] for x in plotting]+[x[1]+x[0] for x in plotting])
    ax.set_title("Priority Scheduling\nAverage Waiting Time: "+str(round(sum(wt)/len(wt), 2))+
                 " , Average Turnaround Time: "+str(round(sum(tat)/len(tat), 2)))
    plt.show()
    
def main():

       n = int(input("No. of processes: "))
       priority = list(map(int, input("Priority for processes P1, P2, ...., Pn respectively (lower the number, higher the priority): ").split()))
       f = open("q.txt", 'r')
       burst, arrival = f.read().split("\n")[:2]
       burst = list(map(float, burst.split()))
       arrival = list(map(float, arrival.split()))
       PSNP(n, burst, arrival, priority)
       
main()
