package IN1010.Oblig0;

public class Bil2 {
    String regNr;
    public Bil2 (String rNr){
        regNr = rNr;
    }
    
    public void skriv_ut() {
        System.out.println("Jeg er en bil!");
    }

    public void skriv_regNr(Bil2 bil) {
        System.out.println("Registreringsnummer: " + bil.regNr);
    }
}
