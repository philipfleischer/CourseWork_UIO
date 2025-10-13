public class Vanlig extends Legemiddel{

  public Vanlig(String navn, int pris, double virkestoff){
    super(navn, pris, virkestoff);
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
    "\nID-en til legemiddelet er "+this.hentId();
  }
}
