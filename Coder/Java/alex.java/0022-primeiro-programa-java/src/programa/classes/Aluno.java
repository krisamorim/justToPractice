package programa.classes;

/*Clase/Objeto que representa aluno*/
public class Aluno {
	//Atributos:
	String nome;
	int idade;
	String dataNascimento;
	String registroGeral;
	String numeroCpf;
	String nomePai;
	String nomeMae;
	String dataMatricula;
	String nomeEscola;
	String serieMatriculado;
	
	public Aluno(String nomePadrao) {
		nome = nomePadrao;
	}
	
	public Aluno(String nomePadrao, int idadePadrao) {
		nome = nomePadrao;
		idade = idadePadrao;		
	}
}
