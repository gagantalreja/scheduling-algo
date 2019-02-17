from PyQt5 import QtCore, QtGui, QtWidgets,QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import qdarkstyle
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib
import matplotlib.pyplot as plt
import warnings
import warnings
warnings.filterwarnings('ignore')
StyleSheet = '''
QPushButton#btn {
     /* Green */
  font:bold;
  color: white;
  text-align: center;
  text-decoration: none;
  background-color:chocolate;
  font-family:Georgia;
}

QPushButton#btn:hover {
    background-color: black;
    border: 0.5px  solid burlywood;
    color: #fff;
}

QPushButton#btn:pressed {
    background-color: orange;
}
QPushButton#btn1{
background-color:Teal;
font-family:Georgia;
font:bold;
color:black;
}
QPushButton#btn1:hover {
background-color:black;
color:white;
font-family:Georgia;
font:bold;
}

QPushButton#btn1:pressed {
    background-color: red;
    font-family:Georgia;
    font:bold;
}
QPushButton#btn2 {
     /* Green */
  font:bold;
  color: white;
  text-align: center;
  text-decoration: none;
  background-color:Teal;
  font-family:Georgia;
}
QPushButton#btn2:hover {
background-color:black;
color:white;
font-family:Georgia;
font:bold;
}
QPushButton#btn3{
background-color:CadetBlue ;
font-family:Georgia;
font:bold;
color:black;
}
QPushButton#btn3:hover {
background-color:black;
color:white;
font-family:Georgia;
font:bold;
}

QPushButton#btn3:pressed {
    background-color: red;
    font-family:Georgia;
    font:bold;
}

QPushButton#btn4{
background-color:red;
font-family:Georgia;
font:bold;
color:black;
}
QPushButton#btn4:hover {
background-color:black;
color:white;
font-family:Georgia;
font:bold;
}

QPushButton#btn4:pressed {
    background-color: red;
    font-family:Georgia;
    font:bold;
}
QPushButton#btn5{
background-color:salmon;
font-family:Georgia;
font:bold;
color:black;
}
QPushButton#btn5:hover {
background-color:black;
color:white;
font-family:Georgia;
font:bold;
}
QPushButton#btn5:pressed {
    background-color: red;
    font-family:Georgia;
    font:bold;
}
QPushButton#upld{
background-color:BlueViolet ;
font-family:Georgia;
font:bold;
color:black;
}
QPushButton#upld:hover {
background-color:black;
color:white;
font-family:Georgia;
font:bold;
}

QPushButton#upld:pressed {
    background-color: red;
    font-family:Georgia;
    font:bold;
}

QPushButton#OK{
background-color:green ;
font-family:Georgia;
font:bold;
color:black;
}
QPushButton#OK:hover {
background-color:black;
color:white;
font-family:Georgia;
font:bold;
}

QPushButton#OK:pressed {
    background-color: red;
    font-family:Georgia;
    font:bold;
}
 '''
class GRAPH(QtWidgets.QWidget):
    filename=None
    def __init__(self,filename, parent=None):
        super().__init__()
        layout = QVBoxLayout()
        GRAPH.filename=filename
        # a figure instance to plot on
        #self.figure = plt.figure()
        self.setGeometry(30,30,1200,695)
        self.setWindowTitle("ALGORITHMS")

        tab=QTabWidget(self)
        #tab.setStyleSheet("QTabWidget{}")
        #tab.addTab(SecondTab(),"GRAPH")
        tab.addTab(FCFS(),"FCFS")

        layout.addWidget(tab)

        self.setLayout(layout)
