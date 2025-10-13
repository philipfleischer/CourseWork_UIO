import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Huffsa {

    private static String user = "philipef"; // Skriv ditt UiO-brukernavn
    private static String pwd = "besiesae2O"; // Skriv passordet til _priv-brukeren du fikk i mail fra USIT
    // Tilkoblings-detaljer
    private static String connectionStr =
        "user=" + user + "_priv&" +
        "port=5432&" +
        "password=" + pwd + "";
    private static String host = "jdbc:postgresql://dbpg-ifi-kurs03.uio.no";

    public static void main(String[] agrs) {

        try {
            // Last inn driver for PostgreSQL
            Class.forName("org.postgresql.Driver");
            // Lag tilkobling til databasen
            Connection connection = DriverManager.getConnection(host + "/" + user
                    + "?sslmode=require&ssl=true&sslfactory=org.postgresql.ssl.NonValidatingFactory&" + connectionStr);

            int ch = 0;
            while (ch != 3) {
                System.out.println("--[ HUFFSA ]--");
                System.out.println("Vennligst velg et alternativ:\n 1. Sok etter planet\n 2. Legg inn resultat\n 3. Avslutt");
                ch = getIntFromUser("Valg: ", true);

                if (ch == 1) {
                    planetSok(connection);
                } else if (ch == 2) {
                    leggInnResultat(connection);
                }
            }
        } catch (SQLException|ClassNotFoundException ex) {
            System.err.println("Error encountered: " + ex.getMessage());
        }
    }

    private static void planetSok(Connection connection)  throws SQLException {
        System.out.println("--[ HUFFSA ]--");
        String molekyl1 = getStrFromUser("Molekyl 1: ");
        String molekyl2 = getStrFromUser("Molekyl 2: ");

        String sporring = ("SELECT p.navn, p.masse, s.masse, s.avstand, p.liv" +
        " FROM stjerne AS s" +
        " INNER JOIN planet AS p" +
        " ON (p.stjerne = s.navn)" +
        " INNER JOIN materie AS m" +
        " ON (m.planet = p.navn)");

        if (!molekyl2.equals("")) {
          sporring += " INNER JOIN materie AS mm" +
          " ON (mm.planet = p.navn)" +
          " WHERE (m.molekyl = ?) AND (mm.molekyl = ?)";
        }else {
          sporring += " WHERE (m.molekyl = ?)";
        }
        sporring += " ORDER BY s.avstand DESC;";

        PreparedStatement statement = connection.prepareStatement(sporring);
        statement.setString(1, molekyl1);

        if (!molekyl2.equals("")){
          statement.setString(2, molekyl2);
        }

        ResultSet rows = statement.executeQuery();

        if (!rows.next()) {
          System.out.println("No results");
          return;
        }

        do {
          System.out.println("--[ Planet ]--\n" +
          "Navn: " + rows.getString(1) + "\n" +
          "Planet-masse: " + rows.getInt(2) + "\n" +
          "Stjerne-masse: " + rows.getInt(3) + "\n" +
          "Stjerne-distanse: " + rows.getInt(4) + "\n" +
          "Bekreftet liv: " + rows.getString(5));

          System.out.println("\n");
        } while (rows.next());
    }



    private static void leggInnResultat(Connection connection) throws SQLException {
        System.out.println("--[ LEGG INN RESULTAT ]--");
        String navn = getStrFromUser("Planet: ");
        String skummel = getStrFromUser("Skummel: ");
        String intelligent = getStrFromUser("Intelligent: ");
        String beskrivelse = getStrFromUser("Beskrivelse: ");

        PreparedStatement statement = connection.prepareStatement("UPDATE planet"+
        " SET skummel = ?, intelligent = ?, beskrivelse = ?" +
        " WHERE navn = ?;");

        if (skummel.equals("j")) {
          statement.setBoolean(1, true);
        }else {
          statement.setBoolean(1, false);
        }
        if (intelligent.equals("j")) {
          statement.setBoolean(2, true);
        }else {
          statement.setBoolean(2, false);
        }
        statement.setString(3, beskrivelse);
        statement.setString(4, navn);

        statement.execute();
        System.out.println("Resultat lagt inn.");
    }

    /**
     * Utility method that gets an int as input from user
     * Prints the argument message before getting input
     * If second argument is true, the user does not need to give input and can leave
     * the field blank (resulting in a null)
     */
    private static Integer getIntFromUser(String message, boolean canBeBlank) {
        while (true) {
            String str = getStrFromUser(message);
            if (str.equals("") && canBeBlank) {
                return null;
            }
            try {
                return Integer.valueOf(str);
            } catch (NumberFormatException ex) {
                System.out.println("Please provide an integer or leave blank.");
            }
        }
    }

    /**
     * Utility method that gets a String as input from user
     * Prints the argument message before getting input
     */
    private static String getStrFromUser(String message) {
        Scanner s = new Scanner(System.in);
        System.out.print(message);
        return s.nextLine();
    }
}
