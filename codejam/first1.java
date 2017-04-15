import java.io.*;
public class first1{
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
			char[][] cake = new char[r][c];
			for(int j = 0; j<r;j++){
				String str = in.readLine();
			   for(int k=0; k<c;k++){
			   		cake[j][k]=	str.charAt(k);   
			   }
			}
            int n=0;
            /*for(int j=1;j<=d;j++){
                if(sum<j){
                    sum++;
                    n++;
                }
                sum=sum+parts[1].charAt(j)-'0';
            }*/
            out.printf("Case #%d:\n",i);
			for(int j=0;j<r;j++){
				for(int k=0;k<c;k++){
					out.print(cake[j][k]);
				}
				out.println();
			}
            out.flush();
        }
        in.close();
        out.close();
    }
    public static void main(String[] args)throws IOException{
        fun();
    }
}
            
        
