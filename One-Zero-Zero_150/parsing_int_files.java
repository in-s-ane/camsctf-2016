import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.Path;
import java.math.BigInteger;
import java.io.IOException;
import java.util.Arrays;

public class parsing_int_files {
    public static void main(String[] args) throws IOException {
        Path path = Paths.get(args[0]);
        byte[] data = Files.readAllBytes(path);
        BigInteger num = new BigInteger(data);
        System.out.println(num);
    }
}
