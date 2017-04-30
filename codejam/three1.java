import java.io.*;
public class three1{
    static String infile = "in.txt";
    static String outfile = "out.txt";
    public static void fun() throws IOException{
        BufferedReader in = new BufferedReader(new FileReader(infile));
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter(outfile,false)));
        int line = Integer.parseInt(in.readLine());
        for(int i=1;i<=line;i++){
            String[] parts = in.readLine().split(" ");
            int r = Integer.parseInt(parts[0]);
            int c = Integer.parseInt(parts[1]);
            int w = Integer.parseInt(parts[2]);
            int n=0;
            /*for(int j=1;j<=d;j++){
                if(sum<j){
                    sum++;
                    n++;
                }
                sum=sum+parts[1].charAt(j)-'0';
            }*/
            n = ((c/w)+w-1)*r;
            out.printf("Case #%d: %d",i,n);
            out.println();
            out.flush();
        }
        in.close();
        out.close();
    }
    public static void main(String[] args)throws IOException{
        fun();
    }
}
            
        
