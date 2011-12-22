import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Collections;

public class usrbincrash {

	public static ArrayList<Item> list;
	public static int burden;

	public static void main(String[] args) {
		readInput(args[0]);
		int gcd = gcd(burden, gcd(1));
		if (gcd > 1)
			reduce(gcd);
		//System.out.println(gcd);
		//System.out.println(burden);
		// sort by weight
		//Collections.sort(list);
		//Item temp = new Item("ablimit", -1, -1); // for utility use;
		//Collections.binarySearch(list, temp);

		System.out.println(knapsack());
	}

	public static int knapsack() {
		int[] table = new int[burden + 1];
		int weight = list.get(0).getWeight();
		int cost = list.get(0).getCost();

		for (int j = 1; j <= burden; j++) { // Initialization 
			table[j] = (j < weight) ? cost : (table[j - weight]+ cost);
		}
		
		for (int i = 1; i < list.size(); i++) {
			weight = list.get(i).getWeight();
			cost = list.get(i).getCost();

			for (int j = 1; j <= burden; j++) {
				int cost_without_item_j = table[j];
				int cost_with_item_j = 0;
				cost_with_item_j = (j < weight) ? cost : (table[j - weight]+ cost);
				table[j] = Math.min(cost_with_item_j, cost_without_item_j);
			}
		}
		//print (table);

		return table[burden];
	}
	public static void  print(int [] table) {
		
		for (int i=0;i< table.length;i++)
			System.out.print(table[i]+",");
		System.out.println();
	}

	public static int knapsack2() {
		int[] weights = new int[burden + 1];

		return weights[burden];
	}

	public static int gcd(int a, int b) // valid for positive integers.
	{
		while (b > 0) {
			int c = a % b;
			a = b;
			b = c;
		}
		return a;
	}

	public static void reduce(int gcd) {
		int len = list.size();
		int w = 0;
		for (int i = 0; i < len; i++) {
			w = list.get(i).getWeight();
			list.get(i).setWeight(w / gcd);
		}
		burden = burden / gcd;
	}

	public static int gcd(int depth) {
		if (depth == list.size())
			return list.get(depth - 1).getWeight();
		else
			return gcd(list.get(depth - 1).getWeight(), gcd(depth + 1));
	}

	public static void readInput(String args) {
		BufferedReader in = null;
		try {
			in = new BufferedReader(new FileReader(args), 51200);
			String line;
			if ((line = in.readLine()) != null) {
				burden = Integer.parseInt(line);
			}
			list = new ArrayList<Item>(1000);
			while ((line = in.readLine()) != null) {
				String[] items = line.split("\\s+");
				int weight = Integer.parseInt(items[1]);
				int cost = Integer.parseInt(items[2]);
				list.add(new Item(items[0], weight, cost));
			}
			in.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

}
