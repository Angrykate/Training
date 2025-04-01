#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct Node{
    int data;
    struct Node *next;
}node;

node *head = NULL;

void insererTete(int data){
    node *Nw = (node*)malloc(sizeof(node));
    Nw->data = data;
    Nw->next = head;
    head = Nw;
}

void insererFin(int data){
    if (head == NULL){
        insererTete(data);
        return;
    }
    node *Nw = (node*)malloc(sizeof(node));
    node *temp = head;
    while(temp->next!=NULL){
        temp = temp->next;
    }
    Nw->data = data;
    Nw->next = NULL;
    temp->next = Nw;

}

void insererPosition(int data, int position){
    node *Nw = (node*)malloc(sizeof(node));
    Nw->data = data;
    if(position == 1){
        insererTete(data);
        return;
    }
    node *temp = head;
    for(int i=1;temp!=NULL&& i<position-1;i++){
        temp = temp->next;
    }
    if(temp == NULL||temp->next==NULL){return;}
    Nw->next = temp->next;
    temp->next = Nw;

}

void supprimerDebut(){
    node *temp = head;
    head = temp->next;
    free(temp);
}

void supprimerFin(){
    if(head==NULL){return;}
    node *temp = head;
    while(temp->next->next!=NULL){
        temp = temp->next;
    }
    free(temp->next);
    temp->next = NULL;
}

void printList(){
    node *temp = head;
    while(temp!=NULL){
        printf("%d->",temp->data);
        temp=temp->next;
    }
    printf("NULL");
}

void longueur(){
    int l=0;
    while(head!=NULL){
        l++;
        head = head->next;
    }
    printf("\nla longueur = %d",l);
}

int main()
{
    insererTete(20);
    insererFin(10);
    insererTete(21);
    insererTete(41);
    insererPosition(4,3);
    supprimerFin();
    printf("liste:\n");
    printList();
    longueur();

}
