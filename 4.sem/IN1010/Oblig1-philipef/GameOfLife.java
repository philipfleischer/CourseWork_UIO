package IN1010.Oblig1;

import java.util.Scanner;

public class GameOfLife {
    public static void main(String[] arg) {
        Scanner scanner = new Scanner(System.in);
        String svar = "";
        System.out.print("Skriv inn antall rader til Rutenettet: ");
        int r = scanner.nextInt();
        System.out.print("Skriv inn antall kolonner til Rutenettet: ");
        int k = scanner.nextInt();
        Verden verden = new Verden(r, k);

        while (!svar.equals("Q")) {
            verden.tegn();
            verden.oppdatering();
            System.out.print("Stoppe spillet? = (Q): ");
            svar = scanner.nextLine();
        }
        scanner.close();
    }
}
