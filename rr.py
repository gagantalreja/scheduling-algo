import matplotlib.pyplot as plt

def RR(n, burst, arrival, tq):

    ct, tat, wt, gantt = [0]*n, [0]*n, [0]*n, []
    barr = list(zip(list(range(n)), burst, arrival))
    barr = sorted(barr, key = lambda x: x[2])
    barr = [list(i) for i in barr]
    print(barr)
    t=barr[0][2]
    tt=[0]*n
    for i in barr: tt[i[0]] = i[2]
    ready=[]
    curr=0.0
    comp_flg=0
    gantt.append([-999999, -999999])
    gantt_ind=0
    
    while comp_flg<n:

        i=0
        add=tq
        while i<len(barr):
            if barr[i][2]<curr:
                ready.insert(len(ready)-1, barr.pop(i))
            elif barr[i][2]==curr:
                ready.append(barr.pop(i))
            else:
                i+=1
        print(ready, curr)
        if ready==[]:
            curr+=1
            continue
        
        if ready[0][1]>tq:
            ready[0][1]-=tq
            curr+=tq
            k=ready.pop(0)
            ready.append(k)

        else:
            curr+=ready[0][1]
            add=ready[0][1]
            ct[ready[0][0]] = curr
            tat[ready[0][0]] = ct[ready[0][0]] - ready[0][2]
            wt[ready[0][0]] = tat[ready[0][0]] - burst[ready[0][0]]
            k = ready.pop(0)
            comp_flg+=1
        
        if k[0]!=gantt[gantt_ind][0]:
            gantt.append([k[0], curr])
            gantt_ind+=1                
        else:
            gantt[gantt_ind][1]+=add


    gantt=gantt[1::]
    print(ct, tat, wt, gantt)
    color=('pink', 'lightgreen', 'gold', 'violet')
    ax = plt.subplot(111)
    plotting=[]
    names = []
    for i in range(len(gantt)):
        if i==0:
            plotting.append((t, gantt[i][1]-t, "P"+str(gantt[i][0])))
        else:
            q=gantt[i-1][1] if gantt[i-1][1]>tt[gantt[i][0]] else tt[gantt[i][0]]
            plotting.append((q, gantt[i][1]-q, "P"+str(gantt[i][0])))
    print(plotting)

    #ax.broken_barh(list(map(lambda v: v[:2], plotting)), (3, 4), facecolors=color)
    i=0
    for v in plotting:
        ax.barh(left=v[0], width=v[1], y=3, height=4, facecolor=color[i%4], align='edge')
        i=i+1
        anno = ax.annotate(v[2], xy=((2*v[0]+v[1])/2, 5))

    ax.set_xlim(0, plotting[-1][1])
    ax.set_xlabel('Time (in milliseconds)')
    ax.set_yticks(list(range(0, 11)))
    ax.xaxis.grid(True)
    ax.set_xticks([x[0] for x in plotting]+[x[1]+x[0] for x in plotting])
    ax.set_title("Round Robin Scheduling\nAverage Waiting Time: "+str(round(sum(wt)/len(wt), 2))+
      " , Average Turnaround Time: "+str(round(sum(tat)/len(tat), 2)))
    plt.show()
    
def main():

       n = int(input("No. of processes: "))
       tq = float(input("Time Quantum: "))
       f = open("q.txt", 'r')
       burst, arrival = f.read().split("\n")[:2]
       burst = list(map(float, burst.split()))
       arrival = list(map(float, arrival.split()))
       RR(n, burst, arrival, tq)
       
main()
