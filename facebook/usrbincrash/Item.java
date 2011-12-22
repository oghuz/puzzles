public class Item implements Comparable <Item>{
	
	public String label;
	public int cost ;
	public int weight;
	public String getLabel() {
		return label;
	}
	public void setLabel(String label) {
		this.label = label;
	}
	public int getCost() {
		return cost;
	}
	public void setCost(int value) {
		this.cost = value;
	}
	public int getWeight() {
		return weight;
	}
	public void setWeight(int weight) {
		this.weight = weight;
	}
	public Item(String label, int weight ,int cost) {
		this.label = label;
		this.cost = cost;
		this.weight = weight;
	}
	
	public int compareTo(Item o) {
		
		return this.weight - o.getWeight();
	}
	


}
