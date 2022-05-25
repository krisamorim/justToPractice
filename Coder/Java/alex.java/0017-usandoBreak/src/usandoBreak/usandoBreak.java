package usandoBreak;

public class usandoBreak {

	public static void main(String[] args) {

		for (int num=0; num <= 10; num++) {
			if (num == 3) {
				System.out.println("Encontrei o 3\nVou parar");
				break;
			}else {
				System.out.println(num);
			}
		}

	}

}
