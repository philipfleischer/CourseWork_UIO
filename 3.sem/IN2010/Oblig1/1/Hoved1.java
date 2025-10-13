import java.util.Scanner;

public class Hoved1 {
	public static void main(String[] args) {
		Set set = new Set();

		Scanner stdin = new Scanner(System.in);
		int startTall = Integer.parseInt(stdin.nextLine());

			for(int i = 0; i < startTall; i++) {
				String[] linje = stdin.nextLine().split(" ");

				if(linje[0].equals("insert")) {
					set.insert(Integer.parseInt(linje[1]));
				}else if (linje[0].equals("contains")) {
					System.out.println(set.contains(Integer.parseInt(linje[1])));
				}else if (linje[0].equals("remove")) {
					set.remove(Integer.parseInt(linje[1]));
				}else if (linje[0].equals("size")) {
					System.out.println(set.size());
				}else {
					System.exit(0);
				}
			}
		}

}
