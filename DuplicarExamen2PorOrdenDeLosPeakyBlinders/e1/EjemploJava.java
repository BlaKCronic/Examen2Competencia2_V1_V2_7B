import java.util.Scanner;

public class EjemploJava {
    private int edad;
    private String nombre;
    private boolean activo;
    private int[] numeros;

    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        System.out.println("Hola");
        int x = 10;
        double precio = 12.5;
        String texto = "Hola";
        Boolean estado = true;
        int[] valores = {1, 2, 3};

        for (int i = 0; i < 3; i++) {
            System.out.println(i);
        }

        while (x > 0) {
            x--;
        }

        do {
            x++;
        } while (x < 5);

        EjemploJava obj = new EjemploJava();
        obj.setNombre("Ana");
        System.out.println(obj.getNombre());
    }

    public int getEdad() { return edad; }
    public void setEdad(int edad) { this.edad = edad; }
    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }
    public boolean isActivo() { return activo; }
    public void setActivo(boolean activo) { this.activo = activo; }
}
