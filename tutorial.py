# name = input('Enter your name: ')
# distance_km = input('Enter distance in km: ')
# distance_mi = float(distance_km)/1.609
# print(f'Hi {name.title()}! {distance_km}km is equivalent to {distance_mi} miles')
# print(f'Hi {name.title()}! {distance_km}km is equivalent to {round(distance_mi,1)} miles.')


#example of extrating characters from a string
msg='welcome to Python 101: Strings'
msg1=msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]  
print(msg1.title()) #output 1 Welcome Ring To Tyler

#prints the sequence backwards
print(msg1[::-1].title)