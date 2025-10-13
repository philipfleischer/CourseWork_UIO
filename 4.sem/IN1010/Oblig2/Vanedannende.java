public class Vanedannende extends Legemiddel{
  private int styrke;

  public Vanedannende(String navn, int pris, double virkestoff, int styrke){
    super(navn, pris, virkestoff);
    this.styrke = styrke;
  }

  public int hentVanedannendeStyrke(){
    return styrke;
  }

  @Override
  public int settNyPris(int nyPris){
    pris = nyPris;
    return pris;
  }

  @Override
  public String toString(){
    return "Informasjon tilgjengelig om "+this.navn+
    ":\nPrisen er "+this.pris+"kr\nMengde virkestoff er "+this.virkestoff+"mg"+
    ":\nStyrken til legemiddelet er: "+this.hentVanedannendeStyrke()+
    "\nID-en til legemiddelet er "+this.hentId();
  }
}
