
public class Porte extends Block{

	private boolean verrouillee;
	
	public Porte(final int longueur,final int  largeur, final int hauteur, final boolean verrouillee) throws IllegalBlockException{
		super(longueur,largeur,hauteur);
		this.verrouillee = verrouillee;
		this.couleur = Couleur.BLEU;
	}

	public Couleur getN() {
		return couleur;
	}
	public boolean estVerrouillee() {
		return verrouillee;	
	}
	
	public void verrouiller() throws PorteVerrouilleException{
		if (!verrouillee) {
			this.verrouillee = true;
		}
		else {
			throw new PorteVerrouilleException();
		}
	}
}
