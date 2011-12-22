import java.util.LinkedList;
import java.util.List;

public class Node {
	public static enum COLOR {
		RED, BLACK, WHITE
	};

	private COLOR color;
	private String name;

	public String getName() {
		return name;
	}

	private List<Node> verticies = null;

	public Node(String s) {
		name = s;
		color = COLOR.WHITE;
		verticies = new LinkedList<Node>();
	}

	public Node(String s, COLOR c) {
		name = s;
		color = c;
		verticies = new LinkedList<Node>();
	}

	public List<Node> getVerticies() {
		return verticies;
	}
	public int outDegree() {
		return verticies.size();
	}

	public COLOR getColor() {
		return color;
	}

	public void setColor(COLOR color) {
		this.color = color;
	}

	public boolean iaccused(Node liar) {
		boolean accused = false;
		if (liar == null)
			return false;

		for (Node n : verticies) {
			if (n.getName().equals(liar.getName())) {
				accused = true;
				break;
			}
		}
		return accused;
	}

	public void accused(Node liar) {
		if (liar == null || iaccused(liar))
			return;
		verticies.add(liar);
	}
}
