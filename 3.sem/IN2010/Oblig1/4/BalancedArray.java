import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

class BalancedArray {
  public static void main(String[] args) throws IOException{
    BufferedReader stdin = new BufferedReader(new InputStreamReader(System.in));
    ArrayList<Integer> sortertArray = new ArrayList<>();

    for (String line = stdin.readLine(); line != null; line = stdin.readLine()) {
      sortertArray.add(Integer.parseInt(line));
    }
    lesSortertArray(sortertArray, 0, sortertArray.size() - 1);
  }

  public static void lesSortertArray(ArrayList<Integer> array, int start, int slutt) {
    //int start = 0;
    //int slutt = array.size() - 1;
    if (start < slutt) {
      int midtElement = (start + slutt) / 2;
      System.out.println(array.get(midtElement));
      lesSortertArray(array, midtElement + 1, slutt);
      lesSortertArray(array, start, midtElement - 1);

    }else {
      return;
    }
  }
}
