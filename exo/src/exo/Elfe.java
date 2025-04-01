package exo;

public class Elfe extends Personnage {

	public Elfe(String n, int x, int y, int v) {
		super(n, x, y, 7);

	}

	@Override
	public String parler() {
		return "Eldarie";
	}

}
