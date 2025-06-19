import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String dropped = sc.nextLine(); 
        String picked = sc.nextLine();  

        int[] countDropped = new int[10]; 
        int[] countPicked = new int[10];

        for (char c : dropped.toCharArray()) {
            countDropped[c - '0']++;
        }

        for (char c : picked.toCharArray()) {
            countPicked[c - '0']++;
        }

        boolean isSame = true;
        for (int i = 0; i < 10; i++) {
            if (countDropped[i] != countPicked[i]) {
                isSame = false;
                break;
            }
        }

        System.out.println(isSame ? "YES" : "NO");
    }
}
