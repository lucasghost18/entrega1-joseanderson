package package_01;

import java.io.FileWriter;
import java.io.IOException;

public class PersistenciaCSV {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String conteudo ="Exemplo,de,arquivo.csv";
		
		try {
			FileWriter escritor = new FileWriter("arquivo.csv");
			escritor.write("Teste1 ; teste2; teste3");
			escritor.close();
			System.out.println("Dados gravados com sucesso!");
			
		}catch (IOException e){
			System.err.println("Erro ao escrever no arquivo: " + e.getMessage());
		}

	}
}
