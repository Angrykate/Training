#ifndef NOMBRES_H_INCLUDED
#define NOMBRES_H_INCLUDED
// Définition de la structure de la liste chaînée
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// Fonction pour créer un nouveau nœud
Node* creation_Node(int data);
// Fonction pour ajouter un nœud en tête de liste
void insert_At_Head(Node** head, int data);
// Fonction pour ajouter un nœud en fin de liste
void insert_At_Tail(Node** head, int data);

//Fonction pour ajouter un noeud a une position donnée
void insert_At_Position(Node** head, int data, int position);
//Fonction pour calculer la longueur de la liste
int lenght_list(Node*  head);

//Fonction pour supprimer un élément en tete de liste
void delete_At_Head(Node** head);
//Fonction pour supprimer un element en queue de liste
void delete_At_Tail(Node** head);
//Fonction pour supprimer un element à une position donné
void delete_At_Position(Node** head,int position);

//Fonction pour trier la liste dans l'ordre croissant
void Sorted_List(Node** head);

//Fonction pour supprimer les doublons de la liste
void Remove_Doublons(Node** head);

// Fonction pour afficher la liste
void Affiche_List(Node* head);
//Fonction pour chercher un nombre dans la liste
void Search_Number(Node** head,int data);




#endif // NOMBRES_H_INCLUDED
