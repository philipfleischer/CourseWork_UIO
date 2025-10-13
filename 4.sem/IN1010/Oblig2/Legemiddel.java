public abstract class Legemiddel{
  protected String navn;
  protected int pris;
  protected double virkestoff;
  public static int iDen = 0;
  public int iD;

  public Legemiddel(String navn, int pris, double virkestoff){
    this.navn = navn;
    this.pris = pris;
    this.virkestoff = virkestoff;
    iDen++;
    iD = iDen;
  }

  public String toString(){
    return "Informasjon tilgjengelig om "+this.navn+
    ":\nPrisen er "+this.pris+"kr\nMengde virkestoff er "+this.virkestoff+"mg"+
    "\nID-en til legemiddelet er "+this.hentId();
  }

  public int hentId(){
    return iD;
  }

  public int hentPris(){
    return pris;
  }

  public double hentVirkestoff(){
    return virkestoff;
  }

  public int settNyPris(int nyPris){
    pris = nyPris;
    return pris;
  }

  public String hentNavn(){
    return navn;
  }
}
