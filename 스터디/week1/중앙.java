// 정렬+ 중앙값 문제
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 입력받기
        String[] input = sc.nextLine().split(" ");
        int[] arr = new int[input.length];
      
        for (int i = 0; i < input.length; i++) {
            arr[i] = Integer.parseInt(input[i]);
        }

        //오름차순 정렬
        Arrays.sort(arr);

        // 인덱스 중앙값 찾기
        int idx = arr.length / 2;

        // 중앙값 출
        System.out.println(arr[idx]);
    }
}
