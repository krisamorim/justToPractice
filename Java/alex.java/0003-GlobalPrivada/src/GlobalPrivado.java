
public class GlobalPrivado {

	/*Variavel global � acessivel a todos*/
	static int  maiorIdadeGlobal = 30;
	
	/*Main � um metodo autoexecutavel em java*/
	public static void main(String[] args) {
		
		/*Variavel local pois pertence somente a esse m�todo e o valor fica dentro do metodo*/
		int maiorIdade = 18;
		System.out.println("Valor da variav�l local = " + maiorIdade );
		
		metodo2();
	}
	
	public static void metodo2() {
		System.out.println("Valor da vari�vel Global = " + maiorIdadeGlobal);
	}
	
}
