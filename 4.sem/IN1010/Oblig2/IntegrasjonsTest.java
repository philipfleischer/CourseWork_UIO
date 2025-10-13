class IntegrasjonsTest{
  public static void main(String[] args){
    Legemiddel aerius = new Vanlig("Aerius", 250, 10.3);
    System.out.println(aerius);
    System.out.println();
    System.out.println();
    Lege lege1 = new Lege("Anders Bye");
    System.out.println();
    Resept enBlaaResept = new BlaaResept(aerius, lege1, 145, 1);
    System.out.println(enBlaaResept);

    System.out.println();
    System.out.println();
    System.out.println();
    System.out.println();

    Legemiddel morfin = new Narkotisk("Morfin", 2500, 150.4, 3);
    System.out.println(morfin);
    System.out.println();
    System.out.println();
    Lege lege2 = new Spesialist("Parvitz Susa", "R-2022-0056");
    System.out.println();
    Resept enHvitResept = new HvitResept(morfin, lege2, 143, 1);
    System.out.println(enHvitResept);
    System.out.println(lege2);

    System.out.println();
    System.out.println();
    System.out.println();
    System.out.println();

    Legemiddel neseSpray = new Vanedannende("Nesespray", 250, 15.34, 2);
    System.out.println(neseSpray);
    System.out.println();
    System.out.println();
    Lege lege3 = new Lege("Titill bokard");
    Resept enHvitResept2 = new MillitaerResept(neseSpray, lege3, 144);
    System.out.println(enHvitResept2);
    System.out.println(enHvitResept2.bruk());
    System.out.println("Nå har du så mange uttak igjen: "+enHvitResept2.hentReit());

    System.out.println();
    System.out.println();
    System.out.println();
    System.out.println();

    Legemiddel etVanligLegemiddel = new Vanlig("Vanlig Legemiddel", 2500, 10.4);
    System.out.println(etVanligLegemiddel);
    System.out.println();
    System.out.println();
    Lege lege4 = new Lege("Trudy Beckmann");
    Resept enHvitResept3 = new PResept(etVanligLegemiddel, lege4, 145, 1);
    System.out.println(enHvitResept3);
  }
}
