#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define null 0
#define n 100

typedef int keytype;

typedef struct node
{
	keytype key;//二叉排序树结点的关键字域
	struct node *lchild;
	struct node  *rchild;
}bstnode; //二叉排序树结点结构

typedef bstnode *bstree;//二叉排序树类型定义


void insertbst(bstree *tptr,keytype key)
{
    if((*tptr)==NULL)
	{
		(*tptr)=(bstnode*)malloc(sizeof(bstnode));
		(*tptr)->key=key;
	    (*tptr)->lchild=NULL;	
		(*tptr)->rchild=NULL;
	} //若树为空，插入的第一个结点作为根结点 
	else if(key<(*tptr)->key)
	    insertbst(&((*tptr)->lchild),key);//待插入元素小于根节点，则插入在左子树 
	else
	    insertbst(&((*tptr)->rchild),key);//待插入元素大于根节点，则插入在右子树 
	    
		//在二叉排序树tptr中，插入值为key的结点
}//end of insertbst

void createbst(bstree *t)
{
	//创建一棵二叉排序树t
	keytype key;
	int i,m;

	//随机输入100个以内的数据生成二叉排序树
	m = rand()%100;
	printf("random source data:");
	for(i=1; i<=m; i++)
	{
			key=rand()%100;;
			printf("%d ",key);
			insertbst(t,key);//将关键字key插入到二叉排序树t中
	}
	printf("\n");
	
}//end of createbst 

void inorder(bstree t)
{
	//对二叉排序树t进行中序遍历
	if (t)
	{
		inorder(t->lchild);//中序遍历左子树
		printf(" %d",t->key);//访问根结点
		inorder(t->rchild);//中序遍历右子树
	}//end of if 
}//end of inorder


void main()//主函数
{
	bstree t=null,q=null;
	
	srand( (unsigned)time( NULL ) );
	
	createbst(&t);//创建一棵二叉排序树t
	printf("\nbst data:");
	
	inorder(t);//输出二叉排序树t的中序遍历序列
	printf("\n");
}

