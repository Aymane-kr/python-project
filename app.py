import phonenumbers 
from phonenumbers import geocoder, carrier, timezone

print("x" * 50)

en_num = input("enrter your phone number : ")

phone_num = phonenumbers.parse(en_num, None)

print(phone_num)

print(f"the location of this number is: {geocoder.description_for_number(phone_num, "en")}")

print(f"the carrier of this number is : {carrier.name_for_number(phone_num, "en")}")

print(f"the timezone of this number is:{timezone.time_zones_for_geographical_number(phone_num)}")