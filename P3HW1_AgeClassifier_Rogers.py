# CTI-110 
# P3HW1 - Age Classifier 
# Kenneth Rogers 
# June 22, 2018
#
#If the person is 1 year old or less, he or she is an infant.
#If the person is older than one year, but younger than 13 years, he or she is a child.
#If the person is at least 13 years old, but less than 20 years old, he or she is a teenager.
#If the person is at least 20 years old, he or she is an adult.

ageGroup = int(input( 'Enter your age: '))

if ageGroup <= 1:
    print('You are in the Infant Age Group')
    
elif ageGroup < 13:
    print('You are in the Child Age Group')
elif ageGroup < 20:
    print('You are in the Teenager Age Group')
elif ageGroup >= 20:
    print('You are in the Adult Age Group')
