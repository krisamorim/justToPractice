
public class logicaAninhada {

	public static void main(String[] args) {
		int n1 = 70;
		int n2 = 60;
		int n3 = 50;
		int n4 = 50;
		int media = 0;
		media = (n1+n2+n3+n4)/4;
		
		if (media >= 50) {
			if (media >= 70) {
				System.out.println("A media � " + media);
				System.out.println("Aluno est� aprovado direto");
			}else{
				System.out.println("A m�dia � " + media);
				System.out.println("Aluno est� em recupera��o");
			}
		}else{
			System.out.println("Aluno reprovado direto");
		}
	}
}
