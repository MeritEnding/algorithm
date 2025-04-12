// 구현 문제
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // h, m을 각각 받음
        int h = sc.nextInt(); // 시
        int m = sc.nextInt(); // 분

        // m을 먼저 처리해줌
        m -= 30;

        // m이 만약에 음수로 되버렸다 => h가 하나 빠져야됨
        // 그리고 m을 정상화하기위해서는 +60을 해줘야해
        if (m < 0) {
            h -= 1;
            m += 60;
            // h가 0시보다 작다는것은 23시(오후 11시) 였으니까!
            if (h < 0) {
                h = 23;
            }
        }

        System.out.println(h + " " + m);
    }
}
