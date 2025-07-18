import java.util.Scanner;

public class C6 {
    public static int sumar(int a, int b) {
        return a + b;
    }
    public static int restar(int a, int b) {
        return a - b;
    }
    public static int multiplicar(int a, int b) {
        return a * b;
    }

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.print("Ingresa el valor a: ");
        int a = entrada.nextInt();

        System.out.print("Ingresa el valor b: ");
        int b = entrada.nextInt();

        System.out.println("El resultado de la suma es " + sumar(a, b));
        System.out.println("El resultado de la resta es " + restar(a, b));
        System.out.println("El resultado de la multiplicaicon es " + multiplicar(a, b));

        entrada.close();
    }
}
