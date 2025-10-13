class Quick extends Sorter {
  public Quick(){}

    void sort() {
      int lav = 0;
      int hoy = A.length - 1;
      if(lt(lav, hoy)){
        int partition = partition(A, lav, hoy);
        quickSort(A, lav, partition - 1);
        quickSort(A, partition + 1, hoy);
      }
    }

    void quickSort(int[] A, int lav, int hoy) {
      if(lt(lav, hoy)){
        int p = partition(A, lav, hoy);
        quickSort(A, lav, p - 1);
        quickSort(A, p + 1, hoy);
      }
    }

    int partition(int[] array, int lav ,int hoy){
      int pivot = array[hoy];
      int midlertidigSted = lav - 1;

      for(int i = lav; leq(i, (hoy -1)) ; i++){
        if(lt(array[i], pivot)){
          midlertidigSted++;
          swap(midlertidigSted, i);
          totalSwaps++;
        }
      }
      swap(midlertidigSted + 1, hoy);
      totalSwaps++;
      return (midlertidigSted + 1);
    }

    String algorithmName() {
      return "quick";
    }
}
