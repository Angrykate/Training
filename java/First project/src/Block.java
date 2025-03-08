
public abstract class Block implements IBlock {
	protected int longueur;
	protected int largeur;
	protected int hauteur;
	protected Couleur couleur;
	
	public Block(final int longueur, final int largeur, final int hauteur) throws IllegalBlockException {
		if (longueur < MIN_LONGUEUR || largeur < MIN_LARGEUR || hauteur < MIN_HAUTEUR) {
			throw new IllegalBlockException();
		}
		this.longueur = longueur;
		this.largeur = largeur;
		this.hauteur = hauteur;
	}
	
	public int getLongueur() {
		return longueur;
	}

	public int getLargeur() {
		return largeur;
	}

	public int getHauteur() {
		return hauteur;
	}
	
	public void setCouleur(Couleur couleur) {
		this.couleur = couleur;
	}
	
	public void afficher() {
		System.out.println("Longueur = "+this.longueur+" ;Largeur = "+this.largeur+" ;Hauteur ="+this.hauteur);
	}
}
