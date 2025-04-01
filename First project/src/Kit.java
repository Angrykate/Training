import java.util.ArrayList;
import java.util.List;

public class Kit {

	private List<IBlock> blocks = new ArrayList<IBlock>();
	private List<String> motsCles = new ArrayList<String>();

	public Kit() throws IllegalBlockException {
		blocks.add(new Mur(3,2,2,true));
		blocks.add(new Mur(3,2,2,true));
		blocks.add(new Mur(2,1,2,false));
		blocks.add(new Mur(2,1,2,false));
		blocks.add(new Porte(1,2,2,true));

		motsCles.add("Cabane");
		motsCles.add("Muraille");
	}

	public void afficherKit() {
		System.out.println("Nombre de bloc dans le kit : "+blocks.size());
		System.out.print("Liste des mots clés du kit : ");
		for(String i:motsCles) {
			System.out.print(i+" ");
		}
	}
}
