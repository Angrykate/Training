
public class Mur extends Block {

	private boolean porteur;

	public Mur(final int longueur,final int largeur,final int hauteur,boolean porteur) throws IllegalBlockException {
		super(longueur,largeur,hauteur);
		this.porteur = porteur;
		this.couleur = Couleur.GRIS;
	}

	public boolean estTraversale() {
		return !porteur;
	}

}
