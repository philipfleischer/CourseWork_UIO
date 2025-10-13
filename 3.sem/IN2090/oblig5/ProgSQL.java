

class SLEtt {
  public static void main(String[] args) {

  }

//Under er en oppgave som bruker SQL-spørringer!! der vi skal registrere en bruker inn i databasen
  private static void register(Connection connection) {
    System.oout.println(" -- REGISTER NEW USER --");
    String username = getStrFromUser("Username: ");
    String password = getStrFromUser("Password: ");
    String name = getStrFromUser("Name: ");
    String address = getStrFromUser("Address: ");

    PreparedStatement statement = connection.prepareStatement("INSERT INTO ws.users(name, username, password, address)"+
    "VALUES (?, ?, ?, ?);");

    statement.setString(1, name);
    statement.setString(2, username);
    statement.setString(3, password);
    statement.setString(4, address);

    //Bruker kun dette for å endre på databasen
    statement.execute();
    System.out.println("NEW USER ADDED!");
  }

//Under er en oppgave som er å logge inn, der man må søke om personen finnes i databasen
  private static void register(Connection connection) {
    System.oout.println(" -- LOGIN USER --");
    String username = getStrFromUser("Username: ");
    String password = getStrFromUser("Password: ");

    //Vi skal hente ut brukernavnet og passordet
    PreparedStatement statement = connection.prepareStatement("SELECT username, name, FROM ws.users"+
    "WHERE username = ? AND password = ?;");

    statement.setString(1, username);
    statement.setString(2, password);

    //Bruker denne for å skrive SELECT spørringer
    ResultSet rows = statement.executeQuery();

    if (!rows.next()) {
      System.out.println("Incorrect username or password");
      return null;
    }else {
      System.out.println("Welcome " + rows.getString(2));
      return rows.getString(1);
    }
  }

//Oppgave som gjør at en innlogget bruker kan søke i databasen etter navn på produkt og type kategori hvis det trengs
//Oppgave 2 i obligen er lik denne
  private static void search(Connection connection, String username) {
    System.out.println(" -- SEARCH --");
    String name = getStrFromUser("Search: ");
    String category = getStrFromUser("Category: ");

    String q = "SELECT p.id, p.ame, p.price, c.name AS category, p.description" +
    "FROM ws.products AS p INNER JOIN ws.categories AS c USING (cid)" +
    "WHERE p.name LIKE ?";

    if (!category.equals("")) {
      q += " AND c.name = ?";
    }

    q+= ";";

    PreparedStatement statement = connection.prepareStatement(q);
    statement.setString(1, '%' + name + '%');

    if (!category.equals("")){
      statement.setString(2, category);
    }

    ResultSet rows = statement.executeQuery();

    if (!rows.next()) {
      System.out.println("No results");
      return;
    }

    do {
      System.out.println("=== " + rows.getString(2) + " ===\n" +
      "Product ID: " + rows.getInt(1) + "\n" +
      "Price: " + rows.getFloat(3) + "\n" +
      "Category: " + rows.getString(4));
      if (!rows.getString(5).equals("NULL")) {
        System.out.println("Description: " + rows.getString(5));
      }
      System.out.println("\n");
    } while (rows.next());

  }
}
















//
