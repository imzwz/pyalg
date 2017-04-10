import java.io.*;
import java.util.*;
public class qual3{
    static String infile = "in.txt";
    static String outfile = "out.txt";
    public static void fun() throws IOException{
        BufferedReader in = new BufferedReader(new FileReader(infile));
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter(outfile,false)));
        int line = Integer.parseInt(in.readLine());
        for(int i=1;i<=line;i++){
            String[] parts = in.readLine().split(" ");
            int cap = Integer.parseInt(parts[0]);
            int num = Integer.parseInt(parts[1]);
            int[] n;
			n = attempt(cap, num);
            out.printf("Case #%d: %d %d",i,n[0],n[1]);
            out.println();
            out.flush();
        }
        in.close();
        out.close();
    }

    public static int[] attempt(int cap, int num) {
        int[] ret = {cap, cap};

        ArrayList<Integer> bucket = new ArrayList<>();
        bucket.add(cap);
        int currentHighest = -1;

        while (num > 0) {
            //System.out.println("begin iteration");
            currentHighest = Collections.max(bucket);
            bucket.remove(new Integer(currentHighest));
            bucket.add(getSmall(currentHighest));
            bucket.add(getLarge(currentHighest));

            ret[0] = getLarge(currentHighest);
            ret[1] = getSmall(currentHighest);

            System.out.println("iteration # " + num);
            num--;
        }
        return ret;
    }

    public static int getSmall(int input) {
        if (input <= 1) return 0;
        return ((input & 1) == 0) ? (input / 2) - 1 : (input - 1) / 2;
    }

    public static int getLarge(int input) {
        if (input <= 1) return 0;
        return ((input & 1) == 0) ? (input / 2) : (input - 1) / 2;
    }
    public static void main(String[] args)throws IOException{
        fun();
    }
}
            
        
