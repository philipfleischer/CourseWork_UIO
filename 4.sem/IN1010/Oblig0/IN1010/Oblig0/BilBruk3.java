package IN1010.Oblig0;

public class BilBruk3 {
    public static void main(String[] args) {
        Bil3 bil = new Bil3("KJ20968");
        Person person = new Person(bil, "Philip");
    
        person.skriv();   
    }
}
