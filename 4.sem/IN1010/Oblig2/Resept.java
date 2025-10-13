public abstract class Resept{
  protected int pasientId;
  protected int reit;
  public static int iDen = 0;
  public int iD;
  private String legemiddelNavn;
  private String legeNavn;

  public Resept(Legemiddel legemiddel, Lege utskrivendeLege, int pasientId, int reit){
    legemiddelNavn = legemiddel.hentNavn();
    this.pasientId = pasientId;
    this.reit = reit;
    legeNavn = utskrivendeLege.hentNavn();
    iDen++;
    iD = iDen;
  }
  /*
  public Resept(Legemiddel legemiddel, Lege utskrivendeLege, int pasientId){
    legemiddelNavn = legemiddel.hentNavn();
    this.pasientId = pasientId;
    this.reit = reit;
    legeNavn = utskrivendeLege.hentNavn();
    iDen++;
    iD = iDen;
  }*/

  public String toString(){
    return "Informasjon tilgjengelig om "+this.hentLegemiddel()+":"+
    "\nResept ID: "+ this.hentId()+
    "\nPasienten sin ID: "+ this.hentPasientId()+
    "\n"+ this.farge()+
    "\nPris å betale er: "+ this.prisAaBetale()+"kr"+
    "\nDu har så mange uttak igjen: "+this.hentReit()+
    ":\nUtskrivende lege: "+ this.hentLege();
  }

  public int hentId(){
    return iD;
  }

  public String hentLegemiddel(){
    return legemiddelNavn;
  }

  public String hentLege(){
    return legeNavn;
  }

  public int hentPasientId(){
    return pasientId;
  }

  public int hentReit(){
    return reit;
  }

  public boolean bruk(){
    if(reit <= 0){
      return false;
    }
    reit--;
    return true;
  }
  abstract public String farge();

  abstract public int prisAaBetale();
}
