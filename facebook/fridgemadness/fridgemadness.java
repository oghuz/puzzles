import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Iterator;
import java.util.TreeMap;

public class fridgemadness {

	public static int engineerCount = 0;
	public static int drinkCount = 0;
	public static final String comma = ",";
	public static final String space = " ";

	public static HashMap<Integer, HashMap<Integer, Integer>> graph;
	//public static TreeMap<Integer, HashMap<Integer, Integer>> seniors;
	public static TreeMap<Integer, HashMap<Integer, Integer>> juniors;

	public static TreeMap<Integer, ArrayList<engineer>> seniors_list;
	//public static TreeMap<Integer, ArrayList<engineer>> juniors_list;
	
	public static HashMap<Integer, Integer> engaged;

	public static void main(String[] args) {
		readInput(args[0]);
		populatePreference();
		match_engineers();
		output(engineerCount / 2);
	}
	
	public static void  output(int size) {
		for (int i=0 ;i<size ;i++)
		{
			System.out.println(i + space +engaged.get(i) );
		}
	}

	public static void  match_engineers() {
		engaged = new HashMap<Integer, Integer>(engineerCount);
		HashMap<Integer, ArrayList<engineer>> engaged_list = new HashMap<Integer, ArrayList<engineer>>();

		int senior = -1;
		int junior = -1;
		int partner = -1;
		HashMap<Integer, Integer> pref = null;
		// while (engaged.size() != engineerCount){
		while (seniors_list.size() > 0) {
			senior = seniors_list.firstKey(); // get an unengaged senior
			// get the most preferred junior
			junior = seniors_list.get(senior).remove(0).getId();
			// if this junior is already engaged ?
			if (engaged.containsKey(junior)) {
				partner = engaged.get(junior); // who is the partner ?
				pref = juniors.get(junior); // get preference map

				// if this junior likes the current available senior ?
				if (pref.get(senior) < pref.get(partner)) {
					engaged.remove(junior);
					engaged.remove(partner); // dump the old guy
					
					engaged.put(senior, junior); // get engaged with new guy
					engaged.put(junior, senior);
					
					engaged_list.put(senior, seniors_list.remove(senior)); // remove from the list 
					
					seniors_list.put(partner, engaged_list.remove(partner));
				}
			} else {
				engaged.put(senior, junior);
				engaged.put(junior, senior);
				engaged_list.put(senior, seniors_list.remove(senior));
			}
		}
	}

	public static int prefer(ArrayList<engineer> pref, int engaged_senior,
			int new_newsenior) {
		int len = pref.size();
		int pref_idx_engaged = -1;
		int pref_idx_new = -1;
		for (int i = 0; i < len && (pref_idx_engaged < 0 || pref_idx_new < 0); i++) {
			if (pref.get(i).getId() == pref_idx_engaged)
				pref_idx_engaged = i;
			if (pref.get(i).getId() == pref_idx_new)
				pref_idx_new = i;
		}
		return -1;
	}

	public static void populatePreference() {
		int groupsize = engineerCount / 2;
		//seniors = new TreeMap<Integer, HashMap<Integer, Integer>>();
		juniors = new TreeMap<Integer, HashMap<Integer, Integer>>();

		//juniors_list = new TreeMap<Integer, ArrayList<engineer>>();
		seniors_list = new TreeMap<Integer, ArrayList<engineer>>();

		ArrayList<engineer> pref;
		HashMap<Integer, Integer> map;

		// calculate senior engineer preference to new engineers
		for (int id = 0; id < groupsize; id++) {
			pref = new ArrayList<engineer>(groupsize);
			for (int jd = groupsize; jd < engineerCount; jd++) {
				pref.add(new engineer(jd, calculatePreference(id, jd)));
			}
			Collections.sort(pref);
			/*
			map = new HashMap<Integer, Integer>(groupsize);
			for (int i = 0; i < groupsize; i++) {
				map.put(pref.get(i).getId(), i);
			}
			*/
			//seniors.put(id, map);
			seniors_list.put(id, pref);
			/*
			System.out.print(id + space);
			for (int i=0 ;i< pref.size();i++)
			System.out.print(pref.get(i).getId()+comma+pref.get(i).getLikability() + "\t");
			System.out.println();
			*/
		}

		// calculate new engineer preference to senior engineers
		for (int id = groupsize; id < engineerCount; id++) {
			pref = new ArrayList<engineer>(groupsize);
			for (int jd = 0; jd < groupsize; jd++) {
				pref.add(new engineer(jd, calculatePreference(id, jd)));
			}
			Collections.sort(pref);
			map = new HashMap<Integer, Integer>(groupsize);
			for (int i = 0; i < groupsize; i++) {
				map.put(pref.get(i).getId(), i);
			}
			juniors.put(id, map);
			//juniors_list.put(id, pref);
		}

		// collect the space;
		graph = null;
	}

	public static int calculatePreference(int engineer_i, int engineer_j) {
		if (engineer_i == engineer_j)
			return -1;
		HashMap<Integer, Integer> drinks_i = graph.get(engineer_i);
		HashMap<Integer, Integer> drinks_j = graph.get(engineer_j);

		Iterator<Integer> it = drinks_i.keySet().iterator();
		int likability = 0;
		int drink;
		int index;
		int val;
		int N = drinks_i.size();
		int drink_order_in_j;
		while (it.hasNext()) {
			drink = it.next();
			index = drinks_i.get(drink);
			val = N - index;

			if (drinks_j.containsKey(drink)) {
				drink_order_in_j = drinks_j.get(drink);
				if (drink_order_in_j < index)
					val = 0;
				else if (drink_order_in_j == index)
					val = val * val;
			}
			likability += val;
		}
		return likability;
	}

	public static void readInput(String args) {
		BufferedReader in = null;
		try {
			in = new BufferedReader(new FileReader(args), 51200);
			String line;
			if ((line = in.readLine()) != null) {
				String[] fields = line.split("\\s+");
				engineerCount = Integer.parseInt(fields[0]);
				drinkCount = Integer.parseInt(fields[1]);
			}

			graph = new HashMap<Integer, HashMap<Integer, Integer>>(
					engineerCount);
			for (int i = 0; i < engineerCount; i++) {
				graph.put(i, new HashMap<Integer, Integer>(drinkCount));
			}
			for (int i =0; i<drinkCount;i++ ) line=in.readLine();

			while ((line = in.readLine()) != null) {
				String[] fields = line.split("\\s+");
				int id = Integer.parseInt(fields[0]);
				String[] drinks = fields[1].split(comma);
				for (int i = 0; i < drinks.length; i++) {
					graph.get(id).put(Integer.parseInt(drinks[i]), i);
				}
			}
			in.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

}
