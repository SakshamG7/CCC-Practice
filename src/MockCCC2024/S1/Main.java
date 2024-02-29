package MockCCC2024.S1;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        int N = in.nextInt(), K = in.nextInt();
        in.nextLine();
        String[] numsS = in.nextLine().split("");

        in.close();

        while (true) {
            int s = Integer.MAX_VALUE;
            boolean temp = false;
            for (int i = 0; i < N; i++) {
                if (numsS[i].equals("1")) {
                    if (!temp) {
                        temp = true;
                    } else {
                        if (numsS[i].equals("0") && ) {
                            s++;
                        } else {
                            s = 0;
                        }
                    }
                }
            }
        }

    }
}
