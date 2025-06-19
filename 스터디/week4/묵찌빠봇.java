import java.util.*;

public class Main {
    static int[] bot1, bot2;
    static int N, M;

    // 1: bot1 승, 2: bot2 승, 0: 비김
    static int rpsResult(int a, int b) {
        if (a == b) return 0;
        if ((a == 1 && b == 3) || (a == 2 && b == 1) || (a == 3 && b == 2))
            return 1;
        else
            return 2;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();

        bot1 = new int[N];
        bot2 = new int[M];

        for (int i = 0; i < N; i++) bot1[i] = sc.nextInt();
        for (int i = 0; i < M; i++) bot2[i] = sc.nextInt();

        int firstTurn = decideFirstTurn();
        if (firstTurn == 0) {
            System.out.println(0);
            return;
        }

        int winner = mukjjippa(firstTurn);
        System.out.println(winner);
    }

    static int decideFirstTurn() {
        int idx1 = 0, idx2 = 0;
        int limit = N * M * 3;
        for (int i = 0; i < limit; i++) {
            int r = rpsResult(bot1[idx1], bot2[idx2]);
            if (r == 1) return 1;
            else if (r == 2) return 2;

            idx1 = (idx1 + 1) % N;
            idx2 = (idx2 + 1) % M;
        }
        return 0;
    }

    static int mukjjippa(int firstTurn) {
        int idx1 = 0, idx2 = 0;
        int attacker = firstTurn;
        int defender = (attacker == 1) ? 2 : 1;

        Set<String> visited = new HashSet<>();

        while (true) {
            String state = idx1 + "," + idx2 + "," + attacker;
            if (visited.contains(state)) return 0;
            visited.add(state);

            int attHand = (attacker == 1) ? bot1[idx1] : bot2[idx2];
            int defHand = (defender == 1) ? bot1[idx1] : bot2[idx2];

            if (attHand == defHand) {
                return attacker;
            } else {
                int r = rpsResult(attHand, defHand);
                if (r == defender) {
                    int temp = attacker;
                    attacker = defender;
                    defender = temp;
                }
            }

            idx1 = (idx1 + 1) % N;
            idx2 = (idx2 + 1) % M;
        }
    }
}
