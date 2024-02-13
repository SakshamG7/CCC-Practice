package CCC2021.S1;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        double t = 0;
        input.nextLine();

        String[] hS = input.nextLine().split(" ");
        String[] bS = input.nextLine().split(" ");

        input.close();
        for (int i = 0; i < n; i++) {
            t += Double.parseDouble(bS[i]) * (Double.parseDouble(hS[i]) + Double.parseDouble(hS[i + 1]));
        }

        t /= 2.0;

        System.out.println(t);
        
    }
}
