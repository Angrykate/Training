import java.util.List;
import java.util.ArrayList;

public class Membre {
	private String nom;
	private String identifiant;
	private List<Livre> emprunts;
	
	public Membre(String nom, String identifiant) {
		this.nom = nom;
		this.identifiant = identifiant;
		this.emprunts = new ArrayList<>();
	}
	
	public void afficherInfos() {
		System.out.println("\nNom: "+this.nom+"\tIdentifiant: "+this.identifiant);
		if (this.emprunts.isEmpty()) {
			System.out.println("Aucun livre empruntés !");
		}
		else {
			System.out.println("Livres empruntés: ");
			for (Livre livre: emprunts) {
				System.out.println("-"+livre.getTitre());
			}
		}
	}
	
	public String getNom() {
		return nom;
	}

	public void setNom(String nom) {
		this.nom = nom;
	}

	public String getIdentifiant() {
		return identifiant;
	}

	public void setIdentifiant(String identifiant) {
		this.identifiant = identifiant;
	}

	public void emprunterLivre(Livre livre) {
		if(livre.isDisponible()) {
			livre.emprunter();
			emprunts.add(livre);
		}
		else {
			System.out.println("Désole, ce livre n'est pas disponible à l'emprunt !");
		}
	}
	
	public void rendreLivre(Livre livre) {
		if (emprunts.contains(livre)) {
			livre.retourner();
			int ind = emprunts.indexOf(livre);
			emprunts.remove(ind);
		}
		else {
			System.out.println("Désole ce livre n'est pas emprunté!");
		}
	}
}