class FCFS(QWidget):
    def __init__(self):
        super().__init__()
        self.filename=GRAPH.filename
        layout = QVBoxLayout()
        hlayout=QHBoxLayout()
        self.figure = plt.figure()

        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumSize(1100,560)

        hlayout1=QHBoxLayout()
        self.toolbar = NavigationToolbar(self.canvas, self)
        hlayout1.setAlignment(QtCore.Qt.AlignBottom)
        self.input=QLineEdit(self)
        self.input.setPlaceholderText("Enter Number of Processes")
        hlayout.addWidget(self.input)
        self.input.setMaximumSize(150,30)
        hlayout.setAlignment(QtCore.Qt.AlignLeft)
        self.ok=QPushButton("OK",self,objectName="OK")
        self.ok.setStyleSheet(StyleSheet)
        hlayout.addWidget(self.ok)
        self.ok.setMaximumSize(80,30)
        layout.addLayout(hlayout)
        layout.addLayout(hlayout1)
        hlayout1.addWidget(self.canvas)
        layout.addWidget(self.toolbar)
        layout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(layout)
        self.ok.clicked.connect(self.plot)
    def plot(self):
        try:
            n = self.input.text()
            n=int(n)
            f = open(self.filename,"r")
            burst, arrival = f.read().split("\n")[:2]
            burst = list(map(float, burst.split()))
            arrival = list(map(float, arrival.split()))
            self.plot_fcfs(n, burst, arrival)
        except:
            QMessageBox.information(self, 'Alert',"Invalid User Input", QMessageBox.Ok)
    def plot_fcfs(self,n, burst, arrival):
        self.figure.clear()
        ax=self.figure.add_subplot(111)
        barr = list(zip(list(range(n)), burst, arrival))
        barr = sorted(barr, key = lambda x: x[2])
        ct, tat, wt, gantt = [0]*n, [0]*n, [0]*n, []
        t=barr[0][2]
        tt=[0]*n

        for i in barr: tt[i[0]] = i[2]
        curr=barr[0][2]
        comp_flg=0
        i=0
        while comp_flg!=n:

            if curr<barr[i][2]: curr+=1
            else:
                curr+=barr[i][1]
                ct[barr[i][0]]=curr
                tat[barr[i][0]] = curr - barr[i][2]
                wt[barr[i][0]] = curr - barr[i][2] - barr[i][1]
                comp_flg+=1
                i=i+1

        gantt = [[i, ct[i]] for i in range(len(ct))]
        gantt = sorted(gantt, key = lambda x: x[1])


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
        ax.set_title("First Come, First Serve\nAverage Waiting Time: "+str(round(sum(wt)/len(wt), 2))+
          " , Average Turnaround Time: "+str(round(sum(tat)/len(tat), 2)))
        self.canvas.draw()


class GRAPH2(QtWidgets.QWidget):
    filename=None
    def __init__(self,filename, parent=None):
        super().__init__()
        layout = QVBoxLayout()
        GRAPH.filename=filename
        # a figure instance to plot on
        #self.figure = plt.figure()
        self.setGeometry(30,30,1200,695)
        self.setWindowTitle("ALGORITHMS")

        tab=QTabWidget(self)
        #tab.setStyleSheet("QTabWidget{}")
        #tab.addTab(SecondTab(),"GRAPH")
        tab.addTab(PSNP(),"PSNP")

        layout.addWidget(tab)

        self.setLayout(layout)
class PSNP(QWidget):
    def __init__(self):
        super().__init__()
        self.filename=GRAPH.filename
        layout = QVBoxLayout()
        hlayout=QHBoxLayout()
        self.figure = plt.figure()

        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumSize(1100,560)

        hlayout1=QHBoxLayout()
        self.toolbar = NavigationToolbar(self.canvas, self)
        hlayout1.setAlignment(QtCore.Qt.AlignBottom)
        self.input=QLineEdit(self)
        self.input.setPlaceholderText("Enter Number of Processes")
        hlayout.addWidget(self.input)
        self.input.setMaximumSize(150,30)
        self.priority=QLineEdit(self)
        self.priority.setPlaceholderText("Priority for processes P1, P2, ...., Pn respectively (lower the number, higher the priority)")
        hlayout.addWidget(self.priority)

        hlayout.setAlignment(QtCore.Qt.AlignLeft)
        self.ok=QPushButton("OK",self,objectName="OK")
        hlayout.addWidget(self.ok)
        self.ok.setMaximumSize(80,30)
        self.ok.setStyleSheet(StyleSheet)
        layout.addLayout(hlayout)
        layout.addLayout(hlayout1)
        hlayout1.addWidget(self.canvas)
        layout.addWidget(self.toolbar)
        layout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(layout)
        self.ok.clicked.connect(self.plot)
    def plot(self):
        try:
            n=int(self.input.text())
            h=self.priority.text()
            h=h.split()
            priority=list(map(int,h))
            if len(priority)<n:
                QMessageBox.information(self, 'Alert',"Number of priority values should be = "+str(n), QMessageBox.Ok)
            else:
                f=open(self.filename,"r")
                burst, arrival = f.read().split("\n")[:2]
                burst = list(map(float, burst.split()))
                arrival = list(map(float, arrival.split()))
                self.plot_psnp(n, burst, arrival, priority)
        except:
            QMessageBox.information(self, 'Alert',"Invalid User Input", QMessageBox.Ok)
    def plot_psnp(self,n, burst, arrival, priority):
        self.figure.clear()
        ax=self.figure.add_subplot(111)
        ct, tat, wt, gantt = [0]*n, [0]*n, [0]*n, []
        barr = list(zip(list(range(n)), burst, arrival, priority))
        barr = sorted(barr, key = lambda x: (x[2], x[3]))
        t=barr[0][2]
        tt=[0]*n
        for i in barr:
            tt[i[0]] = i[2]

        arrived, i = [], 0

        comp_flg=0
        curr=0.0

        while comp_flg!=n:

            #print(curr)
            while barr!=[] and barr[0][2]<=curr:
                arrived.append(barr.pop(0))

            if arrived==[]:
                curr+=1
                continue

            arrived = sorted(arrived, key = lambda x: (x[3]))
            #print(arrived)
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

        for i in range(len(gantt)):
            if i==0:
                plotting.append((t, gantt[i][1]-t, "P"+str(gantt[i][0])))
            else:
                #print(gantt[i][0])
                q=gantt[i-1][1] if gantt[i-1][1]>tt[gantt[i][0]] else tt[gantt[i][0]]
                plotting.append((q, gantt[i][1]-q, "P"+str(gantt[i][0])))


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
        self.canvas.draw()
