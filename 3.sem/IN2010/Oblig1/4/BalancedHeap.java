import java.util.PriorityQueue;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BalancedHeap {
    public static void main(String[] args) throws IOException {
      BufferedReader stdin = new BufferedReader(new InputStreamReader(System.in));
      PriorityQueue<Integer> prioKoe = new PriorityQueue<>();

      for (String line = stdin.readLine(); line != null; line = stdin.readLine()) {
        prioKoe.offer(Integer.parseInt(line));
      }

      lesSortertHeap(prioKoe, 0, prioKoe.size() - 1);
  }

  public static void lesSortertHeap(PriorityQueue<Integer> pk, int start, int slutt) {
      int stoerrelse = pk.size();
      int midtElement = (start + slutt) / 2;

      if (stoerrelse > 1) {
          PriorityQueue<Integer> nyPk = new PriorityQueue<>();
          int teller = 0;
          while (teller < (stoerrelse / 2)) {
              nyPk.offer(pk.poll());
              teller++;
          }
          System.out.println(pk.poll());
          lesSortertHeap(pk, start, midtElement - 1);
          lesSortertHeap(nyPk, midtElement + 1, slutt);
      }else {
        return;
      }
  }
}
