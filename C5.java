public class C5 {
    public static int procesarNumero(int n) {
        if (n % 2 == 0){
            return n * 2;
        } else {
            return n * 3;
        }
    }
    public static void main(String[] args) {
        int resultado = procesarNumero(4);
        System.out.println("El resultado es: " + resultado);
    }
}
