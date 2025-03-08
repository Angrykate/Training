
public class Livre extends ItemBibliotheque implements Empruntable {

	protected String titre;
	protected String auteur;
	protected String isbn;
	protected boolean disponible;
	
	public Livre(String titre,String auteur,String isbn,boolean disponible) {
		this.titre = titre;
		this.auteur= auteur;
		this.isbn = isbn;
		this.disponible = disponible;
	}

	public String getTitre() {
		return titre;
	}

	public void setTitre(String titre) {
		this.titre = titre;
	}

	public String getAuteur() {
		return auteur;
	}

	public void setAuteur(String auteur) {
		this.auteur = auteur;
	}

	public String getIsbn() {
		return isbn;
	}

	public void setIsbn(String isbn) {
		int longueur = isbn.length();
		
		if(longueur != 13) {
			System.out.println("ERREUR: Le numero doit contenir 13 caractères!");
		}
		else {
			this.isbn = isbn;	
		}

	}

	public boolean isDisponible() {
		return disponible;
	}

	public void setDisponible(boolean disponible) {
		this.disponible = disponible;
	}
	
	public void afficherInfos() {
		String dispo = "Non";
		if(this.disponible) {
			dispo = "Oui";
		}
		System.out.println("\nTitre: "+this.titre+"\nAuteur: "+this.auteur+"\nIsbn: "+this.isbn+"\nDisponible: "+dispo);
	}
	
	@Override
	public void emprunter() {
		this.disponible = false;
	}

	@Override
	public void retourner() {
		this.disponible = true;
	}

	@Override
	public void afficherDetails() {
		afficherInfos();
	}
	
}
