public class Main {
	public static void main(String[] args) {
		try {
			Porte porte = new Porte(1, 1, 1, true);
			porte.verrouiller();
			System.out.println(porte.getN());
		} catch (IllegalBlockException e) {
			System.out.println("Impossible de construire le bloc.");
		} catch (PorteVerrouilleException exception) {
			System.out.println("La porte est déjà vérrouillée.");
		}
		

		
	}
}