#include <stdio.h>
#include <stdlib.h>

typedef struct huffman_node 
 {
	int data;
	int lchild;
	int rchild;
	int parent;
 }bnode;  //定义二叉链表结点结构

void SelectIJ(int k, bnode node[], int *i, int *j)
 {
   	int x,y;       
    *i=0;	
	while(node[*i].parent!=0) 
	 { 
	*i=*i+1; 
	 } 
	*j=*i+1;
	while(node[*j].parent!=0&&*j<k)  
	{ 
	*j=*j+1;
	} 
	if (node[*i].data > node[*j].data)
	{  
      y=*i; 
	  *i=*j;
	  *j=y;  
    }  
    for (x=0; x<=k; x++) 
	{  
       if (node[x].parent==0) 
	   {  	
                if (node[x].data < node[*i].data && node[x].data < node[*j].data) 
				{  
                *j=*i;  
                *i=x;   
                } 
                if (node[x].data > node[*i].data && node[x].data< node[*j].data)
			    {  
                *j=x;  
                }  
       }  
    }  
 }
 
void HuffmanTree(int n, bnode node[],int w[])
 {
	int k,p;
	int i,j;
	for(p=0;p<n;p++)
	{
		node[p].data=w[p];
		node[p].lchild=node[p].rchild=0; 
	}
	for(p=0;p<2*n-1;p++)
	{
		node[p].parent=0;
	}
	for(k=n;k<2*n-1;k++)
	{
	SelectIJ(k,node,&i,&j);
	node[k].data=node[i].data+node[j].data;
	node[k].lchild=i;node[k].rchild=j;
	node[i].parent=node[j].parent=k;
    }
 }
int main(void)
{
	FILE *fp;
	int weight[26];
	int i,j,c,p,q;
	int a[30];
	int ch;
	int n;

	bnode *node;
	unsigned long code;

	for(i=0; i<26; i++)
	{
		weight[i] = 0;
	}

	if( (fp = fopen("StrayBirds.txt","r")) == NULL )
		return 0;

	do {
		ch = fgetc(fp);

		if (!( ((ch>=97)&&(ch<=122)) ||
			   ((ch>=65)&&(ch<=90 ))	 )
		   )
		{
			continue;
		}
		if( (ch>=97)&&(ch<=122) )
		{
			ch -= 32;
		}
        putchar(ch);
		weight[ch-65]++;
	} while(feof(fp)==0);

	printf("\n");

	n = 0;
	for(i=0; i<26; i++)
	{
		if(weight[i] > 0) 
		{
			n++;
			printf("%c  %d \n", i+65, weight[i]);
		}
	}

	node = (bnode *)malloc((2*26-1) * sizeof(bnode));

	//建立哈夫曼树
	HuffmanTree(26, node, weight);
	//哈夫曼编码
 

	for (i=0; i<26; i++)
	{
		q=0;
		printf("Now processing %c -----", i+65);
        c=i;
		p=node[c].parent;

		while(p){
			if(node[p].lchild==c)
			a[q]=0;
			else 
			a[q]=1;
		    c=p;	
		    p=node[c].parent;
			q++;
		}
		
		for(n=q-1;n>-1;n--) printf("%d",a[n]);
		printf("\n");
	}

	free(node);
	fclose(fp);
}
