import java.io.*;
public class tou1{
    static String infile = "in.txt";
    static String outfile = "out.txt";
    public static void fun() throws IOException{
        BufferedReader in = new BufferedReader(new FileReader(infile));
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter(outfile,false)));
        String[] parts = in.readLine().split(" ");
        int n = Integer.parseInt(parts[0]);
        int k = Integer.parseInt(parts[1]);
        //out.printf("Case #%d: %d",i,n);
		for(int i=0; i<n; i++){
			
        out.println();
        out.flush();
        in.close();
        out.close();
    }
    public static void main(String[] args)throws IOException{
        fun();
    }
}
            
        
