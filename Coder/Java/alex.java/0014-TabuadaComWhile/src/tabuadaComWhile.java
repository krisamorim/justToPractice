
public class tabuadaComWhile {

	public static void main(String[] args) {
		int tabuada=9, incremento=1;
		
		while (incremento <= 10) {
			int mult = tabuada*incremento;
			
			//if p/ verificar se o resultado � de um digito somente, se sim acrescenta o 0 na frente
			if (incremento < 10) {
				System.out.println(tabuada + "x" + "0" + incremento + "= " + mult);
				incremento ++;
			}else {
				System.out.println(tabuada + "x" + incremento + "= " + mult);
				incremento ++;
			}
			
		}
	}

}
