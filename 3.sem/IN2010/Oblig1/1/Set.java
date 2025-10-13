import java.util.TreeSet;

public class Set {
	private TreeSet<Integer> settet;

	public Set() {
		settet = new TreeSet<Integer>();
	}

	public void insert(int x) {
		settet.add(x);
	}

	public boolean contains(int x) {
		return settet.contains(x);
	}

	public void remove(int x) {
		settet.remove(x);
	}

	public int size() {
		return settet.size();
	}
}
