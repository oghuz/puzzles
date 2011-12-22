import java.io.BufferedReader;
import java.io.FileReader;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;

public class breathalyzer {

	public static final String VocabularyPath = "/var/tmp/twl06.txt";
	public static final HashSet<String> vocab = new HashSet<String>(200000);
	public static final HashMap<String, Integer> postings = new HashMap<String, Integer>(1000);
	public static int Max_Dic_Word_Len=0;
	public static int Max_Post_Word_Len = 0;
	public static int [][] distance;

	public static void main(String[] args) {
		int sum_distance = 0;

		Max_Dic_Word_Len = getVocabulary();
		String post = getPost(args[0]);
		String words[] = post.split("\\s+");
		for (String term : words) {
			if (term.length() > Max_Post_Word_Len)
				Max_Post_Word_Len = term.length();
		}
		//initlize 
		
		distance = new int [Max_Post_Word_Len+1][Max_Dic_Word_Len+1] ;
		
		for (String term : words)
			sum_distance += getMinimumDistance(term.toUpperCase());
		System.out.println(sum_distance);
	}

	public static int getMinimumDistance(String term) {
		int distance = Integer.MAX_VALUE;
		if (vocab.contains(term))
			distance = 0;
		else if (postings.containsKey(term)) {
			distance = postings.get(term);
		} else {
			Iterator<String> itor = vocab.iterator();
			int temp = Integer.MAX_VALUE;

			while (itor.hasNext()) {
				String word = itor.next();
				if (Math.abs(word.length() - term.length()) >= temp)
					continue;
				temp = getEditDistance(term, word);
				if (temp < distance)
					distance = temp;

				if (distance == 1)
					break;
			}
			postings.put(term, distance);
		}

		return distance;
	}

	public static int getEditDistance(String src, String tar) {
		int src_len = src.length();
		int tar_len = tar.length();

		// subproblem table we need fill up
		//int[][] distance = new int[src_len + 1][tar_len + 1];

		int cost = 0;

		// prefill the table in horizental dimension
		for (int i = 0; i <= src_len; i++) {
			distance[i][0] = i;
		}
		// prefill the table entry in vertical dimension
		for (int i = 0; i <= tar_len; i++) {
			distance[0][i] = i;
		}

		for (int i = 1; i <= src_len; i++) {
			for (int j = 1; j <= tar_len; j++) {
				if (src.charAt(i - 1) == tar.charAt(j - 1))
					cost = 0;
				else
					cost = 1;

				// Minimum of the three, corresponsds to 3 subprobelm.
				distance[i][j] = Math.min(Math.min(distance[i - 1][j] + 1, // delete
						distance[i][j - 1] + 1), // insert
						distance[i - 1][j - 1] + cost); // substitute if cost==1
				// or copy if cost ==0
			}
		}
		return distance[src_len][tar_len];
	}

	public static String getPost(String args) {
		String post = null;
		try {
			BufferedReader br = new BufferedReader(new FileReader(args), 51200);
			String line;

			if ((line = br.readLine()) != null) {
				post = line.trim();
			}
			br.close();

		} catch (Exception e) {
			e.printStackTrace();
		}
		return post;
	}

	public static int getVocabulary() {
		int max = 0;
		try {
			BufferedReader br = new BufferedReader(new FileReader(
					VocabularyPath), 51200);
			String line;
			while ((line = br.readLine()) != null) {
				// String word = line.trim().toLowerCase();
				if (line.length() > max)
					max = line.length();
				vocab.add(line);
				// vocs.add(word);
			}
			br.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
		return max;
	}

}
