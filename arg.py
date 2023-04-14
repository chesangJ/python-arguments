def hello(*names):
    for name in names:
        print(f"Hello {name}")
        
# write a function that accepts any number of intergers and retuns the result of all of them
        
        
def multiply(*digits):
    result=1
    for digit in digits:
        result*=digit
    return result

def student_attributes(**kwargs):
    for key,value in kwargs.items():
     print(f"{key}:{value}")
     
    #  DO MORE
    
def my_country(country="Burundi"):
    print(f"Hello {country}")
    

def concatenate_args(*strings):
    result=" "
    for string in strings:
        result+=string
    return result
def concatinate_kwargs(**kwargs):
    result=" "
    for key,value in kwargs.items():
        result +=(f"{key},{value},")
    return result