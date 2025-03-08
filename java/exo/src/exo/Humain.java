package exo;

public class Humain extends Personnage{

	public Humain(String n, int x, int y, int v) {
		super(n, x, y, 5);

	}

	@Override
	public String parler() {
		return "Bonjour";
	}

}