class GRAPH3(QtWidgets.QWidget):
    filename=None
    def __init__(self,filename, parent=None):
        super().__init__()
        layout = QVBoxLayout()
        GRAPH.filename=filename

        self.setGeometry(30,30,1200,695)
        self.setWindowTitle("ALGORITHMS")

        tab=QTabWidget(self)

        tab.addTab(ROBIN(),"ROUND ROBIN")

        layout.addWidget(tab)

        self.setLayout(layout)
class ROBIN(QWidget):
    def __init__(self):
        super().__init__()
        self.filename=GRAPH.filename
        layout = QVBoxLayout()
        hlayout=QHBoxLayout()
        self.figure = plt.figure()

        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumSize(1100,560)

        hlayout1=QHBoxLayout()
        self.toolbar = NavigationToolbar(self.canvas, self)
        hlayout1.setAlignment(QtCore.Qt.AlignBottom)
        self.input=QLineEdit(self)
        self.input.setPlaceholderText("Enter Number of Processes")
        hlayout.addWidget(self.input)
        self.input.setMaximumSize(150,30)
        self.time=QLineEdit(self)
        self.time.setPlaceholderText("Enter Time Quantum")
        hlayout.addWidget(self.time)
        self.time.setMaximumSize(120,30)
        hlayout.setAlignment(QtCore.Qt.AlignLeft)
        self.ok=QPushButton("OK",self,objectName="OK")
        hlayout.addWidget(self.ok)
        self.ok.setMaximumSize(80,30)
        self.ok.setStyleSheet(StyleSheet)
        layout.addLayout(hlayout)
        layout.addLayout(hlayout1)
        hlayout1.addWidget(self.canvas)
        layout.addWidget(self.toolbar)
        layout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(layout)
        self.ok.clicked.connect(self.plot)
    def plot(self):
        try:
            n=int(self.input.text())
            tq=self.time.text()
            if tq=='':
                QMessageBox.information(self, 'Alert',"Enter Time Quantum", QMessageBox.Ok)
            else:
                tq=float(self.time.text())
                f=open(self.filename,"r")
                burst, arrival = f.read().split("\n")[:2]
                burst = list(map(float, burst.split()))
                arrival = list(map(float, arrival.split()))
                self.plot_round(n, burst, arrival, tq)
        except:
            QMessageBox.information(self, 'Alert',"Invalid User Input", QMessageBox.Ok)
    def plot_round(self,n, burst, arrival, tq):
        self.figure.clear()
        ax=self.figure.add_subplot(111)
        ct, tat, wt, gantt = [0]*n, [0]*n, [0]*n, []
        barr = list(zip(list(range(n)), burst, arrival))
        barr = sorted(barr, key = lambda x: x[2])
        barr = [list(i) for i in barr]
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
            #print(ready, curr)
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
        self.canvas.draw()
