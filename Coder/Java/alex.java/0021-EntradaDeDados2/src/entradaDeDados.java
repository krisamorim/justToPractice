import javax.swing.JOptionPane;

public class entradaDeDados {

	public static void main(String[] args) {
		String carros = JOptionPane.showInputDialog("Informe a quantidade de carros");
		String pessoas = JOptionPane.showInputDialog("Informe a quantidade de pessoas");
		
		double carroQntde = Double.parseDouble(carros);
		double pessoaQntde = Double.parseDouble(pessoas);
		
		int divide = (int) (carroQntde/pessoaQntde);
		
		double resto = carroQntde % pessoaQntde;
		
		JOptionPane.showMessageDialog(null, "Divisão p/ pessoas deu " + divide + " carros e sobram " + resto);
	}

}
