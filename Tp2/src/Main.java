
public class Main {
	
	public static void main(String[] args) {
		
		// Creation de livres standards
		Livre l1 = new Livre("Harry_potter","J.K rowling","8175714687132",true);
		Livre l2 = new Livre("Game_of_Thrones","George R.R. martin","7821231167482",true);
		Livre l3 = new Livre("Hunger_Games","Susanne Collins","4568034752108",false);
		
		// Creation de livres academiques
		LivreAcademique l4 = new LivreAcademique("Femto","Jimmy Roussel","124786540561284","Physique",true);
		LivreAcademique l5 = new LivreAcademique("CIAM","Salio Touré","47856651025478","Mathématique",false);
		
		// Creation de membres
		Membre m1 = new Membre("Joe","100");
		Membre m2 = new Membre("Ben","99");
		
		// Creation d'une bibliotheque
		Bibliothèque b = new Bibliothèque("Sainte_Genevieve");
		
		// Ajout de livres à la bibliothèque
		b.ajouterLivre(l1);
		b.ajouterLivre(l2);
		b.ajouterLivre(l3);
		b.ajouterLivre(l4);
		
		// Ajout de membre à la bibliothèque
		b.ajouterMembre(m1);
		b.ajouterMembre(m2);
		
		// Emprunts de livre
		m1.emprunterLivre(l1);
		m1.emprunterLivre(l2);
		m2.emprunterLivre(l5); 
		m2.emprunterLivre(l4);
		
		// Infos des membres
		m1.afficherInfos();
		m2.afficherInfos();
		
		// Retours de livre
		m1.rendreLivre(l1);
		m1.rendreLivre(l2);
		m2.rendreLivre(l5);
		m2.rendreLivre(l4);
		
		// mise à jour des infos
		m1.afficherInfos();
		m2.afficherInfos();

	}
	
	public static void afficherDetailsLivre(Livre livre) {
		livre.afficherInfos();
	}
}
