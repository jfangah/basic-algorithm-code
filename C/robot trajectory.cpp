#include<stdio.h>  
#include<string.h>  
#include<stdlib.h>  
#include<algorithm>  

main()
{	int casenum=0;				 /* casenum����һ��Ҫ���뼸�鷿��  */
	int endcase=0;
	int M,N,number;				 /* ����M*N���䳤��numberǽ��,M���У�N����  */
	int i,j;
	int a[100][100];   				/*����һ���޴�ľ��󣬴������ڵĸ���*/
	int flag[100],wallnumber=0;     /*flag[n]������ĵ�n���������޷�������ڵĸ�����*/
	int xx1,yy1,xx2,yy2;         	/*����ǽ����ʼ�������ֹ����*/
	
	while(endcase==0)			
	{
		scanf("%d %d %d",&M,&N,&number);		 /* ����M*N���䳤��numberǽ��,M���У�N����  */
		if(M==0&&N==0&&number==0)
			break;								/*�������0 0 0 ���������*/
		else
		{
			wallnumber=0;
			casenum++;
			for(i=0;i<=M-1;i++)
			{
				for(j=0;j<=N-1;j++) 		/*���и��ӳ�ֵΪ5*/
				{
				a[i][j]=5;
				}	
			}

			for(i=1;i<=number;i++)
			{
				scanf("%ld %ld %ld %ld",&xx1,&yy1,&xx2,&yy2);			/*�����ǽ����ֵΪ0*/
				for(j=xx1;j<=xx2;j++)
				{
				a[j][yy1]=0;
				wallnumber++;						/*�ƹ��ж��ٸ����ӵ�ǽ*/
				}
			}
	
			for(i=0;i<=M-2;i++)					/*�������Ϸ���ǽ��ֵΪ0������һ��ֵΪ1 */
			{
				a[i][N] =0;
			}
			a[i][N]=1;
	
			for(i=0;i<=N-2;i++)					/*�������ұߵ�ǽ��ֵΪ0������һ��ֵΪ1 */
			{
				a[M][i] =0;
			}
			a[M][i]=1;
	
			if(a[M-1][N-1]==0)					/*������ڴ���ǽ����ô�޷�������ڵĸ�����Ϊ�ܸ�������ȥǽ������*/
			{
				flag[casenum]=M*N-wallnumber;
			}
			else
			{
				for(i=M-1;i>=0;i--)
				{
			 		for(j=N-1;j>=0;j--)
					{
					if(a[i][j]==0)						/* ����a[i][j]��ǽ������ */
						continue;
					else											/*�ж�a[i][j]�ұ߻��ϱߵĸ����Ƿ���1���еĻ�a[i][j]��ֵ1��û�еĻ���ֵ2*/
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
		 		for(j=N-1;j>=0;j--)			/*�������и��ӣ�������ж��ٸ�ֵΪ2�ĸ��ӣ����޷�������ڵĸ���*/
	     		{
				if(a[i][j]==2)
				flag[casenum]++ ;
			
				}			
			}
    	}
	}
	for(i=1;i<=casenum;i++)					/*��������������޷�������ڵĸ�����*/
	printf("case %d : %d\n",i,flag[i]);
}

	
	


