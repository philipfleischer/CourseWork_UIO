import java.util.Scanner;

class BinaerSoek1 {
  public static void main(String[] args) {
    BinaerSoek1 bs = new BinaerSoek1();
    Scanner in = new Scanner(System.in);
    System.out.println("Vennligst skriv inn et array (1 2 3 43 123): ");
    String[] strengArray = in.nextLine().split(" ");
    int[] array = new int[strengArray.length];
    for (int i = 0; i < strengArray.length; i++) {
      array[i] = Integer.parseInt(strengArray[i]);

    }
    System.out.println("Vennligst skriv inn et tall: ");
    int tall = Integer.parseInt(in.nextLine());

    for (int j = 0; j < array.length; j++){
      System.out.print(array[j] + ", ");
    }
    System.out.println(tall);

    System.out.println(bs.erX(array, tall));
  }

  public boolean erX(int[] a, int x) {
    for (int e = 0; e < a.length; e++) {
      if (x == a[e]) {
        return true;
      }
    }
    return false;
  }
}
