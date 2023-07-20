try:
    numerator = 10
    denominator = 0
    result = numerator/denominator
    print(result)
except:
    print("Error: Denominator cannot be 0.")

try:
    a=12
    b=2
    c=a%b
    print(c)
except:
    print("c is not greater than to b")

try:
    a=12
    b=2
    c=a%b
    print(c)
except:
    print("a is not greater than to b")

try:
    a=12
    b=2
    c=b%a
    print(c)
except:
    print("a is not greater than to b")

def addNumbers(num1,num2):
    try:
        return(num1+num2)
    except TypeError:
        return ("invalid Number")
print(addNumbers(1,2))
print(addNumbers(5,10))
print(addNumbers(7,"a"))
print(addNumbers(99,1))
print("executive completed")

def addNumbers(num1,num2):
    try:
        return(num1+num22222)
    except TypeError:
        return ("invalid Number")
    except NameError:
        return("invalid parameter")

print(addNumbers(1,2))
print(addNumbers(5,10))
print(addNumbers(7,"a"))
print(addNumbers(99,1))
print("executive completed")



def addNumbers(num1,num2):
    try:
        print(num1+num22222)
    except TypeError:
        print("invalid Number")
    except NameError:
        print("invalid parameter")

print(addNumbers(1,2))
print(addNumbers(5,10))
print(addNumbers(7,"a"))
print(addNumbers(99,1))
print("executive completed")


def addNumbers(num1,num2):
    try:
        return(num1+num2)
    except Exception as e:
        return(e)
print(addNumbers(1,2))
print(addNumbers(5,10))
print(addNumbers(7,"a"))
print(addNumbers(99,1))
print("executive completed")

def addNumbers(num1,num2):
    try:
        return(num1+num22222)
    except TypeError:
        return("invalid Number")
    except NameError:
        return("invalid parameter")
    except Exception as e:
            return(e)

print(addNumbers(1,2))
print(addNumbers(5,10))
print(addNumbers(7,"a"))
print(addNumbers(99,1))
print("executive completed")

def addNumbers(num1,num2):
    try:
        if(isinstance(num1,int)or isinstance(num1,float))and (isinstance(num2,int)or(num2,float)):
            return(num1+num2)
        else:
            raise exception("only int and float values are allowed")
    except Exception as e:
        return e

print(addNumbers(1,2))
print(addNumbers(5,10))
print(addNumbers("b","a"))
print(addNumbers(99,1))
print("executive completed")
        

def addNumbers(num1,num2):
    try:
        print(num1+num2)
    except TypeError:
        print("Invalid Number")
    except Exception as e:
        print(e)
    else:
        print("succsfull...")

addNumbers(5,2)

def addNumbers(num1,num2):
    try:
        print(num1+num2)
    except TypeError:
        print("Invalid Number")
    except Exception as e:
        print(e)
    else:
        print("succsfull...")

addNumbers(5,"a")


def addNumbers(num1,num2):
    try:
        print(num1+num2)
    except TypeError:
        print("Invalid Number")
    except Exception as e:
        print(e)
    else:
        print("succsfull...")
    finally:
        print("the end...")

addNumbers(5,2)


def addNumbers(num1,num2):
    try:
        print(num1+num2)
    except TypeError:
        print("Invalid Number")
    except Exception as e:
        print(e)
    else:
        print("succsfull...")
    finally:
        print("the end...")

addNumbers(5,"b")



try:
    
    even_numbers = [2,4,6,8]
    print(even_numbers[5])

except ZeroDivisionError:
    print("Denominator cannot be 0.")
    
except IndexError:
    print("Index Out of Bound.")



try:
    
    even_numbers = [2,4,6,8]
    print(even_numbers[4])

except ZeroDivisionError:
    print("Denominator cannot be 0.")
    
except IndexError:
    print("Index Out of Bound.")



try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")
    
finally:
    print("This is finally block.")



try:
    a=6
    b=2
    result = a/b

    print(result)

except:
    print("a cannot be 0 ")
finally:
    print("i love india")














    





