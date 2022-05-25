public class switchCase {

	public static void main(String[] args) {
		int n1=90, n2=10, n3=50, n4=90;
		int media = (n1+n2+n3+n4)/4;
		
		switch(media) {
		case 70:
			System.out.println("Aprovado");
			break;
			
			default:
				System.out.println("Outro valor " + media);
				break;
		}
	}

}
