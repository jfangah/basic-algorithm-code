#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>
#define maxsize 100

typedef struct stack{
	int data[maxsize];
	int top;
}stack;

void initstack(stack * s)
{
	s->top = -1;
}

void Push(stack *s, int x){
	if(s->top==maxsize-1){
		printf("Stack is FULL!!!");
		exit(0);
	}
	else	s->data[++s->top]=x;
}

int Pop(stack* s){
	return s->data[s->top--];
}

void Decimal_Binary(int x)
{
    
	stack * s=(stack*)malloc(sizeof(struct stack));        
    initstack(s);  
	int i;

    while(x) {     
      Push(s,x%2);    /* 余数入栈*/
      x/=2;             //被除数data整除以2，得到新的被除数
    }
 while(s->top!=-1){
  	 i=Pop(s); 
   	printf("%d",i);
	}

}

int main(){
	int x;
	scanf("%d",&x);
	Decimal_Binary(x);
}

