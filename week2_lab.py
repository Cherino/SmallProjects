#1 & #4 Uses Try, Except & Else
'''
My program will take an input from a user "Job Role" and using
a jobsites api I will scrape relevant data from roles that meet
the user's input. Then it will parse data from the job posting
to find skills related to that role and send that back to
the user to help upskill them in that role.
'''

'''
while True:
    try:
        celcius = int(input("Input Temperature in Celcius"))
    except:
        print("Please only enter an integer.")
    else:
        print("The Temperature is ",(celcius*9/5)+32,"Degrees Farenheit")
        print("Again!?")
'''  
#2
'''
varstr = "Hello! 123"
varint = 123
varflt = 1.23
varbool = True

print("So, A string such as '",varstr,"' is a datatype which has a data value assigned to each " \
"character including numerical ones. Strings can concatinate with other strings but not with Ints, " \
"Floats or Bools")
print("")
print(varint, "This is an integer. They are primarily used for mathematical operations such as counting. They tend to be" \
"able to be concatinated with strings and easily changed in their datatype to a string. However you cannot use math operations" \
"with this whilst it is a string type.")
print("")
print(varflt, "This is a floating point integer. typically known as a float. they utilise 32bit(Single precision)" \
"which is mostly used, it's fairly accurate when working with simple math however I wouldn't use it unless I have to" \
"as using too many floats can cause issues as a float is not an absolute like an integer. The computer makes a close approximation" \
"to the value assigned to the float and can cause math errors after repeated use. There is such thing as a 64bit float, this is" \
"known as Double precision. This does take up more memory but has a strong use case for floats that must remain stable over extended" \
"periods of time. The double is more expensive but more precise.")
print("")
print(varbool,not varbool," <-- These are True or False statements, 1 or 0. These are used as a foundation of choice" \
"in programming.")
'''

#3
'''
name = "Caileb"
age = str(26)
course = "Computer Science and AI"
favlang = [3.14,"Thon"]

print("Hi, I'm "+name+"I'm "+age+"and I'm studying "+course+". My Favourite Language is "+str(favlang[0])+favlang[1])
'''