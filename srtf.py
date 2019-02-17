import matplotlib.pyplot as plt
def SRTF(n, burst, arrival):

        barr = list(zip(list(range(n)), burst, arrival))
        barr = sorted(barr, key = lambda x: (x[2], x[1]))
        barr = [list(i) for i in barr]
        t=barr[0][2]
        tt=[0]*n
        for i in barr: tt[i[0]] = i[2]
        comp_flg = 0
        arrived, ct, tat, wt, gantt = [], [0]*n, [0]*n, [0]*n, []
        curr = 0.0
        print(barr)
        gantt_ind=0
        gantt.append([-99999, -999999])
        while comp_flg!=n:

                i=0
                while i<len(barr):
                        if barr[i][2]<=curr:
                            arrived.append(barr.pop(i))
                        else:
                            i+=1
                            
                if arrived==[]:
                        curr+=1
                        continue
                m=min(arrived, key=lambda x:x[1])
                k=arrived.index(m)
                arrived[k][1]-=1
                curr+=1


                if arrived[k][0]!=gantt[gantt_ind][0]:
                        gantt.append([arrived[k][0], curr])
                        gantt_ind+=1                
                else:
                        gantt[gantt_ind][1]+=1
                            
                if arrived[k][1]==0:
                        comp_flg+=1
                        ct[arrived[k][0]]=curr
                        tat[arrived[k][0]]=ct[arrived[k][0]]-arrived[k][2]
                        wt[arrived[k][0]]=tat[arrived[k][0]]-burst[arrived[k][0]]
                        arrived.pop(k)

        gantt=gantt[1::]
        print(ct, tat, wt, gantt)
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
                anno = ax.annotate(v[2], xy=((2*v[0]+v[1])/2, 5))

        ax.set_xlim(0, plotting[-1][1])
        ax.set_xlabel('Time (in milliseconds)')
        ax.set_yticks(list(range(0, 11)))
        ax.xaxis.grid(True)
        ax.set_xticks([x[0] for x in plotting]+[x[1]+x[0] for x in plotting])
        ax.set_title("Shortest Remaining Time First\nAverage Waiting Time: "+str(round(sum(wt)/len(wt), 2))+
                 " , Average Turnaround Time: "+str(round(sum(tat)/len(tat), 2)))
        plt.show()
        
def main():

       n = int(input("No. of processes: "))
       f = open("q.txt", 'r')
       burst, arrival = f.read().split("\n")[:2]
       burst = list(map(float, burst.split()))
       arrival = list(map(float, arrival.split()))
       SRTF(n, burst, arrival)
       
main()
