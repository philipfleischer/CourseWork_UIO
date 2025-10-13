public class Teque {
	private Node start;
	private Node midt;
	private Node slutt;
	private int stoerrelse;

	public Teque() {
		start = null;
		midt = null;
		slutt = null;
		stoerrelse = 0;
	}

	public void push_back(int antallBak) {
		Node nyNode = new Node(antallBak);

		if(stoerrelse == 0){
			start = midt = slutt = nyNode;
		}

		nyNode.forrige = slutt;
		if(slutt != null){
			slutt.neste = nyNode;
		}
		slutt = nyNode;
		stoerrelse++;
	}

	public void push_front(int antallForran) {
		Node nyNode = new Node(antallForran);

		if(stoerrelse == 0){
			start = midt = slutt = nyNode;
		}

		nyNode.neste = start;
		if(start != null){
			start.forrige = nyNode;
		}
		start = nyNode;
		stoerrelse++;
	}

	public void push_middle(int antMidt) {
		Node nyNode = new Node(antMidt);

		if(stoerrelse == 0) {
			start = midt = slutt = nyNode;
		} else {
			Node midtNode = start;

			for (int i = 1; i < (stoerrelse+1)/2; i++){
				midtNode = midtNode.neste;
			}

			midt = midtNode;
			nyNode.forrige = midt;
			if(midt != null) {
				nyNode.neste = midt.neste;
				midt.neste.forrige = nyNode;
				midt.neste = nyNode;
			}
			midt = nyNode;
		}
		stoerrelse++;
	}

	public int get(int y) {
		Node nyNode = start;

		for(int i = 0; i < y; i++){
			nyNode = nyNode.neste;
		}
		return nyNode.data;
	}

	protected class Node {
		protected Node neste;
		protected Node forrige;
		protected int data;

    public Node(int x) {
      data = x;
			neste = null;
			forrige = null;
    }
	}
}
