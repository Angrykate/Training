package exo;

public abstract class Personnage{ 
	private String nom; 
	private int pointsVie, x, y, v, sous; 
	
	public Personnage(String n, int x, int y, int v){ 
		this.nom = n; 
		this.x = x; this.y = y; 
		this.pointsVie = 100; 
		this.v = v; 
		this.sous = 0; 
	} 
	
	public int getSous(){return this.sous;} 
	public void setSous(int s){this.sous = s;} 
	public int getPointsVie(){return this.pointsVie;} 
	public void setPointsVie(int pv){this.pointsVie = pv;} 
	
/** Le personnage se deplace dans la direction (dx,dy) durant un temps t. 
*/ 	public void seDeplacer(int dx, int dy, int t){ 
		this.x = (int) (this.x + dx*this.v*t/Math.sqrt(dx*dx+dy*dy)); 
		this.y = (int) (this.y + dy*this.v*t/Math.sqrt(dx*dx+dy*dy)); 
} 
public abstract String parler(); 
}
