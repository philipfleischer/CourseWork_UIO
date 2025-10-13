package IN1010.Oblig0;

public class Bil3 {
    String regNr;
    public Bil3 (String rNr){
        regNr = rNr;
    }
    
    public void skriv_ut() {
        System.out.println("Jeg er en bil!");
    }

    public void skriv_regNr(Bil3 bil) {
        System.out.println("Registreringsnummer: " + bil.regNr);
    }

    public String hentNummer(Bil3 bil) {
        return bil.regNr;
    }
}
