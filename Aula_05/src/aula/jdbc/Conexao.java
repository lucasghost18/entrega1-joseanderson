package aula.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Conexao {

 public static void main(String[] args){
	 String driver = "org.postgresql.Driver";
	 String user = "postgres";
	 String senha = "postgres";
	 String url = "jdbc:postgresql://localhost:5432/jdbc";

	 try{
		 Class.forName(driver);
		 Connection con = null;

		 con = (Connection) DriverManager.getConnection(url, user, senha);

		 System.out.println("Conexão realizada com sucesso.");

	 }
	 catch (ClassNotFoundException ex){
		 System.err.print(ex.getMessage());
	 }
	 catch (SQLException e){
		 System.err.print(e.getMessage());
	 }
 	}
}