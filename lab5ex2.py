email=input("Enter your email:")
def checkmail(m):
    if "@" and "." in m:
        return True
    else:
        return False    
        
if checkmail(email)==True:
    print("Mail is valid.")
else:
    print("Mail is not valid.")    
