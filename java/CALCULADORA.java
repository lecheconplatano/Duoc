public class CALCULADORA {
    public static int sumar(int a, int b) {
        int resultado = a + b;
        return resultado;
    }
    public static int restar(int a, int b) {
        int resultado = a - b;
        return resultado;
    }
    public static int multiplicar(int a, int b) {
        int resultado = a * b;
        return resultado;
    }
    public static int dividir(int a, int b) {
        int resultado = a / b;
        return resultado;
    }
    public static void main(String[] args) {
        int a = 6;
        int b = 6;

        int suma = sumar(a, b);
        int resta = restar(a, b);
        int multiplicacion = multiplicar(a, b);
        int division = dividir(a, b);

        // resultados
        System.out.println("Suma " + suma);
        System.out.println("Resta = " + resta);
        System.out.println("Multiplicacion " + multiplicacion);
        System.out.println("Division " + division);
    }
}
