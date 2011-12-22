import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.Collections;

public class gattaca {

	public static final ArrayList<Gene> geneList = new ArrayList<Gene>();

	public static void main(String[] args) throws IOException {
		readinput(args[0]);

		// Sort ArrayList by end position O(n*log(n))
		Collections.sort(geneList);
		//print();
		// System.out.println();
		// Collections.sort(geneList, new GeneComparator());
		// print();

		int size = geneList.size();
		// maximum overlap index
		int[] p = new int[size];
		p[0] = -1;

		// O(n^2) theoretically
		for (int i = size - 1; i > 0; i--) {
			int j; // linear search of maximum index, should use binary search
			for (j = i - 1; j >= 0 && geneList.get(i).overlaps(geneList.get(j)); j--)
				;
			p[i] = j;
		}

		//print(p);
		// max so far 
		int[] m = new int[size];
		m[0] = geneList.get(0).getWeight();

		for (int i = 1; i < size; i++) {
			m[i] = Math.max((p[i] >= 0 ? m[p[i]] : 0)
					+ geneList.get(i).getWeight(), m[i - 1]);
		}
		System.out.println(m[size-1]);
		//print(m);

	}

	public static void removeDuplicateGenes(ArrayList<Gene> list) {

		for (int i = 0; i < list.size(); i++) {
		}
	}

	public static void print(int[] array) {
		int size = array.length - 1;
		for (int i = 0; i < size; i++)
			System.out.print(array[i] + ",");
		System.out.println(array[size]);
	}

	public static void print() {
		for (int i = 0; i < geneList.size(); i++)
			System.out.println(geneList.get(i).getStart() + " "
					+ geneList.get(i).getEnd() + " "
					+ geneList.get(i).getWeight());
	}

	public static void readinput(String args) throws IOException {
		BufferedReader in = new BufferedReader(new FileReader(args));
		long skip = Long.parseLong(in.readLine());
		skip += Math.ceil(skip / 80);
		in.skip(skip);
		StreamTokenizer st = new StreamTokenizer(in);
		st.parseNumbers();

		while (st.ttype != StreamTokenizer.TT_NUMBER)
			st.nextToken();
		int count = (int) st.nval;

		Gene gene;
		for (int i = 0; i < count; i++) {
			st.nextToken();
			int start = (int) st.nval;
			st.nextToken();
			int end = (int) st.nval;
			st.nextToken();
			int weight = (int) st.nval;
			gene = new Gene(start, end, weight);
			geneList.add(gene);
		}
		in.close();
	}

}
