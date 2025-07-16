public class conversion {
    public static void main(String[] args) {
        // conversion implicita
        byte a = 1;
        double b = 15.15;
        double c = a+b;
        System.out.println(c);

        // conversion explicita
        int x = 15;
        double y= 15.015;
        int z = (int) (x+y);
        System.out.println(z);

        // Conversion String a num
        int e = 5;
        String s = "1.1";
        double resultado = e + Double.parseDouble(s);
        System.out.println(resultado);
    }
    
}
