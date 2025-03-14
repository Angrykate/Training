
public abstract class Pokemon {

	protected String nom;
	protected int hp;
	protected int atk;
	
	public Pokemon(String name,int hp,int atk) {
		this.nom = name;
		this.hp = hp;
		this.atk = atk;
	}

	public String getNom() {
		return nom;
	}

	public int getHp() {
		return hp;
	}

	public int getAtk() {
		return atk;
	}
	
	public boolean isDead() {
		return (hp==0);
	}
	
	public void afficher() {
		System.out.println("Nom: "+this.nom + " , Hp: "+this.hp+" , ATK: "+this.atk);
	}
	
	public abstract void attaquer(Pokemon p);
	
}
