
public class PokemonNormal extends Pokemon{

	public PokemonNormal(String name, int hp, int atk) {
		super(name, hp, atk);
	}

	@Override
	public void attaquer(Pokemon p) {
		p.hp -= this.atk;
		if (p.hp < 0) {
			p.hp = 0;
		}
	}
	
}