class GRAPH4(QtWidgets.QWidget):
    filename=None
    def __init__(self,filename, parent=None):
        super().__init__()
        layout = QVBoxLayout()
        GRAPH.filename=filename

        self.setGeometry(30,30,1200,695)
        self.setWindowTitle("ALGORITHMS")

        tab=QTabWidget(self)

        tab.addTab(SJF(),"SJF")

        layout.addWidget(tab)

        self.setLayout(layout)
class SJF(QWidget):
    def __init__(self):
        super().__init__()
        self.filename=GRAPH.filename
        layout = QVBoxLayout()
        hlayout=QHBoxLayout()
        self.figure = plt.figure()

        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumSize(1100,560)

        hlayout1=QHBoxLayout()
        self.toolbar = NavigationToolbar(self.canvas, self)
        hlayout1.setAlignment(QtCore.Qt.AlignBottom)
        self.input=QLineEdit(self)
        self.input.setPlaceholderText("Enter Number of Processes")
        hlayout.addWidget(self.input)
        self.input.setMaximumSize(150,30)
        hlayout.setAlignment(QtCore.Qt.AlignLeft)
        self.ok=QPushButton("OK",self,objectName="OK")
        hlayout.addWidget(self.ok)
        self.ok.setMaximumSize(80,30)
        self.ok.setStyleSheet(StyleSheet)
        layout.addLayout(hlayout)
        layout.addLayout(hlayout1)
        hlayout1.addWidget(self.canvas)
        layout.addWidget(self.toolbar)
        layout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(layout)
        self.ok.clicked.connect(self.plot)
    def plot(self):
        try:
            n=int(self.input.text())
            f=open(self.filename,"r")
            burst, arrival = f.read().split("\n")[:2]
            burst = list(map(float, burst.split()))
            arrival = list(map(float, arrival.split()))
            self.plot_sjf(n, burst, arrival)
        except:
            QMessageBox.information(self, 'Alert',"Invalid User Input", QMessageBox.Ok)
    def plot_sjf(self,n, burst, arrival):
            self.figure.clear()
            ax=self.figure.add_subplot(111)
            ct, tat, wt, gantt = [0]*n, [0]*n, [0]*n, []
            barr = list(zip(list(range(n)), burst, arrival))
            barr = sorted(barr, key = lambda x: (x[2], x[1]))
            t=barr[0][2]
            tt=[0]*n
            #print(barr)
            for i in barr: tt[i[0]] = i[2]
            curr=barr[0][2]
            comp_flg=0
            i=0
            while comp_flg!=n:

                    if curr<barr[i][2]: curr+=1
                    else:
                            curr+=barr[i][1]
                            ct[barr[i][0]]=curr
                            tat[barr[i][0]] = curr - barr[i][2]
                            wt[barr[i][0]] = curr - barr[i][2] - barr[i][1]
                            comp_flg+=1
                            i=i+1

            gantt = [[i, ct[i]] for i in range(len(ct))]
            gantt = sorted(gantt, key = lambda x: x[1])

            #print(ct, tat, wt, gantt)
            color=('pink', 'lightgreen', 'gold', 'violet')
            ax = plt.subplot(111)
            plotting=[]
            names = []
            #print(gantt)
            for i in range(len(gantt)):
                    if i==0:
                        plotting.append((t, gantt[i][1]-t, "P"+str(gantt[i][0])))
                    else:
                        #print(gantt[i][0])
                        q=gantt[i-1][1] if gantt[i-1][1]>tt[gantt[i][0]] else tt[gantt[i][0]]
                        plotting.append((q, gantt[i][1]-q, "P"+str(gantt[i][0])))

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
            ax.set_title("Shortest Job First\nAverage Waiting Time: "+str(round(sum(wt)/len(wt), 2))+
                     " , Average Turnaround Time: "+str(round(sum(tat)/len(tat), 2)))
            self.canvas.draw()
