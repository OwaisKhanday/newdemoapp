import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import json
import streamlit as st

import config
import pdb

def main():
    
    st.title('HackAndHack')
    
    login_pannel, registration_pannel = st.columns(2)
    
    with login_pannel:
        username  = st.text_input("User Name")
        password  = st.text_input("Password")

        if st.button("Login"):
            response = get_username_passwords_file(username, password)
            if response == 0:
                st.write(" No username ")

            else:
                st.write("OK")
                
    with registration_pannel:
        
        username  = st.text_input("Enter User Name")
        password  = st.text_input("Enter Password")
                
        if st.button("Register"):
            response = registration(username, password)
            if response == 0:
                st.write(" Username already present ")

            else:
                st.write("Registration sucessfull")
                
                
                
def get_username_passwords_file(username, password):
    
    crediantials = open(config.CRED_FILE)
    users = json.load(crediantials)
    
    users =  users["users"]
    #pdb.set_trace()
    flag = 0
    for user in users:
        if user["username"] == username and user["passwd"] == password:
            flag = 1
            break
        
    if flag == 0:
            print(" username , password not found")
            user = 0

    return user

        
        
def registration(username, password):
    
    
    crediantials = open(config.CRED_FILE)
    users = json.load(crediantials)
    
    users =  users["users"]
    #pdb.set_trace()
    flag = 0
    for user in users:
        if user["username"] == username and user["passwd"] == password:
            flag = 1
            return 0
            
        
    if flag == 0:
       
        crediantials = open(config.CRED_FILE)
        users = json.load(crediantials)
        data = {"username":username, "passwd": password}
        old = users["users"]
        old.append(data)
        users = {"users": old}
        json_string = json.dumps(users)
        
        with open(config.CRED_FILE, 'w') as outfile:
            outfile.write(json_string)
        
        return 1
        
        
main()