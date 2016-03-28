import java.nio.file.Files;
import java.nio.file.Paths;

public class Solution {
    public static void main(String[] args) throws Exception {
        String data = new String(Files.readAllBytes(Paths.get("leet.txt"))).trim();
        String decompressed = LZString.decompressHexString(new String(data));
        System.out.println(decompressed.replace("flag", "")); // Flag format...
    }
}

// LeetZ sounds a lot like LZ, especially with the L and Z being capitalized.
// Clearly, we need to decompress the hex given to us as LZ compressed data.

// Looking online, I found this nice implementation of the algorithm in Java: //https://github.com/diogoduailibe/lzstring4j

// If we decompress the hex using the LZString class, we get the flag:
// {lz1zl2c0mpr355m3b4by}
