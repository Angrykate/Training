import java.util.ArrayList;
import java.util.List;

public class Main {

	public static void main(String[] args) {
		
		// Liste de produits standards
		Produit p1 = new Produit("Telephone",15000,10);
		Produit p2 = new Produit("Stylo",100,50);
		Produit p3 = new Produit("Cahier",200,30);
		
		// Liste de produits alimentaires
		ProduitAlimentaire p4 = new ProduitAlimentaire("Mayonnaise",750,5,"14/01/2025");
		ProduitAlimentaire p5 = new ProduitAlimentaire("Lait",2000,20,"12/31/2024");
		
		// Ajout des produits à la liste
		List<Produit>produits = new ArrayList<>();
		produits.add(p1);
		produits.add(p2);
		produits.add(p3);
		produits.add(p4);
		produits.add(p5);
		
		// Affichage de la liste
		for(Produit produit:produits) {
			produit.afficherDetails();
		}
		
		// Simulation de vente
		p1.vendre(5);
		p2.vendre(12);
		p3.vendre(22);
		p4.vendre(1);
		p5.vendre(20);
		
		System.out.println("\nProduits apres mise à jour: ");
		for(Produit produit:produits) {
			produit.afficherDetails();
		}

		p1.vendre(8);
	}
	public static void afficherDetailsProduit(Produit p) {
		p.afficherInfos(); 
	}
}
