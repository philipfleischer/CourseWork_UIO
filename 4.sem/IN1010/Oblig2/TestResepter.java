public class TestResepter{
  public static void main(String[] args){

    Legemiddel aerius = new Vanlig("Aerius", 250, 10.3);
    Lege lege1 = new Lege("Anders Bye");
    System.out.println();
    Resept blaaResept1 = new BlaaResept(aerius, lege1, 145, 1);
    System.out.println(blaaResept1);

    Legemiddel morfin = new Narkotisk("Morfin", 2500, 150.4, 3);
    Lege lege2 = new Spesialist("Parvitz Susa", "Her er en kontrollId. Den ble hentet fra Narkotisk og lagt inn i konsturktøren til Spesialist");
    System.out.println();
    Resept hvitResept1 = new HvitResept(morfin, lege2, 143, 1);
    System.out.println(hvitResept1);

    System.out.println();

    Legemiddel neseSpray = new Vanedannende("Nesespray", 250, 15.34, 2);
    Lege lege3 = new Lege("Titill bokard");
    Resept millResept1 = new MillitaerResept(neseSpray, lege3, 144);
    System.out.println(millResept1);
    System.out.println(millResept1.bruk());
    System.out.println(millResept1.bruk());
    System.out.println(millResept1.bruk());
    System.out.println(millResept1.bruk());
    System.out.println("Du har "+millResept1.hentReit()+" uttak igjen.");

    System.out.println();

    Legemiddel etVanligLegemiddel = new Vanlig("Vanlig Legemiddel", 2500, 10.4);
    Lege lege4 = new Lege("Trudy Beckmann");
    Resept p_Resept1 = new PResept(etVanligLegemiddel, lege4, 145, 1);
    System.out.println(p_Resept1);
  }
}
