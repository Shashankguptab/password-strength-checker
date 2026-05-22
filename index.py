def check_pasword_strength(password):
    score=0

    #length
    if len(password)>=8:
        score+=1

    #upper
    if any(char.isupper() for char in password):
        score+=1
    
    #lower
    if any(char.islower() for char in password):
        score+=1

    #number check
    if any(char.isdigit() for char in password):
        score+=1
    
    #special character check
    special_characters="!@#$%^&*()_+-"
    if any(char in special_characters for char in password):
        score+=1
    
    #strength result
    if score==5:
        return "Strong Password"
    elif score>=3:
        return "Medium Password"
    else:
        return "Weak Password"
    
#main
password=input("Enter your password: ")
result=check_pasword_strength(password)
print("\n Password Strength: ",result)

