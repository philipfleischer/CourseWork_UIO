class BlaaResept extends Resept{
  private int legemiddelHentPris;
  private int rabatt;
  private int rabattNyPris;
  private int legemiddelNyPris;
  private int nyPrisBleSatt;

  public BlaaResept(Legemiddel legemiddel, Lege utskrivendeLege, int pasientId, int reit){
    super(legemiddel, utskrivendeLege, pasientId, reit);
    legemiddelHentPris = legemiddel.hentPris();
  }

  @Override
  public String toString(){
    return "Informasjon tilgjengelig om "+this.hentLegemiddel()+":"+
    "\nResept ID: "+ this.hentId()+
    "\nPasienten sin ID: "+ this.hentPasientId()+
    "\n"+ this.farge()+
    "\nPris å betale er: "+ this.prisAaBetale()+"kr"+
    "\nDu har så mange uttak igjen: "+this.hentReit()+
    ":\nUtskrivende lege: "+ this.hentLege();
  }

  public String farge(){
    return "Dette er en blaa resept";
  }

  public int prisAaBetale(){
    rabattNyPris = (legemiddelHentPris / 100) * 25;
    return rabattNyPris;
  }
}
