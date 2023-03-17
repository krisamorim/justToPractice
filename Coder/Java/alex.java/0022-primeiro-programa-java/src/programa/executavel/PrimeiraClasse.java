package programa.executavel;

import programa.classes.Aluno;

public class PrimeiraClasse {
	
	public static void main(String[] args) {
		
		/* Se o objeto estiver declarado como mostrado abaixo ele não existe na memória*/
		Aluno aluno1;
		
		/*Ja se o objeto for declarado com o new, ele parra a existir na memória*/
		Aluno aluno2 = new Aluno();
	}
}
