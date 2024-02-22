from flask import Flask, render_template, request, redirect
import hashlib
import re
from parse_old import parsing 

def username_regex(username):
    username_regex = "[a-zA-Z0-9_\-\.]\w{6,15}[\S]+"
    match_regex = re.search(username_regex, username)
    if match_regex:
        return True
    else:
        return False
    
def password_regex(password):
    password_regex = "^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@?#$%^&*+=]).{8}$"
    match_regex = re.search(password_regex, password)
    if match_regex:
        return True
    else:
        return False
    
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    return render_template('homepage.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get the form data
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        if username_regex(username) == True and password_regex(password) == True:
            if confirm_password == password:
                with open('user_credentials.txt','a') as user_data:
                    hashed_username = hashlib.sha256(username.encode()).hexdigest()
                    hashed_password = hashlib.sha256(password.encode()).hexdigest()
                    user_data.write(f'{hashed_username},{hashed_password}' + "\n")
                return redirect('/mainpage')  # Redirect to the main page after signup
            else:
                return "Passwords doesn't match!"
        elif username_regex(username) == True and password_regex(password) == False:
            return "Password should of length 8 and should contain atleast one UPPERCASE character, one lowercase characte, one digit and one special character."
        elif username_regex(username) == False and password_regex(password) == True:
            return "Username can be alphanumeric and should of length 6 to 15. It can contain characters '_', '-' and '.' but cannot have whitespaces."
        elif username_regex(username) == False and password_regex(password) == False:
            return "Username can be alphanumeric and should of length 6 to 15. It can contain characters '_', '-' and '.' but cannot have whitespaces.\nPassword should of length 8 and should contain atleast one UPPERCASE character, one lowercase characte, one digit and one special character."
    else:
        # Render the signup form template for GET request
        return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the form data
        entered_username = request.form['username']
        entered_password = request.form['password']

        hashed_entered_username = hashlib.sha256(entered_username.encode()).hexdigest()
        hashed_entered_password = hashlib.sha256(entered_password.encode()).hexdigest() 

        with open('user_credentials.txt','r') as user_data:
            user_credentials = user_data.readlines()
        print(user_credentials)
        for i in user_credentials:
            lst = i.split(',')
            print(lst)
            print(type(lst))
            if lst[0] == hashed_entered_username and lst[1] == hashed_entered_password + '\n':
                return redirect('/mainpage')
            elif lst[0] != hashed_entered_username and lst[1] == hashed_entered_password + '\n':
                return 'Incorrect username!'
            elif lst[0] == hashed_entered_username and lst[1] != hashed_entered_password + '\n':
                return 'Incorrect password!'
        return "Looks like you're a new user, please signup first!"
    else:
        # Render the login form template for GET request
        return render_template('login.html')

@app.route('/mainpage', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        query = request.form['query']  # Get the user's query from the form
        ans = parsing(query)
        if not ans:
            ans = "Sorry! We don't have an answer to your question"
            return render_template('mainpage.html', query=query, answer=ans)
        else:
            ans_str = " ".join(ans)
            return render_template('mainpage.html', query=query, answer=ans_str)
    return render_template('mainpage.html')

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)

