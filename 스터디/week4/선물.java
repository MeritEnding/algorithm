import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();         
        int[] gifts = new int[N];      
        for (int i = 0; i < N; i++) {
            gifts[i] = sc.nextInt();  
        }

        int gcd = gifts[0];
        for (int i = 1; i < N; i++) {
            gcd = getGCD(gcd, gifts[i]);
        }
        System.out.println(gcd);      
    }
    private static int getGCD(int a, int b) {
        while (b != 0) {
            int tmp = a % b;
            a = b;
            b = tmp;
        }
        return a;
    }
}
