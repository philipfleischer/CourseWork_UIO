package IN1010.Oblig0;

public class Person {
    Bil3 bil;
    String navn;
    public Person (Bil3 b, String n) {
        bil = b;
        navn = n;
    }

    public void skriv() {
        System.out.println(navn + ": " + bil.regNr);
    }
}
