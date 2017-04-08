import java.io.*;
public class qual2{
    static String infile = "in2.txt";
    static String outfile = "out2.txt";
    public static void fun() throws IOException{
        BufferedReader in = new BufferedReader(new FileReader(infile));
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter(outfile,false)));
        int line = Integer.parseInt(in.readLine());
        for(int i=1;i<=line;i++){
            String[] parts = in.readLine().split(" ");
			byte[] str = parts[0].getBytes();
			int num = str.length;
			int[] result = new int[num];
			for(int nn=0; nn<num; nn++){
				result[nn] = str[nn] & 0xFF;
				//result[nn] = Integer.parseInt(str[nn]);
			}
			int a = result[0],min,j;
			boolean flag=true;
			min = result[0];
            for( j=0;j<num;j++){
				if(result[j]<min){
				   	break;
				}else{
					result[j]=min;
				}
            }
			/*if(flag==false){
				result[0] = a-1;
				for(int m=1; m < num;m++){
					result[m] = 9;
				}
			}*/
			String n ="";
			if(result[0]==0){
				for(int m=1; m < num; m++){
					n = n+result[m]+"";
				}
			}else{
				for(int m=0; m < num; m++){
					n = n+result[m]+"";
				}
			}
            out.printf("Case #%d: %s",i,n);
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
            
        
