import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int a = scanner.nextInt();  
        int b = scanner.nextInt();  
        int c = scanner.nextInt();

        int result = (int) Math.ceil(10.0 * c / a);
        System.out.println(result);
    }
}
