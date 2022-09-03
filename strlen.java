import java.util.*;
import java.lang.*;
import java.io.*;


public class strlen{
	public static int Len(String s){
		if(s.equals("")) return 0;
		else return 1 + Len(s.substring(1));
	}
	public static void main(String[] args) {
		String s = "ABCDEFG";
		System.out.println(Len(s));
	}
}