public class FUNCIONES {
    // Funcion saludar que no retorna nada
    public static void saludar() {
        System.out.println("Hola mundo");
    }

    // Funcion sumar que retorna un resultado
    public static int sumar(int a, int b) {
        int resultado = a + b;
        return resultado;
    }

    // Llamamos a Main para ejecutar las funciones 
    public static void main(String[] args) {
        saludar(); // llamamos a la funcion saludar

        int suma = sumar(5,3);
        System.out.println("La suma es de " + suma);

    }
}
