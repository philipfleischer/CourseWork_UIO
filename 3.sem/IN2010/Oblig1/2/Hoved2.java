import java.util.Scanner;

public class Hoved2 {
	public static void main(String[] args) {
		Teque teque = new Teque();

		Scanner stdin = new Scanner(System.in);
		int startTall = Integer.parseInt(stdin.nextLine());

			for(int i = 0; i < startTall; i++) {
				String[] linje = stdin.nextLine().split(" ");

				if(linje[0].equals("push_back")) {
					teque.push_back(Integer.parseInt(linje[1]));
				}else if (linje[0].equals("push_front")) {
					teque.push_front(Integer.parseInt(linje[1]));
				}else if (linje[0].equals("push_middle")) {
					teque.push_middle(Integer.parseInt(linje[1]));
				}else if (linje[0].equals("get")) {
					System.out.println(teque.get(Integer.parseInt(linje[1])));
				}else {
					System.exit(0);
				}
			}
		}

}
