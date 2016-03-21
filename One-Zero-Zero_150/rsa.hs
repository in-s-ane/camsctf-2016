import Data.Char (ord, chr)

-- | Extended Euclidean Algorithm: egcd a b => (g, x, y) means g = ax + by in
-- lowest forms. Hopefully g == 1 (which implies x, y are coprime)
egcd :: Int -> Int -> (Int, Int, Int)
egcd 0 b = (b, 0, 1)
egcd a b = let (g, y, x) = egcd (b `mod` a) a in (g, x - ((b `div` a) * y), y)

-- Finds the inverse of the first argument mod the second argument
modinv :: Int -> Int -> Int
modinv a m
    | g == 1    = x `mod` m
    | otherwise = error "Modular inverse does not exist"
    where (g, x, y) = egcd a m

-- Converts an ascii string into a decimal number
ascii2Decimal :: [Char] -> Int
ascii2Decimal x = ascii2DecimalH x (length x - 1)

-- second int is length, of the string, used to keep track of length of string - 1 to increase efficiency
ascii2DecimalH :: [Char] -> Int -> Int
ascii2DecimalH x 0 = ord (head x)
ascii2DecimalH (x:xs) n = ord x * (16 ^ (2 * n)) + ascii2DecimalH xs (n - 1)


-- Converts a decimal number into an ascii string
decimal2Ascii :: Int -> [Char]
decimal2Ascii n = reverse (decimal2AsciiH n)

decimal2AsciiH :: Int -> [Char]
decimal2AsciiH num
    | num <= 256    = [chr num]
    | otherwise     = chr (num `mod` 256) : decimal2AsciiH (num `div` 256)

-- Encrypts the message (m) with the public key (e, n)
rsaEncrypt :: Int -> Int -> Int -> Int
rsaEncrypt m e n = (m ^ e) `mod` n

-- Decrypts a ciphertext (c) with the private key (d) and the modules n
rsaDecrypt :: Int -> Int -> Int -> Int
rsaDecrypt c d n = (c ^ d) `mod` n

main = do
    let n = 1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139
        e = 65537
        d = 27856072577004096911396713846850363584417408026591016459417310603194644749492416868137791178719126
        currdecrypt c = rsaDecrypt c d n
     in do
         print $ rsaEncrypt (currdecrypt 202915876039746229935722670340487424839857163073658749653272992778826868242273898753310832920993983342) e n
         print $ currdecrypt 202915876039746229935722670340487424839857163073658749653272992778826868242273898753310832920993983342
         print $ currdecrypt 51961498721312088747682686810774742575925154117134413172365649620137208443557184957215829783811743351
         print $ currdecrypt 174180660365459127238753784323442856289524431220970862233124660326683702250952471478404325530921566
         print $ currdecrypt 1202101822408726901750588940528514535773779125703308722028892739852969613685311641582744607797003524
         print $ currdecrypt 268297007571149029428662783098234966825433646219989860782317988234103568921230995288359347354137431
         print $ currdecrypt 209529425972976385621623708207640953656309283633577791673607533451097645212423462654729815094649043154
         print $ currdecrypt 223644394981822094186836837161683879992583985372909017547311952725552787427936479228279459352635176
         print $ currdecrypt 1405234147592221915074567515008046873832549700042148899390724476483743089316201554140113221971290838
