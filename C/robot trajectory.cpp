#include<stdio.h>  
#include<string.h>  
#include<stdlib.h>  
#include<algorithm>  

main()
{	int casenum=0;				 /* casenum代表一共要输入几组房间  */
	int endcase=0;
	int M,N,number;				 /* 定义M*N房间长宽，number墙数,M是行，N是列  */
	int i,j;
	int a[100][100];   				/*定义一个巨大的矩阵，代表房间内的格子*/
	int flag[100],wallnumber=0;     /*flag[n]是输入的第n个房间中无法到达出口的格子数*/
	int xx1,yy1,xx2,yy2;         	/*定义墙的起始坐标和终止坐标*/
	
	while(endcase==0)			
	{
		scanf("%d %d %d",&M,&N,&number);		 /* 输入M*N房间长宽，number墙数,M是行，N是列  */
		if(M==0&&N==0&&number==0)
			break;								/*如果输入0 0 0 则结束输入*/
		else
		{
			wallnumber=0;
			casenum++;
			for(i=0;i<=M-1;i++)
			{
				for(j=0;j<=N-1;j++) 		/*所有格子初值为5*/
				{
				a[i][j]=5;
				}	
			}

			for(i=1;i<=number;i++)
			{
				scanf("%ld %ld %ld %ld",&xx1,&yy1,&xx2,&yy2);			/*输入的墙都赋值为0*/
				for(j=xx1;j<=xx2;j++)
				{
				a[j][yy1]=0;
				wallnumber++;						/*计共有多少个格子的墙*/
				}
			}
	
			for(i=0;i<=M-2;i++)					/*将房间上方的墙赋值为0，最右一格赋值为1 */
			{
				a[i][N] =0;
			}
			a[i][N]=1;
	
			for(i=0;i<=N-2;i++)					/*将房间右边的墙赋值为0，最上一格赋值为1 */
			{
				a[M][i] =0;
			}
			a[M][i]=1;
	
			if(a[M-1][N-1]==0)					/*如果出口处是墙，那么无法到达出口的格子数为总格子数减去墙的数量*/
			{
				flag[casenum]=M*N-wallnumber;
			}
			else
			{
				for(i=M-1;i>=0;i--)
				{
			 		for(j=N-1;j>=0;j--)
					{
					if(a[i][j]==0)						/* 若果a[i][j]是墙，跳过 */
						continue;
					else											/*判断a[i][j]右边或上边的格子是否有1，有的话a[i][j]赋值1，没有的话赋值2*/
						{
							if(a[i+1][j]==1 || a[i][j+1]==1)
								a[i][j]=1;
							else
								a[i][j]=2;
						}
					}			
				}
			}

			for(i=M-1;i>=0;i--)
			{
		 		for(j=N-1;j>=0;j--)			/*遍历所有格子，算出共有多少赋值为2的格子，即无法到达出口的格子*/
	     		{
				if(a[i][j]==2)
				flag[casenum]++ ;
			
				}			
			}
    	}
	}
	for(i=1;i<=casenum;i++)					/*输出各个房间中无法到达出口的格子数*/
	printf("case %d : %d\n",i,flag[i]);
}

	
	


