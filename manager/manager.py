# DB storage
user={
     "ali":"1234",
     "ahmed":"1234",
     "amr":"1234",
     "mohamed":"1234"
}
operators=["delete","update","append","updatepass"]
name= input("please enter your name : ")
if name in user : 
    tries=3
    password=input("enter the password : ")
    if password != user[name] :
         print("incorrect password please try again")
         tries-=1
         password=input("enter your password :")
         
    else :
         print("correct password")     
         print(f"Hello {name.strip().capitalize()} welcome back")

    options=input("Do you want make any options yes or no? ")
    if options == "yes" :
        chose=input("chose any of these options \t Delete : \t update : \t append : \n")
        #Delete
        if chose == "delete":
            removedname=input("enter the name you want to remove it ")
            del(user[removedname])
            print("the name has been removed ")
            print(user)
            #update
        elif chose=="update" :
                answer=input("Do you want to change your name ? y/n ")
                if answer=="yes" :
                    theNewName=input("enter the new name :")
                    user[theNewName] =user.pop(name)
                    print("the name has been updated ")
                    print(user)
                else:
                     theNewName=name    
                passwordAnswer=input("Do you want change your password ? y/n ")
                if passwordAnswer == "yes" :
                     newPassword=input("Enter the new password :")
                     user[theNewName]=newPassword
                     print(f"Password has been changed {user}")

                #append
        elif chose == "append":
             newmember=input("Add the new member you want :")
             newvalue=input("Add the password :")
             user[newmember]=newvalue
             print("Added successfuly ")
             view=input("do you want to see the list ?").strip()
             if view =="yes" :
                  print(user)
             else :
                    print("your program has end")
else :
     print("Sorry you have no access on the program ")                    