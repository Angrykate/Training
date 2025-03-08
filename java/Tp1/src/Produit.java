
public class Produit extends ItemInventaire implements Vendu{
	
	protected String nom;
	protected double prix;
	protected int quantite;
/* Protection des données : Les attributs privés empêchent 
l’accès direct et non contrôlé aux données*/

	Produit(){
		this.nom = "Inconnue";
		this.prix = 0;
		this.quantite = 0;
	}
	
	Produit(String nom, double prix){
		this.nom = nom;
		this.prix = prix;
		this.quantite = 0;
	}
	
	Produit (String nom, double prix, int quantite){
		this.nom = nom;
		this.prix = prix;
		this.quantite = quantite;
	}
	
	public void afficherInfos() {
		System.out.println("\nNom: "+this.nom+"\nPrix: "+this.prix+"\nQuantite: "+this.quantite);
	}
	
	public String getNom() {
		return this.nom;
	}
	
	public void setNom(String nvNom) {
		this.nom = nvNom;
	}
	
	public Double getPrix() {
		return this.prix;
	}
	
	public void setPrix(Double nvPrix) {
		if (nvPrix < 0) {
			System.out.println("Erreur! Veuillez entrez un nombre positif!");
		}
		else {
			this.prix = nvPrix;
		}
	}
	
	public int getQuantite() {
		return this.quantite;
	}
	
	public void setQuantite(int nvQuantite) {
		if (nvQuantite < 0) {
			System.out.println("Erreur! Veuillez entrez un nombre positif!");
		}
		else {
			this.quantite = nvQuantite;
		}
	}
	/*Contrôle : Les méthodes getter et setter permettent de contrôler
	  et de valider les modifications apportées aux attributs.*/

	@Override
	public void vendre(int quantiteVendu) {
		
		if(quantiteVendu > 0 && quantiteVendu <= quantite) {
			this.quantite-=quantiteVendu;
		}
		else {
			System.out.println("ERREUR: Quantité vendue invalide!");
		}
	}

	@Override
	public void afficherDetails() {
		afficherInfos();
	}
	

}
/*Modularité : L'encapsulation Facilite la maintenance et la modification du code
 sans affecter les autres parties du programme.*/


