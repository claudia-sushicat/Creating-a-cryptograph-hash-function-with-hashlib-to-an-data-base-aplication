#  Learning about cryptographic hash functions with python !♥ 
* + - . + - * + - . - + * - + - . 

Use: Python3, Spyder, DBeaver -> SQLite.


In this repository, i'm learning to use  hashlib in python3 to create a hashed password(with salt) to be stored in db.


The ideal cryptographic hash function has the following main properties:

-   it is  deterministic, meaning that the same message always results in the same hash
-   it is quick to compute the hash value for any given message
-   it is infeasible to generate a message that yields a given hash value ( to reverse the process that generated the given hash value)
-   it is infeasible to find two different messages with the same hash value
-   a small change to a message should change the hash value so extensively that the new hash value appears uncorrelated with the old hash value.




## Hashlib...
* + - . + - * + - . - + * - + - . 

If you want to modify the type of algorithm in hash function
you can change the following parts:

def hash_password(password):
    salt = uuid.uuid4().hex
    return     **hashlib.**sha256(  
               salt.encode() + password.encode()).hexdigest() + ':' + salt
 
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == **hashlib.**sha256(salt.encode() + user_password.encode()).hexdigest()
              
*hashlib.    <- you can use:  sha1( ), sha224( ), sha256( ), sha384( ), sha512( ), md5( ) and more (you can read more about it here: https://www.journaldev.com/16035/python-hashlib


## About db .. 
* + - . + - * + - . - + * - + - . 

I set some max/min values for the lenghts of username and user_pass. You can change it by creating another table!


if len(username) < 6 or len(username) > 8 :
    username = input('Username min lenght = 6 max lenght = 8. Please, enter a valid username')
if len(user_pass) < 8 or len(user_pass) > 14:
    user_pass = input('Password min lenght = 8,max lenght = 14. Please, enter a valid password')
def validation_username(username):
    reader.execute("SELECT EXISTS (SELECT 1 FROM data_users where username =  '" + username + "')")
    return (reader.fetchone()[0] == 1)

## More links :0

* + - . + - * + - . - + * - + - . 

[Home — Spyder IDE (spyder-ide.org)](https://www.spyder-ide.org/)
[DBeaver Community | Free Universal Database Tool](https://dbeaver.io/)
[hashlib.sha3_256() in Python - GeeksforGeeks](https://www.geeksforgeeks.org/hashlib-sha3_256-in-python/)
[hashlib — Secure hashes and message digests — … (python.org)](https://docs.python.org/3/library/hashlib.html)