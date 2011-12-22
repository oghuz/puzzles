import java.io.BufferedReader;
import java.io.FileReader;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedList;

public class liarliar {
	public static final int init = 10000;
	public static HashMap<String, Node> graph = new HashMap<String, Node>(init);
	public static LinkedList<String> queue = new LinkedList<String>();

	public static void main(String[] args) {
		getGraph(args[0]);// read input
		
		String root =getMostConnectedNode();
		graph.get(root).setColor(Node.COLOR.RED);
		queue.add(root); // put a node with arbitrary color

		int[] max_min = color(); // calculate

		System.out.println(Math.max(max_min[0], max_min[1]) + " "
				+ Math.min(max_min[0], max_min[1]));
	}

	public static void getGraph(String args) {
		try {
			BufferedReader br = new BufferedReader(new FileReader(args));
			String line = br.readLine();
			int liars = Integer.parseInt(line);
			Node node = null;
			while (liars > 0 && (line = br.readLine()) != null) {
				String[] fields = line.split("\\s+");
				String accuser = fields[0];
				int count = Integer.parseInt(fields[1]);

				if (graph.containsKey(accuser)) {
					node = graph.get(accuser);
				} else {
					node = new Node(accuser);
					graph.put(accuser, node);
				}

				String name = null;

				for (int i = 0; i < count && (name = br.readLine()) != null; i++) {
					if (!graph.containsKey(name))
						graph.put(name, new Node(name));

					node.accused(graph.get(name));

					if (!graph.get(name).iaccused(node))
						graph.get(name).accused(node);
				}
				liars--;
			}

			br.close();

		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	public static String getNext() {
		Iterator<String> it = graph.keySet().iterator();
		Node n = null;
		while (it.hasNext()) {
			n = graph.get(it.next());
			if (n.getColor() == Node.COLOR.WHITE) {
				break;
			}
		}
		return n.getName();
	}

	public static String getMostConnectedNode() {
		Iterator<String> it = graph.keySet().iterator();
		String vertex = null;
		String node = null;
		int max = Integer.MIN_VALUE;
		while (it.hasNext()) {
			vertex = it.next();
			if (graph.get(vertex).outDegree() > max) {
				max = graph.get(vertex).outDegree();
				node = vertex;
			}

		}
		return node;
	}

	public static boolean graph_is_colored() {
		boolean colored = true;
		Iterator<String> it = graph.keySet().iterator();
		Node n = null;
		while (it.hasNext()) {
			n = graph.get(it.next());
			if (n.getColor() == Node.COLOR.WHITE) {
				colored = false;
				break;
			}
		}
		return colored;
	}

	public static int[] color() {
		
		int[] groups = { -1, -1 };
		String accuser_name = null;
		Node accuser = null;
		while (!(queue.isEmpty() && graph_is_colored())) {
			if (!queue.isEmpty())
				accuser_name = queue.remove();
			else
				accuser_name = getNext();
			accuser = graph.get(accuser_name);

			if (accuser.getColor() == Node.COLOR.WHITE)
				accuser.setColor(Node.COLOR.RED);

			if (accuser.getColor() == Node.COLOR.RED) {
				for (Node liar : accuser.getVerticies()) {
					if (liar.getColor() != Node.COLOR.RED) {
						if (liar.getColor() == Node.COLOR.WHITE) {
							liar.setColor(Node.COLOR.BLACK);
							queue.add(liar.getName());
						}
					} else {
						groups[0] = graph.size();
						groups[1] = 0;
						return groups;
					}
				}
			}
			// black
			else {
				for (Node liar : accuser.getVerticies()) {
					if (liar.getColor() != Node.COLOR.BLACK) {
						liar.setColor(Node.COLOR.RED);
						queue.add(liar.getName());
					} else {
						groups[0] = graph.size();
						groups[1] = 0;
						return groups;
					}
				}
			}
		}
		Iterator<String> it = graph.keySet().iterator();
		int black = 0;
		int red = 0;
		while (it.hasNext()) {
			if (graph.get(it.next()).getColor() == Node.COLOR.BLACK)
				black++;
			else
				red++;
		}
		groups[0] = Math.max(black, red);
		groups[1] = Math.min(black, red);
		return groups;
	}

}
