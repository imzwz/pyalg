import java.io.*;
public class qual1{
    static String infile = "in.txt";
    static String outfile = "out.txt";
    public static void fun() throws IOException{
        BufferedReader in = new BufferedReader(new FileReader(infile));
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter(outfile,false)));
        int line = Integer.parseInt(in.readLine());
        for(int i=1;i<=line;i++){
            String[] parts = in.readLine().split(" ");
            byte[] str = parts[0].getBytes();
            int k = Integer.parseInt(parts[1]);
            int n=0, j;
			for(j=0; j<str.length; j++){
				if(str[j]=='-'){
					if(j > str.length-k){
						n = -1;
						break;
					}else{
					exchange(str, j, k);
					n++;
					}
				}
			}

            /*for(int j=1;j<=d;j++){
                if(sum<j){
                    sum++;
                    n++;
                }
                sum=sum+parts[1].charAt(j)-'0';
            }*/
			if(n>=0){
            	out.printf("Case #%d: %d",i,n);
			}else{
				out.printf("Case #%d: IMPOSSIBLE",i);
			}
            out.println();
            out.flush();
        }
        in.close();
        out.close();
    }
	public static void exchange(byte[] str, int start, int k){
	   for(int i = start; i < start+k ;i++){
	   		if(str[i]=='+'){ str[i]='-'; }
			else {str[i]='+' ;}		
	   }
	}
    public static void main(String[] args)throws IOException{
        fun();
    }
}
            
        
