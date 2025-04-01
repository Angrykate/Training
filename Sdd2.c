#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct Node{
    int data;
    struct Node *next;
}node;

node *head = NULL;

void insererTete(node **head,int data){
    node *Nw = (node*)malloc(sizeof(node));
    Nw->data = data;
    Nw->next = *head;
    *head = Nw;
}

void insererFin(node **head,int data){
    node *Nw = (node*)malloc(sizeof(node));
    Nw->data = data;
    node *temp = *head;
    while(temp->next!=NULL){
        temp = temp->next;
    }
    Nw->next = NULL;
    temp->next = Nw;
}

void insererPosition(node **head,int data,int position){
    node *Nw = (node*)malloc(sizeof(node));
    Nw->data = data;
    if(position == 1){
        insererTete(head,data);
        return;
    }
    node *temp = *head;
    for(int i=1;temp!=NULL&&i<position-1;i++){
        temp = temp->next;
    }
    if(temp==NULL||temp->next == NULL){return;}
    Nw->next=temp->next;
    temp->next = Nw;
}

void supprimerDebut(node **head){
    node *temp = *head;
    *head = temp->next;
    free(temp);
}

void supprimerFin(node **head){
    if(*head==NULL){return;}
    node *temp = *head;
    if((*head)->next==NULL){
        free(*head);
        *head = NULL;
    }
    while(temp->next->next!=NULL){
        temp = temp->next;
    }
    temp->next=NULL;
    free(temp->next);
}

void printList(node *head){
    node *temp = head;
    while(temp!=NULL){
        printf("%d->",temp->data);
        temp=temp->next;
    }
    printf("NULL");
}
void longueur(node *head){
    int l =0;
    while(head!=NULL){
        l++;
        head = head->next;
    }
    printf("\nLa longueur = %d",l);
}

int main()
{

    insererTete(&head,20);
    insererFin(&head,10);
    insererTete(&head,21);
    insererTete(&head,41);
    insererPosition(&head,4,2);
    supprimerFin(&head);
    printf("liste:\n");
    printList(head);
    longueur(head);

}
