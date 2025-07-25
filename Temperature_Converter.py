'''
Temperature converter.
Coder: Drizisokay
Convert temperatures from Celsius to fahrenheit. Vice versa!
'''

def celsius_to_fahrenheit(c):
    return (1.8 * c) + 32


#converting Fahrenheit to Celsius.
def fahrenheit_to_celsius(f):
    return (f-32) / 1.8 


print("0C =", celsius_to_fahrenheit(0),"f")
print("100C = ", celsius_to_fahrenheit(100), "F")
print("40F =", fahrenheit_to_celsius(40), "C")
print("80F = ", fahrenheit_to_celsius(80), "f")