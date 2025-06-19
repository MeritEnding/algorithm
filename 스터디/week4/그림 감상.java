import java.util.Scanner;

public class Main {
    static char[][] board = new char[4][4];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        for (int i = 0; i < 4; i++) {
            board[i] = sc.nextLine().toCharArray();
        }

        if (check()) {
            System.out.println("yes");
            return;
        }

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (board[i][j] == 'O') {
                    board[i][j] = 'X';  
                    if (check()) {
                        System.out.println("yes");
                        return;
                    }
                    board[i][j] = 'O';  
                }
            }
        }

        System.out.println("no");
    }

    static boolean check() {
        for (int i = 0; i < 3; i++) {  
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == 'X' &&
                    board[i][j+1] == 'X' &&
                    board[i+1][j] == 'X' &&
                    board[i+1][j+1] == 'X') {
                    return true;
                }
            }
        }
        return false;
    }
}
