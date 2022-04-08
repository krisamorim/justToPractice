
public class CondicionalIfElse {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		double nota1 = 7;
		double nota2 = 7;
		double nota3 = 7;
		double nota4 = 6;
		double media = (nota1+nota2+nota3+nota4)/4;
		
		if (media > 7) {
			System.out.println("Aprovado direto");
		}else{
			System.out.println("Reprovado");
		}
	}

}
