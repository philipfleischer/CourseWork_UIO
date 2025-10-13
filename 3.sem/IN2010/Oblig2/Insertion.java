
class Insertion extends Sorter {

  public Insertion() {}


  public void sort() {
    //int lengde = array.length;
    //Bruker lt-metoden fra Sorter.java, for å telle sammenligninger
    //samtidig som at opersjonene jeg ønsker å foreta meg blir gjort
    for (int i = 1; lt(i, A.length); i++) {
      int j = i-1;
      int midlertidigSted = A[i];
      //Bruker geq- og gt-metoden fra Sorter.java, for å telle sammenligninger
      //samtidig som at opersjonene jeg ønsker å foreta meg blir gjort
      while (geq(j, 0) && gt(A[j], midlertidigSted)) {
        A[j+1] = A[j];
        j = j - 1;
        swaps++;
        totalSwaps++;
      }
      A[j+1] = midlertidigSted;
    }
  }


  public String algorithmName() {
    return "insertion";
  }
}
