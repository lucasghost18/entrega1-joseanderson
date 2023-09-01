package Aula;

import java.io.IOException;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import java.io.FileWriter;

public class Main {

    public static void main(String[] args) {
        try {
            Document doc = Jsoup.connect("https://pt.wikipedia.org/wiki/Napole%C3%A3o_Bonaparte").get();
            String pageTitle = doc.title();

            FileWriter writer = new FileWriter("arquivo.txt");
            writer.write(pageTitle); 
            writer.close();
            
            System.out.println("Dados gravados com sucesso!");

        } catch (IOException e) {
            System.err.println("Erro ao escrever no arquivo: " + e.getMessage());
        }
    }
}
