#include<stdio.h>
#include<stdlib.h>
#include"nombres.h"

// Fonction pour créer un nouveau nœud
Node* creation_Node(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Fonction pour ajouter un nœud en tête de liste
void insert_At_Head(Node** head, int data) {
    Node* newNode = creation_Node(data);
    newNode->next = *head;
    *head = newNode;
}

// Fonction pour ajouter un nœud en fin de liste
void insert_At_Tail(Node** head, int data) {
    Node* newNode = creation_Node(data);
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    Node* temp = *head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = newNode;
}

//Fonction pour ajouter un noeud a une position donnée
void insert_At_Position(Node** head, int data, int position){
    Node* newNode = creation_Node(data);
    if (position == 1 || position == 0){
        insert_At_Head(head, data);
        return;
        }

    Node* temp = *head;
    for(int i=1; temp != NULL && i < position-1; i++){
        temp=temp->next;
    }

    if(temp == NULL || temp->next == NULL){
        insert_At_Tail(head,data);
        return;
    }

    newNode->next = temp->next;
    temp->next = newNode;
    return;
}

//Fonction pour calculer la longueur de la liste
int lenght_list(Node*  head){
    int len = 0;
    while(head != NULL){
        len ++;
        head = head->next;
    }
    return len;
}

//Fonction pour supprimer un élément en tete de liste
void delete_At_Head(Node** head){
    if(*head == NULL) return;
    Node* temp = *head;
    *head = temp->next;
    free(temp);

}

//Fonction pour supprimer un element en queue de liste
void delete_At_Tail(Node** head){
    if(*head == NULL) return;
    Node* temp = *head;
    if((*head)->next == NULL){
        free(*head);
        *head = NULL;
        return;
    }
    while(temp->next->next != NULL){
        temp = temp->next;
    }
    temp->next = NULL;
    free(temp->next);
}

//Fonction pour supprimer un element à une position donné
void delete_At_Position(Node** head,int position){
    if (*head == NULL){
        return;
    }
    if (position == 1 || position == 0) {
        delete_At_Head(head);
        return;
    }
    Node* temp = *head;
    for(int i =1; temp != NULL && i<position - 1;i++){
        temp = temp->next;
    }
    if(temp == NULL || temp->next == NULL){
        return;
    }
    free(temp->next);
    Node* next = temp->next->next;
    temp->next = next;
}

//Fonction pour trier la liste dans l'ordre croissant
void Sorted_List(Node** head){
    if(*head == NULL ||(*head)->next == NULL){
        return;
    }
    Node *i,*j;
    int temp;
    for(i = *head; i != NULL; i = i->next){
        for(j = i->next; j != NULL; j = j->next){
            if(i->data > j->data){
                temp = i->data;
                i->data = j->data;
                j->data = temp;
            }
        }
    }
}

//Fonction pour supprimer les doublons de la liste
void Remove_Doublons(Node** head){
    if(*head == NULL ||(*head)->next == NULL){
        return;
    }
    Node *i,*j;
    for(i = *head; i != NULL; i = i->next){
        for(j = i->next; j != NULL; j = j->next){
            if(i->data == j->data){
                i->next = j->next;
                free(j);
                j = i->next;

            }
        }
    }
}

// Fonction pour afficher la liste
void Affiche_List(Node* head) {
    while (head != NULL) {
        printf("%d -> ", head->data);
        head = head->next;
    }
    printf("NULL\n");
}

//Fonction pour chercher un nombre dans la liste
void Search_Number(Node** head,int data){
    Node* temp = *head;
    while(temp!=NULL){
        if(temp->data == data){
            printf("Nombre %d trouvé\n",data);
            return;
        }
        temp = temp->next;
    }
    printf("Nombre %d non trouvé\n",data);
}
