class PResept extends HvitResept{
  private int rabatt;
  private int legemiddelHentPris;

  public PResept(Legemiddel legemiddel, Lege utskrivendeLege, int pasientId, int reit){
    super(legemiddel, utskrivendeLege, pasientId, reit);
    rabatt = 108;
    legemiddelHentPris = legemiddel.hentPris();
  }

  public int prisAaBetale(){
    if (legemiddelHentPris > rabatt){
      int nyPris = legemiddelHentPris - rabatt;
      return nyPris;
    }
    return legemiddelHentPris;
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
}
