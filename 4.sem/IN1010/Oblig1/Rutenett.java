package IN1010.Oblig1;

public class Rutenett {

    Rutenett[][] rutene;
    int antRader;
    int antKolonner;
    public Rutenett(int x, int y) {
        antRader = x;
        antKolonner = y;
        rutene = new Rutenett[antRader][antKolonner];
    }

    public void lagCelle() {
        Celle celle = new Celle();
    }

}
