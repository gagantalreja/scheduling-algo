#include <stdio.h>

void swap(int *xp, int *yp) 
{ 
	int temp = *xp; 
	*xp = *yp; 
	*yp = temp; 
} 

void sjf_sorted(int arr[], int b[], int n) 
{ 
	int i, j, min_idx; 

	for (i = 0; i < n-1; i++) 
	{ 
		min_idx = i; 
		for (j = i+1; j < n; j++) 
		if (b[j] < b[min_idx]) 
			min_idx = j; 
		swap(&arr[min_idx], &arr[i]); 
		swap(&b[min_idx], &b[i]);
	} 
} 

void pri_sorted(int arr[], int b[], int pri[], int n) 
{ 
	int i, j, min_idx; 

	for (i = 0; i < n-1; i++) 
	{ 
		min_idx = i; 
		for (j = i+1; j < n; j++) 
		if (pri[j] < pri[min_idx]) 
			min_idx = j; 
		swap(&arr[min_idx], &arr[i]); 
		swap(&b[min_idx], &b[i]);
		swap(&pri[min_idx], &pri[i]);	
	} 
}

void fcfs(int b[], int c[], int t[], int w[], int n)
{
	int curr=0;
	for(int i=0;i<n;i++)
	{
		curr+=b[i];
		c[i]=curr;
		t[i]=curr;
		w[i]=curr-b[i];
	}
}

void sjf(int b[], int c[], int t[], int w[], int n)
{
	fcfs(b, c, t, w, n);
}

void priority(int b[], int c[], int t[], int w[], int n)
{
	fcfs(b, c, t, w, n);
}

void rr(int b[], int c[], int t[], int w[], int n)
{
	int tq;
	printf("Quantum time: ");
	scanf("%d",&tq);
	int i=0;
	int check=0;
	int curr=0;
	while(check!=n)
	{
		if(b[i%n]>0)
		{
			printf("%d %d %d %d\n", i, i%n, b[i%n], curr);
			if(b[i%n]<=tq)
			{
				curr=curr+b[i%n];
				c[i%n]=curr;
				t[i%n]=curr;
				w[i%n]=curr-b[i%n];
				check+=1;
			}
			else
			{
				curr=curr+tq;
			}
			b[i%n]-=tq;
		}
			
		i+=1;
	}
}
int main()
{
	
	printf("Enter number of processes\n");
	int n;
	scanf("%d", &n);
	printf("Enter a space separated line having %d integers having burst times of respective processes: ", n);
	int burst[n], cmp[n], tat[n], wt[n], proc[n], pri[n];
	
	for(int i=0;i<n;i++)
	{
		scanf("%d", &burst[i]);
		proc[i]=i+1;
	}

	int choice;
	printf("1. FCFS\n2. SJF\n3. Priority\n4. Round Robin\nEnter your choice: ");
	scanf("%d", &choice);

	switch(choice)
	{
		case 1: fcfs(burst, cmp, tat, wt, n);break;
		case 2: sjf_sorted(proc, burst, n); sjf(burst, cmp, tat, wt, n);break;
		case 3: printf("Enter priority for all process. Lower Number is higher priority: ");
			for(int i=0;i<n;i++)
				scanf("%d", &pri[i]);
			pri_sorted(proc, burst, pri, n);
			priority(burst, cmp, tat, wt, n);
			break;
		case 4: rr(burst, cmp, tat, wt, n);break;
		default: printf("Invalid Choice\n");
	}
	if (choice<=4)
	{
		float avgt=0.0f;
		float avgw=0.0f;
		for(int i=0;i<n;i++)
		{	
			avgt+=tat[i];
			avgw+=wt[i];
		}
		avgt=avgt/n;
		avgw=avgw/n;
		printf("Avg TAT = %f\nAvg WT = %f\n", avgt, avgw);
	}
  return 0;
}
