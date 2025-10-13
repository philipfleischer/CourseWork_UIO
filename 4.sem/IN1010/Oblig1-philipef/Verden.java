package IN1010.Oblig1;

public class Verden {
    Rutenett rutenett;
    int genNr;

    public Verden(int r, int k) {
        rutenett = new Rutenett(r, k);
        genNr = 0;
        rutenett.fyllMedTilfeldigeCeller();
        rutenett.kobleAlleCeller();
    }

    public void tegn() {
        rutenett.tegnRutenett();
        System.out.println("Celle generasjon: " + genNr);
        System.out.println("Levende Celler i rutenettet: " + rutenett.antallLevende());
    }

    public void oppdatering() {
        for (int radIndeks = 0; radIndeks < rutenett.antRader; radIndeks++) {
            for (int kolIndeks = 0; kolIndeks < rutenett.antKolonner; kolIndeks++) {
                rutenett.rutene[radIndeks][kolIndeks].tellLevendeNaboer();
            }
        }
        for (int rIndeks = 0; rIndeks < rutenett.antRader; rIndeks++) {
            for (int kIndeks = 0; kIndeks < rutenett.antKolonner; kIndeks++) {
                rutenett.rutene[rIndeks][kIndeks].oppdaterStatus();
            }
        }
        genNr++;
    }
}
