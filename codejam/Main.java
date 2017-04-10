import java.io.*;
public class Main{
	public static int getResult(int num){
		if(num%2==1) return 1;

	}

    public static void main(String[] args)throws IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		String str = in.readLine();
        in.close();
		int n = Integer.parseInt(str);
		int result = getResult(n);	
		System.out.println(result);
    }
}
            
        
