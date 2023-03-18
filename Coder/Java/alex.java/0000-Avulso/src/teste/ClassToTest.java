package teste;

public class ClassToTest {
	public static void main(String[] args) {
		
		AlunoTeste aluno1 = new AlunoTeste("Kris", 38);
		AlunoTeste aluno2 = new AlunoTeste();
		aluno2.nome = "Ana";
		
		System.out.println(aluno1.nome);
		System.out.println(aluno2.nome);
	}
}
