import phonenumbers
from phonenumbers import carrier, geocoder, timezone
import sys

try:
    phoneNumber = sys.argv[1]
    phoneNumber = phonenumbers.parse(phoneNumber)
    # get timezone a phone number
    print("Timezone of Phone Number:", timezone.time_zones_for_number(phoneNumber))

    # getting carrier of a phone number
    print("Carrier of Phone Number:", carrier.name_for_number(phoneNumber, "en"))

    # getting region information
    print("Region of Phone Number:", geocoder.description_for_number(phoneNumber, "en"))

    # validating a phone number
    print("Valid Phone Number : ", phonenumbers.is_valid_number(phoneNumber))

    # checking possibilty of a number
    print("Checking Possibilty of Phone Number : ", phonenumbers.is_possible_number(phoneNumber))
except Exception as exception:
    print(exception)