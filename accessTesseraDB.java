import java.sql.*;
public class accessTesseraDB {
    public static void main(String[] a)
        throws Exception {
            Class.forName("org.h2.Driver");
            Connection conn = DriverManager.getConnection("jdbc:h2:./target/h2/tessera1", "sa", "");
        // add application code here
        conn.close();
    }
}