package IN1010.Oblig_1;
public class Rutenett {
    int antRader;
    int antKolonner;
    Celle[][] rutene;

    public Rutenett(int r, int k) {
        antRader = r;
        antKolonner = k;
        rutene = new Celle[antRader][antKolonner];
    }

    public void lagCelle(int r, int k) {
        Celle celle = new Celle();
        if (Math.random() <= 0.3333) { celle.settLevende(); }
        rutene[r][k] = celle;
    }

    public void fyllMedTilfeldigeCeller() {
        for (int r = 0; r < antRader; r++) {
            for (int k = 0; k < antKolonner; k ++) { lagCelle(r, k); }
        }
    }

    public Celle hentCelle(int r, int k) {
        if (k >= rutene[0].length || r >= rutene.length || k < 0 || r < 0) { return null; }
        else{ return rutene[r][k]; }
    }

    public void tegnRutenett() {
        //Skriver ut 10 tomme linjer
        for (int i = 0; i <= 10; i++) {
            System.out.print("\n");
        }

        for (int r = 0; r < rutene.length; r++) {
            System.out.print("+---".repeat(rutene[0].length));
            System.out.print("+\n");
            for (int k = 0; k < rutene[0].length; k++) {
                System.out.print("|");
                System.out.print(" " + rutene[r][k].hentStatusTegn() + " ");    
            }
            System.out.print("|");
            System.out.print("\n");
        }
        System.out.print("+---".repeat(rutene[0].length));
        System.out.print("+\n");
    }

    public void settNaboer(int r, int k) {
        Celle celle = hentCelle(r, k); 
        for (int radIndeks = (r-1); radIndeks < (r+2); radIndeks++) {
            for (int kolIndeks = (k-1); kolIndeks < (k+2); kolIndeks++) {
                if (radIndeks == r && kolIndeks == k) { kolIndeks++; }
                if (hentCelle(radIndeks,kolIndeks) != null) {
                    //celle.legfTilNabo(radIndeks, kolIndeks);
                    celle.leggTilNabo(hentCelle(radIndeks, kolIndeks));
               }
            }
        }
    }

    public void kobleAlleCeller() {
        for (int r = 0; r < antRader; r++) {
            for (int k = 0; k < antKolonner; k++) {
                settNaboer(r, k);
            }
        }
    }

    public int antallLevende() {
        int cellerILive = 0;
        for (int r = 0; r < antRader; r++) {
            for (int k = 0; k < antKolonner; k++) {
                if (rutene[r][k].erLevende()) { cellerILive++; }
            }
        }
        return cellerILive;
    }
}
