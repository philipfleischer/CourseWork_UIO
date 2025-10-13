class MillitaerResept extends HvitResept{
  private int reit;

  public MillitaerResept(Legemiddel legemiddel, Lege utskrivendeLege, int pasientId){
    super(legemiddel, utskrivendeLege, pasientId, 3);
    this.reit = 3;
  }

  public int prisAaBetale(){
    return 0;
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

  @Override
  public int hentReit(){
    return reit;
  }

  @Override
  public boolean bruk(){
    if(reit <= 0){
      return false;
    }
    reit--;
    return true;
  }
}
