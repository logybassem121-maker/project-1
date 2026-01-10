print("Welcome to the exam practice program choose your subject")
print("a.physics")
print("b.math")
print("c.chemistry")
x=input()

def physics():
    c=0
    print("Question 1:")
    print("What is Newton's 2nd law?")
    print("a.(v=s/t)")
    print("b.(F=ma)")
    print("c.(I=V/R)")
    y=input("Enter your answer:")
    if y=="b":
        print("Correct answer!!")
        c+=1
    elif y=="a" or y=="c":
        print("incorrect answer the correct answer is b")
    else:
        print("Please choose a,b or c")
        
    print("Question 2:")
    print("What is the SI unit for power?")
    print("a.watts")
    print("b.volts")
    print("c.joules")
    y=input("Enter your answer:")
    if y=="a":
        print("Correct answer!!")
        c+=1
    elif y=="b" or y=="c":
        print("incorrect answer the correct answer is a")
    else:
        print("Please choose a,b or c")
    print("your score is"+str(c)+"/2")


def Math():
    c=0
    print("Question 1:")
    print("What is the diffrential of sin(x)?")
    print("a.tan(x)")
    print("b.-cosx")
    print("c.cosx")
    y=input("Enter your answer:")
    if y=="c":
        print("Correct answer!!")
        c+=1
    elif y=="a" or y=="b":
        print("incorrect answer the correct answer is c")
    else:
        print("Please choose a,b or c")
        
    print("Question 2:")
    print("What is the integral of 1/x?")
    print("a.ln(x)")
    print("b.e^x")
    print("c.ln(ln(x))")
    y=input("Enter your answer:")
    if y=="a":
        print("Correct answer!!")
        c+=1
    elif y=="b" or y=="c":
        print("incorrect answer the correct answer is a")
    else:
        print("Please choose a,b or c")
    print("your score is"+str(c)+"/2")
    
def chemistry():
    c=0
    print("Question 1:")
    print("What is avogadro's number?")
    print("a.1.66*10^-24")
    print("b.6.022x10^23")
    print("c.63.5666")
    y=input("Enter your answer:")
    if y=="b":
        print("Correct answer!!")
        c+=1
    elif y=="a" or y=="c":
        print("incorrect answer the correct answer is b")
    else:
        print("Please choose a,b or c")
        
    print("Question 2:")
    print("What is the element symbol of potassium")
    print("a.P")
    print("b.Pa")
    print("c.K")
    y=input("Enter your answer:")
    if y=="c":
        print("Correct answer!!")
        c+=1
    elif y=="b" or y=="a":
        print("incorrect answer the correct answer is c")
    else:
        print("Please choose a,b or c")
    print("your score is"+str(c)+"/2")

while True:
    if x=="a":
        physics()
    elif x=="b":
        math()
    elif x=="c":
        chemistry()
    print("Would you like to choose another subject?")
    x=input("Enter new subject:")