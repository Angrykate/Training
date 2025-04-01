#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include "nombres.c"

// Fonction principale
int main() {
    Node* head = NULL;
    setlocale(LC_ALL, "");
    printf("\n\t$-*-*-*-*-*-*-*-*-*-*-*-MENU-*-*-*-*-*-*-*-*-*-*-*-$\n");
    while(1)
    {
        int user_choice,j,k;
        char i;
        puts("\n1-) Ajouter un nombre à la liste\n");
        puts("2-) Supprimer un nombre de la liste\n");
        puts("3-) Afficher la liste\n");
        puts("4-) Calculer la longueur de la liste\n");
        puts("5-) Rechercher un nombre dans la liste\n");
        puts("6-) Trier la liste\n");
        puts("7-) Eliminer les doublons de la liste\n");
        puts("8-) Quitter\n\n");
        printf("Veuillez choisir une option: ");
        scanf("%d",&user_choice);
        if (user_choice == 8){break;};
        switch(user_choice)
        {
        case 1:
            getchar();
            puts("\na-) Ajouter un nombre en tête de liste\n");
            puts("b-) Ajouter un nombre en fin de liste\n");
            puts("c-) Ajouter un nombre à une position donné\n");
            printf("Veuillez choisir une option: ");
            scanf("%c",&i);
            switch(i)
            {
            case 'a':
                printf("Entrez le nombre: ");
                scanf("%d",&j);
                insert_At_Head(&head,j);
                printf("Le nombre a bien été ajouté en tête de liste\n\n");
                for(int i=0;i<120;i++){printf("*");};
                break;

            case 'b':
                printf("Entrez le nombre: ");
                scanf("%d",&j);
                insert_At_Tail(&head,j);
                printf("Le nombre a bien été ajouté en fin de liste\n\n");
                for(int i=0;i<120;i++){printf("*");};
                break;

            case 'c':
                printf("Entrez le nombre: ");
                scanf("%d",&j);
                printf("Entrez la position: ");
                scanf("%d",&k);
                insert_At_Position(&head,j,k);
                printf("Le nombre a bien été ajouté à la position souhaitée\n\n");
                for(int i=0;i<120;i++){printf("*");};
                break;

            default:
                printf("Option invalide\n");
                break;
            }
            break;

        case 2:
            getchar();
            puts("a-) Supprimer un nombre en tête de liste\n");
            puts("b-) Supprimer un nombre en fin de liste\n");
            puts("c-) Supprimer un nombre à une position donné\n");
            printf("Veuillez choisir une option: ");
            scanf("%c",&i);
            switch(i)
            {
            case 'a':
                delete_At_Head(&head);
                printf("Le nombre en tête de liste a bien été supprimé\n");
                for(int i=0;i<120;i++){printf("*");};
                break;

            case 'b':
                delete_At_Tail(&head);
                printf("Le nombre en fin de liste a bien été supprimé\n");
                for(int i=0;i<120;i++){printf("*");};
                break;

            case 'c':
                printf("Entrez la position: ");
                scanf("%d",&k);
                delete_At_Position(&head,k);
                printf("Le nombre a bien été supprimé à la position souhaitée\n");
                for(int i=0;i<120;i++){printf("*");};
                break;

            default:
                printf("Option invalide\n");
                for(int i=0;i<120;i++){printf("*");};
                break;
            }
            break;

        case 3:
            getchar();
            puts("Affichage de la liste: ");
            Affiche_List(head);
            printf("\n");
            for(int i=0;i<120;i++){printf("*");};
            break;

        case 4:
            getchar;
            printf("Longueur de la liste = %d\n",lenght_list(head));
            for(int i=0;i<120;i++){printf("*");};
            break;

        case 5:
            getchar();
            printf("Veuillez entrez le nombre à chercher: ");
            scanf("%d",&j);
            Search_Number(&head,j);
            for(int i=0;i<120;i++){printf("*");};
            break;

        case 6:
            getchar();
            if(head == NULL){
                printf("Action inutile sur une liste vide\n\n");
            }
            else{
                printf("La liste a bien été trié\n\n");
                Sorted_List(&head);}
            for(int i=0;i<120;i++){printf("*");};
            break;

        case 7:
            getchar();
            if(head == NULL){
                printf("Action inutile sur une liste vide\n\n");
            }
            else{
                printf("Tous les doublons ont été supprimé de la liste\n\n");
                Remove_Doublons(&head);
            }
            for(int i=0;i<120;i++){printf("*");};
            break;

        default:
              printf("Option invalide:\n\n");
              for(int i=0;i<120;i++){printf("*");};
              break;
        }
    }





















    /* Ajouter des éléments à la liste
    insert_At_Head(&head, 8);
    insert_At_Head(&head, 2);
    insert_At_Head(&head, 1);
    insert_At_Head(&head, 5);
    insert_At_Tail(&head, 7);
    Affiche_List(head);
    insert_At_Head(&head, 5);
    insert_At_Position(&head,0,4);
    Affiche_List(head);
    delete_At_Position(&head,9);
    Sorted_List(&head);
    Affiche_List(head);
    Remove_Doublons(&head);
    Affiche_List(head);
    printf("La longueur = %d\n",lenght_list(head));
    Search_Number(&head, 3);*/
}
