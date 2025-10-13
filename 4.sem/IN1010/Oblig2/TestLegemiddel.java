public class TestLegemiddel{
  public static void main(String[] args){
    Legemiddel morfin = new Narkotisk("Morfin", 2500, 150.4, 3);
    //morfin.oekId();
    morfin.settNyPris(200);
    System.out.println(morfin);

    System.out.println();

    Legemiddel neseSpray = new Vanedannende("Nesespray", 250, 15.34, 2);
    //neseSpray.oekId();
    neseSpray.settNyPris(900);
    System.out.println(neseSpray);

    System.out.println();

    Legemiddel aerius = new Vanlig("Aerius", 2500, 10.4);
    //aerius.oekId();
    aerius.settNyPris(56);
    System.out.println(aerius);

    System.out.println();
    System.out.println(morfin);
    System.out.println();
    System.out.println(morfin);
    System.out.println();
    System.out.println(neseSpray);
  }
}
