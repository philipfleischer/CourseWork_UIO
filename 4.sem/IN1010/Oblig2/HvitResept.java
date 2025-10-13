class HvitResept extends Resept{
  private int legemiddelHentPris;

  public HvitResept(Legemiddel legemiddel, Lege utskrivendeLege, int pasientId, int reit){
    super(legemiddel, utskrivendeLege, pasientId, reit);
    legemiddelHentPris = legemiddel.hentPris();
  }
  /*
  public HvitResept(Legemiddel legemiddel, Lege utskrivendeLege, int pasientId){
    super(legemiddel, utskrivendeLege, pasientId);
    legemiddelHentPris = legemiddel.hentPris();
  }*/

  public String farge(){
    return "Dette er en hvit resept";
  }
  @Override
  public int prisAaBetale(){
    return legemiddelHentPris;
  }
}
