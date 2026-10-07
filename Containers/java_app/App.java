import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class App {
    public static void main(String[] args) throws Exception {
        Thread.sleep(5000);
        // Подключаемся к базе данных
        String url = "jdbc:postgresql://db:5432/mydb";
        String user = "user";
        String password = "password";
        
        System.out.println("Подключаемся к базе данных...");
        
        try (Connection conn = DriverManager.getConnection(url, user, password)) {
            System.out.println("Успешно подключились!");
            
            // Создаём таблицу и вставляем данные
            Statement stmt = conn.createStatement();
            stmt.execute("CREATE TABLE IF NOT EXISTS java_data (id SERIAL PRIMARY KEY, message TEXT)");
            stmt.execute("INSERT INTO java_data (message) VALUES ('Привет из Java!')");
            
            System.out.println("Таблица создана и данные добавлены!");
        }
    }
}
