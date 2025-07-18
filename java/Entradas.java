import java.util.Scanner;

public class Entradas {
    public static void main(String[] args) {
        int entradas = 100;
        Scanner input = new Scanner(System.in);
        
        while (true) {
        System.out.println("***** Cine Estrella *****");
        System.out.println("Bienvenido al sistema de Cine Estrella");
        System.out.println("1. Ver cuántas entradas quedan.");
        System.out.println("2. Comprar una cantidad de entradas.");
        System.out.println("3. Devolver entradas.");
        System.out.println("4. Salir del sistema.");
        System.out.print("Ingrese alguna opcion: ");
        int opc = input.nextInt();

        if (opc == 1) {
            System.out.println("La cantidad de entradas es " + entradas);
        }
        else if (opc == 2) {
            System.out.print("Ingrese la cantidad de entradas que desea comprar: ");
            int cantidad = input.nextInt();
            entradas = entradas - cantidad;
        }
        else if (opc == 3) {
            System.out.print("Ingrese la cantidad de entradas que desea devolver: ");
            int devolver = input.nextInt();
            entradas = entradas + devolver;
        }
        else if (opc == 4) {
            System.out.println("Gracias por preferirnos");
            break;
        }
        else {
            System.out.println("Opcion ingresada incorrecta");
        }
        }
    } 
}
