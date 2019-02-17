# Problem Statement Document

***

## Satement
* Design an interactive platform (Web, app) for CPU scheduling algorithms (minimum requirement: outcome to be displayed in a Gantt chart).

## Inference
* We need to create an interactive web portal or app where the user can specify the number , burst time, arrival time and priority/time quantum of processes .
* The user can also choose the type of algorithm he/she needs for scheduling of processes .
* In return our program will generate a ‘GANTT CHART’ based on the respective scheduling algorithm and inputs the user has provided .


### Constraints
* The project has only five algorithms.

### Assumptions
* The user has some prior knowledge about scheduling algorithms.

***

## Applications
* The project can be used in OS lectures for visual dipiction of gantt charts.
* The project can be used to compare scheduling algorithms.


## Possible soltuions
* The algorithms were standard so they cannot be changed. There were discussions on which platform it would be feasible to show algorithms. The possible platforms were:
    * Android
    * Web
    * GUI

## Solution chosen

* We created the logic and implemented the code of 5 priority scheduling algorithms , namely

	- FIRST COME FIRST SERVE (FCFS)
	- SHORTEST JOB FIRST (SJF)
	- SHORTEST REMAINING TIME FIRST (SRTF)
	- ROUND ROBIN (RR)
	- PRIORITY SCHEDULING
    
* On taking the user inputs of number of processes , arrival time and burst time of processes and priority in the case of PRIORITY SCHEDULING and time quantum in the case of ROUND ROBIN , the program will return the GANTT CHART based on the respective inputs.



## Motivation behind solution
* The team was comfortable with Python.
* Prior knowledge of creating GUI with PyQt5.

***