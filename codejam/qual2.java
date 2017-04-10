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
				result[nn] = (int)str[nn]-48;
			}
			getParts(result,num);
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
	public static void getParts(int[] result, int num){
		if(num<=1) return;
			int max=result[0],j;
            for( j=1;j<num;j++){
				if(result[j]<max){
				   	break;
				}else{
					max = result[j];
				}
            }
			if(j<num){
			result[j-1]-=1;
			for(int k=j;k<num;k++){
				result[k]=9;
			}
			getParts(result, j);
			}
	}

    public static void main(String[] args)throws IOException{
        fun();
    }
}
            
        
