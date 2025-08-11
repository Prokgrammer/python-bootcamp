
#Celcius to fahrenheit
def c_to_f(c):
    return(c * 9/5) + 32

#fahrenheit to celcius

def f_to_c(f):
    return(f -32) * 5/9

#celsius to kelvin
def c_to_k(c):
    return c + 273.15


#kelvin to celcius

def k_to_c(k):
    return k - 273.15

# fahrenheit to kelvin
def f_to_k(f):
    return (f - 32) * 5/9 + 273.15

#kelvin to fahrenheit
def k_to_f(k):
    return(k-273.15) * 5/9 + 32