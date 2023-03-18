package programa.classes;

/*Clase/Objeto que representa aluno*/
public class Aluno {
	//Atributos:
	public String nome;//colocando public pois dessa vez esta em pacotes diferentes
	int idade;
	String dataNascimento;
	String registroGeral;
	String numeroCpf;
	String nomePai;
	String nomeMae;
	String dataMatricula;
	String nomeEscola;
	String serieMatriculado;
	
	//criando o construtor aluno sem parâmetro para poder instanciar o objeto sem colocar valor e depois poder definir os valores direto pelo atributo
	public Aluno() {
	
	}
	
	public Aluno(String nomePadrao) {
		nome = nomePadrao;
	}
	
	public Aluno(String nomePadrao, int idadePadrao) {
		nome = nomePadrao;
		idade = idadePadrao;		
	}
}
