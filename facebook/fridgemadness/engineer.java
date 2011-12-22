public class engineer implements Comparable<engineer>{
	
	private int id;
	private int likability;
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public int getLikability() {
		return likability;
	}
	public void setLikability(int likability) {
		this.likability = likability;
	}
	public engineer(int id, int likability) {
		this.id = id;
		this.likability = likability;
	}

	public int compareTo(engineer b) {
		
		if (this.likability >b.getLikability())
		{
			return -1;
		}
		else if (this.likability < b.getLikability())
		{
			return 1;
		}
		else {
			return b.getId()-this.id;
		}
	}
	

}
