
public class Main {

	public static void main(String[] args) {
		//Instanciation des Pokémons
		
		//Type Normal
		PokemonNormal pn1 = new PokemonNormal("Leuphorie",390,70);
		PokemonNormal pn2 = new PokemonNormal("Ronflex",430,60);
		
		//Type Feu
		PokemonFeu pf1 = new PokemonFeu("Dracaufeu",700,120);
		PokemonFeu pf2 = new PokemonFeu("Salameche",390,80);
		
		//Type Eau
		PokemonEau pe1 = new PokemonEau("Carapuce",440,75);
		PokemonEau pe2 = new PokemonEau("Carabaffe",450,80);
		
		//Type Plante
		PokemonPlante pp1 = new PokemonPlante("Bulbizarre",400,55);
		PokemonPlante pp2 = new PokemonPlante("Florizarre",300,70);
		
		//Simulation des combats
		combatPokemon(pn1,pe1);
		System.out.println(new String(new char[50]).replace('\0', '-'));
		combatPokemon(pp1,pf2);
	}
	 
	//Fonction pour la simulation des combats
	public static void combatPokemon(Pokemon pok1,Pokemon pok2) {
		
		System.out.println(pok1.getNom()+" ("+pok1.getClass().getName()+") VS "+pok2.getNom()+" ("+pok2.getClass().getName()+")\n");
		
		while (!pok1.isDead() && !pok2.isDead()) {
			pok1.attaquer(pok2);
			System.out.println(pok1.getNom()+" attaque "+pok2.getNom());
			pok2.afficher();
			if(pok2.isDead()) {
				System.out.println(pok2.getNom()+ " est KO! "+pok1.getNom()+" gagne !");
				break;
			}
			
			pok2.attaquer(pok1);
			System.out.println(pok2.getNom()+" attaque "+pok1.getNom());
			pok1.afficher();
			if(pok1.isDead()) {
				System.out.println(pok1.getNom()+ " est KO! "+pok2.getNom()+" gagne !");
				break;
			}
		}
	}
}
