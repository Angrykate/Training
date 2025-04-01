
public class Vol {
	
	private int id;
	private int numVol;
	private String heureDepart;
	private String destination;
	
	public Vol(int id, int numVol,String heureDepart, String destination) {
		this.id = id;
		this.numVol = numVol;
		this.heureDepart = heureDepart;
		this.destination = destination;
		
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public int getNumVol() {
		return numVol;
	}

	public void setNumVol(int numVol) {
		this.numVol = numVol;
	}

	public String getHeureDepart() {
		return heureDepart;
	}

	public void setHeureDepart(String heureDepart) {
		this.heureDepart = heureDepart;
	}

	public String getDestination() {
		return destination;
	}

	public void setDestination(String destination) {
		this.destination = destination;
	}
	

}