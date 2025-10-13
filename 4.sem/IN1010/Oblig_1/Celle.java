package IN1010.Oblig_1;
public class Celle {
    boolean doed;
    Celle[] naboer;
    int antNaboer;
    int antLevendeNaboer;

    public Celle() {
        doed = true;
        naboer = new Celle[8];
        antNaboer = 0;
        antLevendeNaboer = 0;
    }

    public void settDoed() { doed = true; }

    public void settLevende() { doed = false; }

    public boolean erLevende() {
        if (doed) { return false;}
        else { return true; }
    }

    public char hentStatusTegn() {
        if (doed) { return '.';}
        else { return 'O'; }
    }

    public void leggTilNabo(Celle nabo) {
        naboer[antNaboer] = nabo;
        antNaboer++;
    }

    public void tellLevendeNaboer() {
        antLevendeNaboer = 0;
        for (int i = 0; i < naboer.length; i++) {
            if (naboer[i] != null) {            
                if (naboer[i].erLevende()) {
                    antLevendeNaboer++;
                }
            }
        }
    }

    public void oppdaterStatus() {
        if (!doed) {
            if (antLevendeNaboer < 2) { settDoed(); }
            else if (antLevendeNaboer > 3) { settDoed(); }
        }
        else {
            if (antLevendeNaboer == 3) { settLevende(); }
            settDoed();
        }
    }
}