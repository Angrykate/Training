#include <conio.h>
#include <stdio.h>

int posDames[8] = {0}; // Index du tableau = y, valeur = x
int solution = 0;

int abs(int n) {
    return n < 0 ? -n : n;
}

void recursive(int nDames) {
    if (nDames == 8) {
        for (int i = 0; i < 8; ++i) {
            for (int j = 0; j < 8; ++j)
                if (j == posDames[i])
                    printf("1 ");
                else
                    printf("0 ");
            printf("\n");
        }
        printf("\n\n");
        ++solution;
    }

    for (int i = 0; i < 8; ++i) {
        for (int j = 0; j < nDames; ++j)
            if (posDames[j] == i || (abs(posDames[j] - i) == abs(j - nDames)))
                goto next; // Si une dame est déjà dans la colonne OU si elles se prennent en diagonale
        posDames[nDames] = i;
        recursive(nDames + 1); // On parcourt la ligne suivante dans l'échiquier
    next:
        continue;
    }
}

int main(int argc, char* argv[]) {
    recursive(0);
    printf("\nNombre de solutions : %d\n", solution);
    _getch();
    return 0;
}
