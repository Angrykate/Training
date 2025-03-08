
public class PokemonFeu extends Pokemon {

	public PokemonFeu(String name, int hp, int atk) {
		super(name, hp, atk);
	}

	@Override
	public void attaquer(Pokemon p) {
		String className = p.getClass().getName();
		
		if ( className == "PokemonPlante") {
			p.hp -= 2*this.atk;
		}else if (className == "PokemonEau" || className == "PokemonFeu" ) {
			p.hp -= 0.5*this.atk;
		}else {
			p.hp -= this.atk;
		}
		
		if (p.hp < 0) {
			p.hp = 0;
		}
	}
}
