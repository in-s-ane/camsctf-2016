palindrome :: Integer -> Bool
palindrome x = reversal x == x

reversal :: Integral a => a -> a
reversal = go 0
  where go a 0 = a
        go a b = let (q,r) = b `quotRem` 10 in go (a*10 + r) q
-- the above taken from https://stackoverflow.com/questions/26315917/decidein-haskell-if-a-number-is-or-not-a-palindrome-without-using-lists

divisible x = x `mod` 16384 == 0

findSum = sum [x | x<-[1000013824,1000030208..9999999999], palindrome x]

main = do
  putStrLn $ show findSum

{19473563648}
