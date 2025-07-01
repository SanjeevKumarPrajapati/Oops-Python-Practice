class chatbook:
    def __init__(self):
        self.user_name=''
        self.password=''
        self.loggedin=False
        self.menu()
    
    def menu(self):
        user_input=input('''Welcome to chatbook !!!! Choose any option to proceed - 
                         1. Press 1 to signup
                         2. Press 2 to signin
                         3. Press 3 to write a post
                         4. Press 4 to message a friend
                         5. Press any other key to exit : \n''')
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            pass
        elif user_input=="4":
            pass
        else:
            exit()
    def signup(self):
        email=input("Enter your email :- ")
        passw=input("Enter your password here :- ")
        self.user_name=email
        self.password=passw
        print("You have successfully signed up.......")
        print("\n")
        self.menu()
        
    def signin(self):
        if self.user_name==" " and self.password==" ":
            print("Please sign-up first......")
        else:
            uname=input("Enter your email/username here :- ")
            pwd=input("Enter your password :- ")
            if self.user_name==uname and self.password==pwd:
                print("You have successfully signed in.........")
                self.loggedin=True
            else:
                print("Please enter correct credentials........")
        print("\n")
        self.menu()
        
        
        
        
        
obj=chatbook()