import java.lang.Math;

class Merge extends Sorter{

  public Merge() {}

    void merge(int array[], int venstre, int midten, int hoyre) {
      int elementV = midten - venstre + 1;
      int elementH = hoyre - midten;
      int[] arrayVenstre = new int[elementV];
      int[] arrayHoyre = new int[elementH];

      for (int i = 0; lt(i, elementV); i++) {
        totalComps++;
        arrayVenstre[i] = array[venstre + i];
      }

      for (int j = 0; lt(j, elementH); j++) {
        arrayHoyre[j] = array[midten + 1 + j];
      }

      int i = 0;
      int j = 0;
      while (lt(i, elementV) && lt(j, elementH)) {
        if (leq(arrayVenstre[i], arrayHoyre[j])) {
          array[venstre] = arrayVenstre[i];
          i++;
        } else {
          array[venstre] = arrayHoyre[j];
          j++;
        }
        venstre++;
      }

      while (lt(i, elementV)) {
        array[venstre] = arrayVenstre[i];
        i++;
        venstre++;
      }

      while (lt(j, elementH)) {
        array[venstre] = arrayHoyre[j];
        j++;
        venstre++;
      }
    }

    void mergeSort(int[] array, int venstre, int hoyre) {
      if (lt(venstre, hoyre)) {
        //int midten = (int) Math.floor((array.length/2));
        int midten = venstre + (hoyre - venstre) / 2;
        mergeSort(array, venstre, midten);
        mergeSort(array, midten + 1, hoyre);
        merge(array, venstre, midten, hoyre);
      }
    }

    void sort() {
      Merge m = new Merge();
      int venstre = 0;
      int hoyre = A.length - 1;
      m.mergeSort(A, venstre, hoyre);
    }

    String algorithmName() {
      return "merge";
    }
}
