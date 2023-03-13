#!/usr/bin/env python
# coding: utf-8

# In[16]:


n=int(input('''\t\tpress 1 to convert currency
                press 2 to calculate BMI
                press 3 to convert temperature
                press 4 to calculate age
                press 5 to see calender
                press 6 to roll dice
                press 7 to use arithmetic calculator
                press 8 to generate random password
                press 9 to detect language
                press 10 to make QR code of link'''))
if n==1:
    from forex_python.converter import CurrencyRates
    c=CurrencyRates()

    a= int(input("Enter the Amount:"))
    b=input("From Currency:").upper() 
    x=input("To Currency: ").upper()


    ans=c.convert(b,x, a)

    print("Result=",ans)
elif n==2:
    
    height=float(input("Enter Your Height in cm:"))
    weight=float(input("Enter Your Weight in Kg:"))

    height=height/100

    BMI=weight/(height*height)

    print("Your Body Mass Index is:",BMI)
    if BMI>0:
        
        if BMI<=16:
        
            print("You are Severely Underweight")

        elif BMI<=18.5:
            print("You are underweight")

        elif BMI<=25:
            print("You are Healthy")

        elif BMI<=30:
            print("You are Overweight")

        else:
            print("very very high!")
elif n==3:
    
    n=int(input("for fahrenheit to celcius=1,celcius to fahrenheit=2"))
    if n==1:
        fahrenheit=int(input("Enter the Value of fahrenheit:"))

        celsius=(fahrenheit-32)*5/9

        print("celsius Value:",celsius)
        
    elif n==2:
        celsius=int(input("Enter the Value of celsius:"))

        fahrenheit=(celsius*(9/5))+32

        print("fahrenheit Value:",fahrenheit)
    else:
        print("invalid operation")
elif n==4:
    def ageCalculator(y,m,d):
        import datetime
        today = datetime.datetime.now().date()
        dob = datetime.date(y,m,d)
        age = int((today-dob).days / 365.25)
        print(age)
    y=int(input("Enter year of birth:"))
    m=int(input("Enter month of birth:"))
    d=int(input("Enter date of birth:"))
    ageCalculator(y,m,d)
elif n==5:
    import calendar
    year=int(input("Enter the year:"))
    cal=calendar.calendar(year)
    print(cal)
elif n==6:
    import random
    x="y"

    while x=="y":
        random_number=random.randint(1,6)
    
        if random_number==1:
            print("[---------]")
            print("[         ]")
            print("[    *    ]")
            print("[         ]")
            print("[---------]")

        elif random_number==2:
            print("[---------]")
            print("[  *      ]")
            print("[         ]")
            print("[      *  ]")
            print("[---------]")

        elif random_number==3:
            print("[---------]")
            print("[         ]")
            print("[ *  *  * ]")
            print("[         ]")
            print("[---------]")

        elif random_number==4:
            print("[---------]")
            print("[ *     * ]")
            print("[         ]")
            print("[ *     * ]")
            print("[---------]")

        elif random_number==5:
            print("[---------]")
            print("[ *     * ]")
            print("[    *    ]")
            print("[ *     * ]")
            print("[---------]")

        elif random_number==6:
            print("[---------]")
            print("[ *  *  * ]")
            print("[         ]")
            print("[ *  *  * ]")
            print("[---------]")

        x=input("Press y to Roll Again and Press Any Other Key for Exit:")
elif n==7:
    num1=int(input("Enter the First Number:"))
    oper=input("Enter the Operation:")
    num2=int(input("Enter the Second Number:"))

    if oper=="+":
        sum=num1+num2
        print("The Answer is:",sum)

    elif oper=="-":
        subs=num1-num2
        print("The Answer is:",subs)

    elif oper=="*":
        mul=num1*num2
        print("The Answer is:",mul)

    elif oper=="/":
        div=num1/num2
        print("The Answer is:",div)

    else:
        print("Wrong Operation Input!")

    print("=========================\n")
elif n==8:
    import random

    passlen=int(input("Enter the Length of Password:"))
    x="abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?<>"
    password="".join(random.sample(x,passlen))
    print(password)    
elif n==9:
    from langdetect import detect

    text=input("Enter the Sentence:")

    print(detect(text))
elif n==10: 
        import qrcode
        import matplotlib.pyplot as plt
        x=input("Enter link you want to convert to convert to QRcode: ")
        img=qrcode.make(x)
        y=input("enter name tou want to save and apply .png: ")
        img.save(y)
        
        
        plt.imshow(img,cmap="gray")
    
    
    
    


# # 122
# 

# In[ ]:




