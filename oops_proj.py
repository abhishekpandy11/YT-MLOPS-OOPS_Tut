class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input('''Welcome to chatbook !! How would you like to proceed?
                            1. Press 1 to signup
                            2. Press 2 to signin
                            3. Press 3 to write a post
                            4. Press 4 to message a friend
                            5. Press any other key to exit
                           
                            ->''')
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            self.my_post()
        elif user_input == '4':
            self.sendmsg()
        else:
            exit()

    def signup(self):
        email = input('Enter your email here -> ')
        pwd = input('Enter your password here -> ')
        self.username = email
        self.password = pwd
        print('You have signed up successfully!!\n')
        self.menu()
    
    def signin(self):
        if self.username == '' or self.password == '':
            print('Please signup first by pressing 1 in the main menu\n')
        else:
            uname = input('Enter your email/username here -> ')
            pwd = input('Enter your password here -> ')
            if self.username == uname and self.password == pwd:
                print('You have signed in successfully !!')
                self.loggedin = True
            else:
                print('Please input correct credentials.....')
        print('\n')
        self.menu()


    def my_post(self):
        if self.loggedin==True:
            txt = input('Enter your message here->')
            print(f'Following content has been posted-> {txt}')
        else:
            print('YOu need to sigin first to post something,....')
        print('\n')
        self.menu()

    def sendmsg(self):
     if self.loggedin == True:
         txt = input('Enter your message here->')
         frnd = input('whom to send the msg?->')
         print(f'Your message has been sent to{frnd}')
     else:
        print('YOu need to sigin first to post something,....')
        print('\n')
        self.menu()



# Run the app
# user1 = chatbook()
