
public class ProduitAlimentaire extends Produit {
	private String dateExpiration ;
	
	public ProduitAlimentaire(String nom, double prix, int quantite,String exp){
		super(nom,prix,quantite);
		this.dateExpiration = exp;
		
	}
	
	public String getDateExpiration() {
		return this.dateExpiration;
	}
	
	public void setDateExpiration(String nvExp) {
		this.dateExpiration = nvExp;
	}
	
	@Override
	public void afficherInfos() {
		super.afficherInfos();
		System.out.println("Date d'expiration: "+this.dateExpiration);
	}
}
