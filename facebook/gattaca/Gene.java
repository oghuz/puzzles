public class Gene implements Comparable <Gene>{


	private int start;
	private int end;
	private int weight;
	
	public Gene(int start, int end, int weight) {
		super();
		this.start = start;
		this.end = end;
		this.weight = weight;
	}

	public int getStart() {
		return start;
	}

	public void setStart(int start) {
		this.start = start;
	}

	public int getEnd() {
		return end;
	}

	public void setEnd(int end) {
		this.end = end;
	}

	public int getWeight() {
		return weight;
	}

	public void setWeight(int weight) {
		this.weight = weight;
	}

	public static void main(String[] args) {

	}
	public boolean overlaps(Gene g) {
			return this.start < g.getEnd() && g.getStart() < this.end; 
	}
	

	// default comparison is by finishing time 
	public int compareTo(Gene g) {
		return this.end - g.getEnd();
	}

}
