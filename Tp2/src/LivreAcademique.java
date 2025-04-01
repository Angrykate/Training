
public class LivreAcademique extends Livre {
	
	private String domaine;
	
	public LivreAcademique(String titre, String auteur, String isbn,String domaine, boolean disponible) {
		super(titre, auteur, isbn, disponible);
		this.domaine = domaine;
	}
	
	@Override
	public void afficherInfos() {
		String dispo = "Non";
		if(this.disponible) {
			dispo = "Oui";
		}
		System.out.println("\nTitre: "+this.titre+"\nAuteur: "+this.auteur+"\nIsbn: "+this.isbn+"\nDomaine: "+this.domaine+ "\nDisponible: "+dispo);
	}
}
