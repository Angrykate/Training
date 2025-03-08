package exo;

public class Nain extends Personnage implements Guerrier, Voleur {

	public Nain(String n, int x, int y, int v) {
		super(n, x, y, 2);
	}

	@Override
	public String parler() {
		return "Groumpf";
	}
	
	@Override
		public void attaquer(Personnage p) {
			p.setPointsVie(p.getPointsVie()-force);
		}
	
	@Override
	public void voler(Personnage p) {
		int retrait = ((p.getSous()-dexterite)<0) ? 0: (p.getPointsVie()-dexterite);
		p.setSous(retrait);
	}
	
}
