
public class Passager {
	
	private String nom;
	private String prenom;
	private int id;
	private int numPasseport;
	
	public Passager(String nom, String prenom , int id, int numPasseport) {
		this.nom = nom;
		this.prenom = prenom;
		this.id = id;
		this.numPasseport = numPasseport;
	}

	public String getNom() {
		return nom;
	}

	public void setNom(String nom) {
		this.nom = nom;
	}

	public String getPrenom() {
		return prenom;
	}

	public void setPrenom(String prenom) { 
		this.prenom = prenom;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public int getNumPasseport() {
		return numPasseport;
	}

	public void setNumPasseport(int numPasseport) {
		this.numPasseport = numPasseport;
	}
}
