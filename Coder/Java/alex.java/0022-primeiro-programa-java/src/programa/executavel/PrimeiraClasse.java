package programa.executavel;

import programa.classes.Aluno;

public class PrimeiraClasse {
	
	public static void main(String[] args) {
		

		Aluno aluno1 = new Aluno();/*Aqui ser� o Jo�o*/
		
		/*Ja se o objeto for declarado com o new, ele parra a existir na mem�ria*/
		Aluno aluno2 = new Aluno();/*Aqui ser� o Pedro*/
		
		Aluno aluno3 = new Aluno("Maria");//utilizando o contrutor nomePadrao
		
		Aluno aluno4 = new Aluno("Pedro", 30);//utilizando o construtor nomePadrao e idadePadrao
		
		Aluno aluno5 = new Aluno();
		aluno5.nome = "Ana";
		System.out.println(aluno5.nome);
		
		Aluno aluno6 = new Aluno();
		aluno5.nome = "kris";
		aluno5.idade = 38;
		System.out.println("O nome do aluno5 � " + aluno5.nome + "\nA idade do aluno5 � " + aluno5.idade);
	}
}
