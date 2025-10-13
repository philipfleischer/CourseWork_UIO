import java.util.Scanner;

class GuessTheNumber {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int randomNumber = (int) (Math.random()*(1000-1));

    for (int i = 0; i < 10; i++) {
      //System.out.println("Gjett ett tall mellom 1-1000. Du har 10 forsok");
      int tall = Integer.parseInt(in.nextLine());
      if (randomNumber > tall) {
        System.out.println("higher");
      }else if (randomNumber == tall) {
        System.out.println("correct");
        break;
      }else {
        System.out.println("lower");
      }
    }
  }
}
