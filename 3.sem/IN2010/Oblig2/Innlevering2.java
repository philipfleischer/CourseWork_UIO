import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.lang.Math;

class Innlevering2 {
  public static void main(String[] args) throws Exception{
    String filnavn = args[0];
    File fil = new File(filnavn);
    BufferedReader br = new BufferedReader(new FileReader(fil));
    int[] A = br.lines().mapToInt(i -> Integer.parseInt(i)).toArray();
    br.close();

    long t = System.nanoTime();
    Innlevering2Runner.runAlgsPart1(A, filnavn);
    Innlevering2Runner.runAlgsPart2(A, filnavn);

    long tid = (System.nanoTime()-t)/1000;
    System.out.println("Tid det tok (i mikrosekunder): " + tid);

    System.out.println("Antall bytter: " + Sorter.totalSwap());

    System.out.println("Antall sammenligninger: " + Math.abs(Sorter.totalComp()));

  }
}
