# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 21:06:56 2020

@author: 55219
"""
"""
tentando estudar sobre função hash, algoritmos (sha256)
e conexão com db.

"""
import hashlib
import sqlite3
import uuid


conect = sqlite3.connect('data.db')
reader = conect.cursor()
 

def register_database(username,hashed_password,salt):
    reader.execute("INSERT INTO data_users (username,hashed_password,salt) VALUES(?,?,?)",(username,hashed_password,salt))
    conect.commit()

def hash_password(password):
    salt = uuid.uuid4().hex
    return     hashlib.sha256(
               salt.encode() + password.encode()).hexdigest() + ':' + salt

def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

def get_hashedpassword(username):
    return reader.execute("SELECT hashed_password,salt FROM data_users where username =  '" + username + "'").fetchall()[0]


def register(username,user_pass):
    if  validation_username(username):
        print('usuário já existe') 
        return False
    hashed_password = hash_password(user_pass)
    register_database(username,hashed_password.split(':')[0],hashed_password.split(':')[1])
    
def login(username,user_pass):
    data_password = get_hashedpassword(username)
    print(data_password)
    print(check_password(data_password[0]+":"+data_password[1],user_pass))

username = input('Please enter a username:')
user_pass = input('Please enter a password: ') 

if len(username) < 6 or len(username) > 8 :
    username = input('Username min lenght = 6 max lenght = 8. Please, enter a valid username')
if len(user_pass) < 8 or len(user_pass) > 14:
    user_pass = input('Password min lenght = 8,max lenght = 14. Please, enter a valid password')
def validation_username(username):
    reader.execute("SELECT EXISTS (SELECT 1 FROM data_users where username =  '" + username + "')")
    return (reader.fetchone()[0] == 1)

 
choice = input('Register or login')

if choice == "register":
    register(username,user_pass)
else:
    login(username,user_pass)
    
