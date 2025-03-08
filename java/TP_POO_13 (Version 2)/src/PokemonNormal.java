
public class PokemonNormal extends Pokemon{

	public PokemonNormal(String name, int hp, int atk) {
		super(name, hp, atk);
	}

	@Override
	public void attaquer(PokemonNormal p) {
		p.hp -= this.atk;
		if (p.hp < 0) {
			p.hp = 0;
		}
	}

	@Override
	public void attaquer(PokemonFeu p) {
		p.hp -= this.atk;
		if (p.hp < 0) {
			p.hp = 0;
		}
	}

	@Override
	public void attaquer(PokemonEau p) {
		p.hp -= this.atk;
		if (p.hp < 0) {
			p.hp = 0;
		}
	}

	@Override
	public void attaquer(PokemonPlante p) {
		p.hp -= this.atk;
		if (p.hp < 0) {
			p.hp = 0;
		}
	}
	
}
