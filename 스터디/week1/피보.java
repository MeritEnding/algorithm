// 기본 피보나치 코드

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        
        Scanner scanner = new Scanner(System.in);

     
        int a = scanner.nextInt();
        int b = scanner.nextInt();

        List<Long> fibFib = new ArrayList<>();

       
        List<Long> fibs = new ArrayList<>();
        fibs.add(1L); 
        fibs.add(1L); 

        int index = 0; 


        while (fibFib.size() < b) {
            if (index >= fibs.size()) {
                long next = fibs.get(fibs.size() - 1) + fibs.get(fibs.size() - 2);
                fibs.add(next); 
            }
          
            long value = fibs.get(index);

            for (int i = 0; i < value; i++) {
                fibFib.add(value);

                if (fibFib.size() >= b) break;
            }

            index++;
        }

        long sum = 0;
        for (int i = a - 1; i < b; i++) {
            sum += fibFib.get(i);
        }
        System.out.println(sum);
    }
}
