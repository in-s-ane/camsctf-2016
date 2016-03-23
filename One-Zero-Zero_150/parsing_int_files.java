import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.Path;
import java.math.BigInteger;
import java.io.IOException;
import java.util.Arrays;

public class parsing_int_files {
    public static byte[] concat(byte[] a, byte[] b) {
        int aLen = a.length;
        int bLen = b.length;
        byte[] c= new byte[aLen+bLen];
        System.arraycopy(a, 0, c, 0, aLen);
        System.arraycopy(b, 0, c, aLen, bLen);
        return c;
    }

    public static void main(String[] args) throws IOException {
        byte[] data = new byte[0];

        for (int i = 1 ; i < 17 ; i++) {
            Path path = Paths.get(i + ".enc");
            byte[] curr = Files.readAllBytes(path);
            BigInteger num = new BigInteger(1, curr);
            System.out.println(num);
            //data = concat(data, curr);
        }

        //BigInteger num = new BigInteger(data);
        //System.out.println(num);
    }
}
