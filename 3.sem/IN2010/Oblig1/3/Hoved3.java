import java.util.HashMap;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Hoved3 {
	public static void main(String[] args) throws IOException {
		HashMap<String, String> hashMap = new HashMap<>();
    InputStreamReader iSR = new InputStreamReader(System.in);
		BufferedReader stdin = new BufferedReader(iSR);
		String katteGren = stdin.readLine();

    while (!katteGren.equals("-1")){
			String[] linjeStykke = stdin.readLine().split(" ");

			if(linjeStykke[0].equals("-1")){
				break;
      }

			for(int j = 1; j < linjeStykke.length; j++) {
				hashMap.put(linjeStykke[j], linjeStykke[0]);
      }
		}

		for(int e = 0; e < hashMap.size(); e++) {
      if (katteGren!=null){
        System.out.print(katteGren + " ");
        katteGren = hashMap.get(katteGren);
      }else {
        break;
      }
		}
    System.out.println();
	}
}
