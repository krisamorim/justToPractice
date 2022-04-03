
public class GlobalPrivado {

	/*Variavel global é acessivel a todos*/
	static int  maiorIdadeGlobal = 30;
	
	/*Main é um metodo autoexecutavel em java*/
	public static void main(String[] args) {
		
		/*Variavel local pois pertence somente a esse método e o valor fica dentro do metodo*/
		int maiorIdade = 18;
		System.out.println("Valor da variavél local = " + maiorIdade );
		
		metodo2();
	}
	
	public static void metodo2() {
		System.out.println("Valor da variável Global = " + maiorIdadeGlobal);
	}
	
}
