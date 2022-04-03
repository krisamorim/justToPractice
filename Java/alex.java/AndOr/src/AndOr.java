
public class AndOr {

	public static void main(String[] args) {
		double payment = 100;
		int age = 18;
		
		if (payment>99.9 && age>17) {
			System.out.println("Entrada autorizada");
		}else{
			if (payment<99.9 && age<18) {
				System.out.println("Idade e dinheiro insuficientes");
			}else{
				if (payment<99.9) {
					System.out.println("Valor insuficiente");
				}else{
					System.out.println("Você não tem idade suficiente");
			}
		}

	}

}
}