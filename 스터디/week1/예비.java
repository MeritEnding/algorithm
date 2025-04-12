// 구현 문제

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 입력 받기
        int year = sc.nextInt();
        String kind = sc.next();
        String dong = sc.next();
        String sin = sc.next();

        int temp = 0;
        // 일단 20고개처럼 가장 크게 분류할 수 있는 기준을 정하고 겹치는 거는 수식에 추가 하지않고 구현
        if (sin.equals("Private")) {
            if (year == 0) {
                temp = 0;
            } else if (1 <= year && year <= 4 && dong.equals("N") &&
                       (kind.equals("ROKA") || kind.equals("ROKN"))) {
                temp = 32;
            } else if (1 <= year && year <= 4 &&
                       (dong.equals("Y") || (dong.equals("N") && kind.equals("ROKAF")))) {
                temp = 28;
            } else {
                temp = 20;
            }
        } else {
            if (year == 0) {
                temp = 0;
            } else if (1 <= year && year <= 6 && dong.equals("N")) {
                temp = 28;
            } else {
                temp = 28;
            }
        }

        System.out.println(temp);
    }
}
