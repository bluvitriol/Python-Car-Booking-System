import pandas as pd
#eclass=pd.read_csv('D:/eclass.csv')
#sclass=pd.read_csv('D:/sclass.csv')

def read_csv_with_retry(file_path, encodings=['utf-8', 'latin-1']):
    for encoding in encodings:
        try:
            return pd.read_csv(file_path, encoding=encoding)
        except UnicodeDecodeError:
            pass
    raise UnicodeDecodeError("Unable to decode the CSV file with the specified encodings")
eclass=read_csv_with_retry('D:/eclass.csv')
sclass=read_csv_with_retry('D:/sclass.csv')
maybach = read_csv_with_retry('D:/MyDevice.csv')

print('Mercedes-Benz welcomes you to the world of the BEST OR NOTHING!')
print('Would you like to dive into the vast universe of Mercedes ?')
answer=input('Please enter: yes or no - ')
while answer=='yes':
    print('There are 3 categories in total : Electric, Sedan, and Maybach')
    category=input('Please enter the category of your choice - ')
    if category=='Electric':
        print("Incomparable Modernity. It's like Driving a Fast Cloud!")
        print(eclass)
    elif category=='Sedan':
        print('The new S-Class. Unstoppable.Just Like You.')
        print(sclass)
    elif category=='Maybach':
        print('The all-new Mercedes-Maybach! Designed for the wilderness.Enjoyed in the city.')
        print(maybach)
    else:
        print('Please enter a valid category')
        category=input('Please enter the category of your choice - ')
    print('Would you like to try a Test Drive with your favourite car out of these free of cost?')
    drive=input('Please enter: yes or no - ')
    if drive=='yes':
        car=input('Enter the car model you liked the most from the following : E 220d | E 350d | S 400d 4MATIC | S450 4MATIC | Maybach S 650 | Maybach GLS 600 4MATIC - ')
        name=input('Enter Full Name : ')
        num=input('Enter Phone Number : ')
        city=input('Enter House Location : ')
        print(name,',',num,',',city,',',car)
        print('THANKYOU FOR CHOOSING MERCEDES! Your test drive has been successfully booked at your nearest Mercedes-Benz showroom :) You would receive a call soon!')
    answer=input('Are you interested in another category?')
else:
    print('Thankyou for visiting Mercedes-Benz !')
    print('We appreciate your efforts :)')
