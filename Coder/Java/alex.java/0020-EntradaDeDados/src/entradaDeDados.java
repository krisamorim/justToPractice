import javax.swing.JOptionPane;

public class entradaDeDados {

	public static void main(String[] args) {
		String name = JOptionPane.showInputDialog("Qual seu nome");
		while (name == null || name == "") {
			name = JOptionPane.showInputDialog("Favor fornecer um valor válido\nQual seu nome");
		}
		System.out.println("Olá "+name);
	}

}
