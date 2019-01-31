#include <stdio.h>
#include <malloc.h>
#include <conio.h>
#include <string.h>

#define MaxLength 10

typedef struct LIST
{
	char name[MaxLength];
	int length;
	struct LIST *next;
}LIST;


void print_list(LIST *p) /* Print all the node of the list. */
{
	LIST *q; 
	while(p){
		printf("%s",p->name);
		q=p->next;
		p=q;
	}
}

 LIST  *GetListNode(char x[MaxLength])
{	
   LIST  *s;	
   s=(LIST *)malloc(sizeof(LIST));
   if (s)	
   { 
     strcpy(s->name,x); 
	 s->next=NULL; 
	 }
	return(s);
	}  

LIST * insert_node(LIST *head, char x[MaxLength], int i)
{
   LIST *s,*p=head ;
   int j=1;  
   s=GetListNode(x);
   if(i==1)
   {
   	s->next=head;
   	head=s;
   	return (head);
   }
   while(p!=NULL&&j<i-1){
   	p=p->next;
   	j++;
   }
   if(j!=i-1||j>4){
   	printf("插入位置不合理\n");
   	return 0;
   }
 
   s->next=p->next;
   p->next=s;
   return (head);
}
     

LIST * delete_node(LIST *head, int i)
{
	LIST *p=head,*s;
	int j=1;
	if(i==1){
		head=head->next;
		return (head);
	}
	while(p->next!=NULL&&j<i-1){
		p=p->next;
		j++;
	}
	if(j!=i-1||j>=3){
		printf("\n删除位置不合理！");
		return 0; 
	}
	s=p->next;
	p->next=p->next->next;
	free(s);
	return (head); 
}

main()
{
	int i, choice;
	char x[MaxLength], element, listname;
	LIST *a, *b, *c, *p, *head; 
	
	a = (LIST *)malloc(sizeof(LIST));
	strcpy(a->name, "Zhou");

	b = (LIST *)malloc(sizeof(LIST));
	strcpy(b->name, "Xing");

	c = (LIST *)malloc(sizeof(LIST));
	strcpy(c->name, "Chi"); 
	
	head = a;
	a->next = b;
	b->next = c;
	c->next = NULL;
	p = head;

	printf("Welcome to use this programe!\nNow the exist list is:\n");
	print_list(p);

	printf("Please chose the function:\n1.Insert a node in the linklist.\n2.Delete a node in the link list.\n3.Print link list.\n4.Quit the programe.\n");
	
	scanf("%d", &choice);
	switch(choice)
	{
		case 4:{
					printf("Thanks to use!Good bye!");
					break;
			   }
		case 1:{
					printf("Input where the node you want to Insert:");
					scanf("%d", &i);

					printf("Input the node you want to Insert:");
					scanf(" %s", &x);
					
					head = insert_node(head, x, i);
					print_list(head);
					
					break;
				}
		case 2:{
					printf("Input where the node you want to Delete:");
					scanf("%d", &i);
					head=delete_node(head, i);
					print_list(head);
					break;
				}
		case 3:{
					print_list(head);
					
					break;

			   }
	}
} 