class GRAPH5(QtWidgets.QWidget):
    filename=None
    def __init__(self,filename, parent=None):
        super().__init__()
        layout = QVBoxLayout()
        GRAPH.filename=filename
        # a figure instance to plot on
        #self.figure = plt.figure()
        self.setGeometry(30,30,1200,695)
        self.setWindowTitle("ALGORITHMS")

        tab=QTabWidget(self)
        #tab.setStyleSheet("QTabWidget{}")
        #tab.addTab(SecondTab(),"GRAPH")
        tab.addTab(SRTF(),"SRTF")

        layout.addWidget(tab)

        self.setLayout(layout)
class SRTF(QWidget):
    def __init__(self):
        super().__init__()
        self.filename=GRAPH.filename
        layout = QVBoxLayout()
        hlayout=QHBoxLayout()
        self.figure = plt.figure()

        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumSize(1100,560)

        hlayout1=QHBoxLayout()
        self.toolbar = NavigationToolbar(self.canvas, self)
        hlayout1.setAlignment(QtCore.Qt.AlignBottom)
        self.input=QLineEdit(self)
        self.input.setPlaceholderText("Enter Number of Processes")
        hlayout.addWidget(self.input)
        self.input.setMaximumSize(150,30)
        hlayout.setAlignment(QtCore.Qt.AlignLeft)
        self.ok=QPushButton("OK",self,objectName="OK")
        hlayout.addWidget(self.ok)
        self.ok.setMaximumSize(80,30)
        self.ok.setStyleSheet(StyleSheet)
        layout.addLayout(hlayout)
        layout.addLayout(hlayout1)
        hlayout1.addWidget(self.canvas)
        layout.addWidget(self.toolbar)
        layout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(layout)
        self.ok.clicked.connect(self.plot)
    def plot(self):
        try:
            n=int(self.input.text())
            f=open(self.filename,"r")
            burst, arrival = f.read().split("\n")[:2]
            burst = list(map(float, burst.split()))
            arrival = list(map(float, arrival.split()))
            self.plot_srtf(n, burst, arrival)
        except:
            QMessageBox.information(self, 'Alert',"Invalid User Input", QMessageBox.Ok)
    def plot_srtf(self,n, burst, arrival):
        self.figure.clear()
        ax=self.figure.add_subplot(111)
        barr = list(zip(list(range(n)), burst, arrival))
        barr = sorted(barr, key = lambda x: (x[2], x[1]))
        barr = [list(i) for i in barr]
        t=barr[0][2]
        tt=[0]*n
        for i in barr: tt[i[0]] = i[2]
        comp_flg = 0
        arrived, ct, tat, wt, gantt = [], [0]*n, [0]*n, [0]*n, []
        curr = 0.0

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
        color=('pink', 'lightgreen', 'gold', 'violet')
        ax = plt.subplot(111)
        plotting=[]
        names = []
        for i in range(len(gantt)):
                if i==0:
                    plotting.append((t, gantt[i][1]-t, "P"+str(gantt[i][0])))
                else:
                    #print(gantt[i][0])
                    q=gantt[i-1][1] if gantt[i-1][1]>tt[gantt[i][0]] else tt[gantt[i][0]]
                    plotting.append((q, gantt[i][1]-q, "P"+str(gantt[i][0])))


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
        self.canvas.draw()

