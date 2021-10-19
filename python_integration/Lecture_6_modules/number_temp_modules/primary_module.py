import m1_number_add, m2_fahr_to_cels, m3_next_let_alp_eng, m4_cels_to_fahr
import requests

# Importing sub modules to main module - bottom up approach because
# sub modules were made first.
while True:
    try:
        print("Type number to add by one:")
        num_input = int(input())
        # print(type(num_input))

        print("Type amount of fahrenheit which should be converted into celcius:")
        fahr_input = float(input())
        # print(type(fahr_input))

        print("Type letter to get the next letter in the alphabet:")
        letter_input = input()
        # print(type(letter_input))

        print("Type amount of celcius which should be converted into fahrenheit:")
        cel_input = float(input())
        # print(type(num_input))

        num = m1_number_add.addOneToNumber(num_input)
        fahr_to_cel = m2_fahr_to_cels.convertFahrToCels(fahr_input)
        next_letter = m3_next_let_alp_eng.getNextLetterAlphabet(letter_input)
        cel_to_fahr = m4_cels_to_fahr.convertCelsToFahr(cel_input)

        print("number: ", num)
        print("fahr to cel: ", fahr_to_cel)
        print("next letter: ", next_letter)
        print("cel to fahr:", cel_to_fahr)

        # Sending the request as a post
        if (
            num != None
            and fahr_to_cel != None
            and next_letter != None
            and cel_to_fahr != None
        ):
            print("Enter phone number: ")
            phone = input()
            message = (
                "Number is: "
                + str(num)
                + ", to celcius is: "
                + str(fahr_to_cel)
                + ", next letter is: "
                + next_letter
                + " and to fahrenheit is "
                + str(cel_to_fahr)
            )

            endpoint = "https://fatsms.com/api-send-sms"
            my_api_key = "77d3350e-22a4-4861-94f3-0fd99cba1a6e"
            data_dict = {"to_phone": phone, "api_key": my_api_key, "message": message}
            response = requests.post(endpoint, data=data_dict)

            print("Response from server:", str(response.text))

    except Exception as wrong_types_error:
        print("Wrong types typed in input:", wrong_types_error)
