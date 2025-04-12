// 구현 문제
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 행 열 정보 따로 받기 
        int n = sc.nextInt(); // 행
        int m = sc.nextInt(); // 열

        // 기둥이 특정 행과 열에 있는지 파악하기위한 배열 선언
        int[][] graph = new int[n][m];
        boolean[] rowAble = new boolean[n];
        boolean[] colAble = new boolean[m];

        
        // 기둥이 이미있으면 설치할 필요 없으므로 True 넣어줌
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                graph[i][j] = sc.nextInt();
                if (graph[i][j] == 0) {
                    rowAble[i] = true;
                    colAble[j] = true;
                }
            }
        }

        // 0이 없는 행과 열 개수 세기
        // 조사한 행과 열에 기둥이 없으면 세워야되니까 숫자 count
        int rowCount = 0;
        for (int i = 0; i < n; i++) {
            if (!rowAble[i]) rowCount++;
        }

        int colCount = 0;
        for (int j = 0; j < m; j++) {
            if (!colAble[j]) colCount++;
        }

        // 행과 열을 동시에 처리하는 최소한의 숫자이므로 행과 열 중에 큰값을 뽑아야
        System.out.println(Math.max(rowCount, colCount));
    }
}
