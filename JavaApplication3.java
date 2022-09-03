package javaapplication3;

public class JavaApplication3 {

    public static int Fib(int n){
        if(n==1|| n==0) return 1;
        else return Fib(n-1) + Fib(n-2);
    }
    public static void main(String[] args) {
        System.out.println(Fib(5));
    }
    
}