class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=None)
        vLayout = QtWidgets.QVBoxLayout(self)
        self.setWindowTitle("ALGORITHMS")
        self.setFixedSize(1100,200)
        self.setWindowIcon(QtGui.QIcon("download.png"))
        self.show()
        hLayout=QHBoxLayout()
        hlayout=QHBoxLayout()
        vLayout.addLayout(hlayout)
        vLayout.addLayout(hLayout)
        hlayout.setAlignment(QtCore.Qt.AlignHCenter)
        self.file=QPushButton("Upload files",self,objectName='upld')
        hlayout.addWidget(self.file)
        self.file.setMaximumSize(190,30)
        self.file.setStyleSheet("font-family:Georgia;font:bold")
        self.file.clicked.connect(self.upload)
        self.button=QPushButton("FIRST COME FIRST SERVE",self,objectName='btn')

        self.button1=QPushButton("MILF",self,objectName='btn1')

        self.button2=QPushButton("PRIORITY SCHEDULING",self,objectName='btn2')

        self.button3=QPushButton("ROUND ROBIN",self,objectName='btn3')

        self.button4=QPushButton("SHORTEST JOB FIRST",self,objectName='btn4')

        self.button5=QPushButton("SMALLEST REMAINING TIME FIRST",self,objectName='btn5')

        #hLayout.addWidget(self.button1)
        hLayout.addWidget(self.button3)
        hLayout.addWidget(self.button4)
        hLayout.addWidget(self.button2)
        hLayout.addWidget(self.button)
        hLayout.addWidget(self.button5)
        ########### styling
        self.button.setMaximumSize(185,30)
        self.button1.setMaximumSize(100,30)
        self.button2.setMaximumSize(170,30)
        self.button3.setMaximumSize(100,30)
        self.button4.setMaximumSize(160,30)
        self.button5.setMaximumSize(240,30)
        self.button.setStyleSheet("font-family:Georgia;font:bold")
        self.button.clicked.connect(self.fcfs)
        self.button1.clicked.connect(self.milf)
        self.button2.clicked.connect(self.psnp)
        self.button3.clicked.connect(self.rr)
        self.button4.clicked.connect(self.sjf)
        self.button5.clicked.connect(self.srtf)

        self.button.setStyleSheet(StyleSheet)
        self.button1.setStyleSheet(StyleSheet)
        self.button2.setStyleSheet(StyleSheet)
        self.button3.setStyleSheet(StyleSheet)
        self.button4.setStyleSheet(StyleSheet)
        self.button5.setStyleSheet(StyleSheet)
        self.file.setStyleSheet(StyleSheet)
        self.filename=None
    def upload(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)");
        if filename:
            self.filename=filename
            self.file.setText("UPLOADED")
            self.file.setToolTip(str(1)+"  File Uploaded")
        else:
            pass
    def fcfs(self):
        if self.filename:
            self.fcfs=GRAPH(self.filename)
            self.fcfs.show()
        else:
            QMessageBox.information(self, 'Alert',"No Files Selected", QMessageBox.Ok)
    def milf(self):
        if self.filename:
            self.milf=GRAPH1(self.filename)
            self.milf.show()
        else:
            QMessageBox.information(self, 'Alert',"No Files Selected", QMessageBox.Ok)
    def psnp(self):
        if self.filename:
            self.psnp=GRAPH2(self.filename)
            self.psnp.show()
        else:
            QMessageBox.information(self, 'Alert',"No Files Selected", QMessageBox.Ok)
    def rr(self):
        if self.filename:
            self.rr=GRAPH3(self.filename)
            self.rr.show()
        else:
            QMessageBox.information(self, 'Alert',"No Files Selected", QMessageBox.Ok)
    def sjf(self):
        if self.filename:
            self.sjf=GRAPH4(self.filename)
            self.sjf.show()
        else:
            QMessageBox.information(self, 'Alert',"No Files Selected", QMessageBox.Ok)
    def srtf(self):
        if self.filename:
            self.srtf=GRAPH5(self.filename)
            self.srtf.show()
        else:
            QMessageBox.information(self, 'Alert',"No Files Selected", QMessageBox.Ok)

App = QApplication(sys.argv)
window = MainWindow()
#window.setWindowFlags(QtCore.Qt.FramelessWindowHint);
#App.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
App.setStyle('Fusion')
dark_palette = QPalette()

dark_palette.setColor(QPalette.Window, QtGui.QColor(53, 53, 53))
dark_palette.setColor(QPalette.WindowText, QtCore.Qt.white)
dark_palette.setColor(QPalette.Base, QtGui.QColor(25, 25, 25))
dark_palette.setColor(QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
dark_palette.setColor(QPalette.ToolTipBase, QtCore.Qt.white)
dark_palette.setColor(QPalette.ToolTipText, QtCore.Qt.white)
dark_palette.setColor(QPalette.Text, QtCore.Qt.white)
dark_palette.setColor(QPalette.Button, QtGui.QColor(53, 53, 53))
dark_palette.setColor(QPalette.ButtonText, QtCore.Qt.white)
dark_palette.setColor(QPalette.BrightText, QtCore.Qt.red)
dark_palette.setColor(QPalette.Link, QtGui.QColor(42, 130, 218))
dark_palette.setColor(QPalette.Highlight, QtGui.QColor(42, 130, 218))
dark_palette.setColor(QPalette.HighlightedText, QtCore.Qt.black)
App.setPalette(dark_palette)
App.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
#window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
window.show()
#App.setStyleSheet(StyleSheet)
sys.exit(App.exec_())
