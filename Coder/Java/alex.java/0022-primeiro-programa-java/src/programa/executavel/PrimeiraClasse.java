package programa.executavel;

import programa.classes.Aluno;

public class PrimeiraClasse {
	
	public static void main(String[] args) {
		

		Aluno aluno1 = new Aluno();/*Aqui ser� o Jo�o*/
		
		/*Ja se o objeto for declarado com o new, ele parra a existir na mem�ria*/
		Aluno aluno2 = new Aluno();/*Aqui ser� o Pedro*/
		
		Aluno aluno3 = new Aluno("Maria");//utilizando o contrutor nomePadrao
		
		Aluno aluno4 = new Aluno("Pedro", 30);//utilizando o construtor nomePadrao e idadePadrao
	}
}
