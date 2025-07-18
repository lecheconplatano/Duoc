import java.util.Scanner;

public class menu {
    public static void main(String[] args) {
        while (true) {
            Scanner entrada = new Scanner(System.in);

            System.out.println("=== MENU DE OPCIONES ===");
            System.out.println("========================");
            System.out.println("1. Salir del programa ");
            System.out.println("2. Hola mundo ");
            System.out.print("Ingrese alguna opcion: ");
            
            try {int opc = entrada.nextInt();
                if (opc == 1) {
                    break;}
                else if (opc == 2) {
                    System.out.println("Hola mundo");
                }
            } catch (Exception e) {
                System.out.println("Ha surgido un error, ingrese un valor entero ");
                entrada.nextLine(); }
        }
    }
}
        