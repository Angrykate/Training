import java.util.List;
import java.util.ArrayList;

public class Bibliothèque {

	private String nom;
	private List<Livre> livres;
	private List<Membre> membres;
	
	public Bibliothèque(String nom) {
		this.nom = nom;
		this.livres = new ArrayList<Livre>();
		this.membres = new ArrayList<Membre>();
	}
	
	public void ajouterLivre(Livre livre) {
		if (this.livres.contains(livre)) {
			System.out.println("Le livre "+livre.getTitre()+" existe déjà dans notre bibliothèque!");
		}
		else {
			livres.add(livre);
		}
	}
	
	public void ajouterMembre(Membre membre) {
		if(this.membres.contains(membre)) {
			System.out.println("Le membre "+ membre.getNom()+" est déjà inscrit dans notre bibliothèque!");
		}
		else {
			membres.add(membre);
		}
	}
	
	public void rechercherLivre(String titre) {
		for(Livre livre: livres) {
			String presence = (livre.getTitre() == titre) ?"Ce livre est bien dans notre bibliothèque":"Ce livre n'est pas dans notre bibliothèque";
			System.out.println(presence);
		}
	}
}
