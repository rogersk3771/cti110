#CTI 110
#P5T1: Kilometer Converter
#Write a program that asks the user to enter a distance in kilometers
#Then convert the distance from  kilometers to miles.
CONVERSION_FACTOR = 0.6214

def main():
    #gets a distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))
    
    #Display the distance converted to miles.
    show_miles(kilometers)

#The show_miles function converts the parameter km from
#kilometers to miles.
def show_miles(km):
    #Calculate miles.
    miles = km * CONVERSION_FACTOR

    #Display the miles.
    print(km, 'kilometers equals', miles, 'miles.')

#Call the main function.
    
main() 


