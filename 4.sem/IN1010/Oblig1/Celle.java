package IN1010.Oblig1;

public class Celle {
    boolean dod;
    Celle[] naboer;
    int antNaboer;
    int antLevendeNaboer;

    public Celle() {
        dod = true;
        naboer = new Celle[8];
        antNaboer = 0;
        antLevendeNaboer = 0;
    }

    public void settDoed() {
        dod = true;
    }

    public void settLevende() {
        dod = false;
    }

    public boolean erLevende() {
        return dod;
    }

    public char hentStatusTegn() {
        if (dod) {
            return '.';
        }else {
            return 'O';
        }
    }

    public void leggTilNabo(Celle nabo) {
        naboer[antNaboer] = nabo;
        antNaboer++;
    }

    public void tellLevendeNaboer() {
        antLevendeNaboer = 0;
        for (int i = 0; i < naboer.length; i++) {
            if (naboer[i] != null) {
                if (naboer[i].erLevende()){
                    antLevendeNaboer++;
                }
            }
        }
    }

    public void oppdaterStatus() {
        if(!dod) {
            if (antLevendeNaboer < 2 || antLevendeNaboer > 3) {
                settDoed();
            }
        }else {
            if (antLevendeNaboer == 3) {
                settLevende();
            }
        }
    }
}
