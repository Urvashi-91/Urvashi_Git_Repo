import java.util.Scanner;

public class HelloWorld {
    
    public static void main(String[] args) {
        Scanner name = new Scanner(System.in);

        Scanner name1 = new Scanner(System.in);
        String userName1;
        String userName2;
        userName1 = name.nextLine();
        userName2 = name1.nextLine();
        System.out.println("Hello, World" + userName1 + " " + userName2);
        System.out.println("GoodBye" + userName2 + "" + userName1);
    }
}
