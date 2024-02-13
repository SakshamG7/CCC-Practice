package CCC2021.S2;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        final int M, N, K;
        M = input.nextInt();
        input.nextLine();
        N = input.nextInt();
        input.nextLine();
        K = input.nextInt();
        input.nextLine();

        int t = 0;
        boolean[][] cavas = new boolean[M][N];

        for (int i = 0; i < K; i++) {
            String[] uinput = input.nextLine().split(" ");
            int command = Integer.parseInt(uinput[1]) - 1;

            if (uinput[0].equals("C")) {
                for (int j = 0; j < M; j++) {
                    cavas[j][command] = !(cavas[j][command]);
                    if (cavas[j][command]) {
                        t ++;
                    } else {
                        t --;
                    }
                }
            } else {
                for (int j = 0; j < N; j++) {
                    cavas[command][j] = !(cavas[command][j]);
                    if (cavas[command][j]) {
                        t ++;
                    } else {
                        t --;
                    }
                }
            }
        }

        // for (int i = 0; i < M; i++) {
        //     for (int j = 0; j < N; j++) {
        //         if (cavas[i][j]) {
        //             t += 1;
        //         }
        //     }
        // }

        input.close();

        System.out.println(t);
    }
}
