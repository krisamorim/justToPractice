
public class ternário {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		
		double nota1 = 2;
		double nota2 = 4;
		double nota3 = 2;
		double nota4 = 6;
		double media = (nota1+nota2+nota3+nota4)/4;
		/*
		if (media > 7) {
			System.out.println("Aprovado direto");
		}else{
			System.out.println("Reprovado");
		}
		*/
		/*Somente um ternário*/
		String resultadoFinal = media>=7 ? "Aprovado" : "Reprovado";
		
		/*ternário dentro de outro ternário
		String resultadoFinal = media>=7 ? "Aprovado" : media>4 && media<7 ? "Em recuperação" : "Reprovado";
		*/
		System.out.println(resultadoFinal);
		
	}

}
