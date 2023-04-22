def isEmail(data):
       
        search = data.find("@")
        com = data.find(".com")

        if(search == -1 or len(data) - 4 != com):

                return False
        else:
                return True
        
def Verification(username,password,email):
  

         if (username is None or password is None or email is None or username == '' or password == '' or email == '' or not username):
                           return {'message': 'You must complete the data.'}
         if (len(username) < 5 or len(password) < 5 or len(email) < 5 or len(password) > 15 or len(username) > 15 or len(email) > 256):
                           return {'message': 'The username and password must not be less than 4 characters or more than 14.'}
         if (isEmail(email) == False):
                            return {'message': 'The email is wrong.'}
         else:
                 return None