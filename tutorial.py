# # name = input('Enter your name: ')
# # distance_km = input('Enter distance in km: ')
# # distance_mi = float(distance_km)/1.609
# # print(f'Hi {name.title()}! {distance_km}km is equivalent to {distance_mi} miles')
# # print(f'Hi {name.title()}! {distance_km}km is equivalent to {round(distance_mi,1)} miles.')


# #example of extrating characters from a string
# msg='welcome to Python 101: Strings'
# msg1=msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]  
# print(msg1.title()) #output 1 Welcome Ring To Tyler

# #prints the sequence backwards
# print(msg1[::-1].title)

# #print  multiple lines ie print as typed in console - use """
# msg="""Dear Rebecca,
# The woods one day
# the bears went walking
# we saw them coming"""
# print(msg)

# msg='Samantha'
# print(msg.replace('Samantha','Michael'))

# #contains or doesnt contain key word
# msg='Welcome to Python 101: Strings'
# print('Python' in msg)
# msg='Welcome to Python 101: Strings'
# print('Python' not in msg)

# #better way to concatenate strings
# name='TERRY'
# color = 'RED'
# msg = '[' + name + '] loves the color ' + color + '!'
# msg1 = f'[{name}] loves the color {color.lower()}!'
# print(msg1)

# if statement
year_born = int(input("Enter your year of birth: "))

if year_born > 2000:
    print("Maleniel 🛠️")  # even prints the little icon assume unicode