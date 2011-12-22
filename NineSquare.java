import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

public class NineSquare {
	public static HashSet<String> vocab = new HashSet<String>();

	public static boolean okay(String a, String b, String c) {
		String x = a.substring(0, 1) + b.substring(0, 1) + c.substring(0, 1);
		System.err.println(x);
		if (!vocab.contains(x))
			return false;
		x = a.substring(1, 2) + b.substring(1, 2) + c.substring(1, 2);
		System.err.println(x);
		if (!vocab.contains(x))
			return false;
		x = a.substring(2) + b.substring(2) + c.substring(2);
		System.err.println(x);
		if (!vocab.contains(x))
			return false;
		x = a.substring(0, 1) + b.substring(1, 2) + c.substring(2);
		System.err.println(x);
		if (!vocab.contains(x))
			return false;
		x = c.substring(0, 1) + b.substring(1, 2) + a.substring(2);
		System.err.println(x);
		if (!vocab.contains(x))
			return false;
		return true;
	}

	public static boolean check(String word) {
		return vocab.contains(word);
	}

	public static void main(String[] args) {
		//HashSet<String> vocab = new HashSet<String>();
		List<String> list = new ArrayList<String>();
		try {
			BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
			String line;
			String word;
			while ((line = in.readLine()) != null) {
				word = line.trim();
				vocab.add(word);
				list.add(word);
			}
			in.close();
		} catch (IOException e) {
		}

		int size = list.size();
		System.err.println(size);
		String a;
		String b;
		String c;
		for (int i = 0; i < size; i++) {
			a = list.get(i);
			for (int j = 0; j < size; j++) {
				b = list.get(j);
				for (int k = 0; k < size; k++) {
					c = list.get(k);
					if (okay(a, b, c)) {
						System.out.println(a);
						System.out.println(b);
						System.out.println(c);
						System.out.println();
					}

				}
			}
		}
	}

}
