import java.util.Scanner;
import java.util.ArrayList;

class Backspace {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    ArrayList<String> liste = new ArrayList<>();

    String[] streng = in.nextLine().split("");

    for (int i = 0; i < streng.length; i++) {
      if (!streng[i].equals("<")) {
        liste.add(streng[i]);
      }else {
        liste.remove(liste.size()-1);
      }
    }
    for (String s : liste) {
      System.out.print(s);
    }
    System.out.println();
  }
}
