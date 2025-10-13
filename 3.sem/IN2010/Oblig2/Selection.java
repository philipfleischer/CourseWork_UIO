
class Selection extends Sorter {

  public Selection() {}

  void selectionSort(int[] array) {
    int lengde = array.length;
    for (int i = 0; lt(i, lengde - 1); i++) {
      int minsteElement = i;

      for (int j = i+1; lt(j, lengde); j++) {
        if (lt(array[j], array[minsteElement])) {
          minsteElement = j;
        }
      }

      int temp = array[minsteElement];
      array[minsteElement] = array[i];
      array[i] = temp;

      //Får av en eller annen grunn ikke denne til å fungere:
      //swap(minsteElement, i);
      //Øker den derfor manuelt
      swaps++;
      totalSwaps++;
    }
  }

  void sort() {
    Selection s = new Selection();
    s.selectionSort(A);

  }

  String algorithmName() {
    return "selection";
  }


}
