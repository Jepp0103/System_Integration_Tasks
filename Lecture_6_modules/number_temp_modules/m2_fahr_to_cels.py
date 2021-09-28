def convertFahrToCels(fahr_num: float):
    try:
        if isinstance(fahr_num, float):
            cel_num = round(((fahr_num - 32) / 1.8), 2)
            return cel_num
        else:
            raise Exception("Fahrenheit input has to be a float.")
    except Exception as incorrect_input_error:
        print("Invalid fahr input: ", incorrect_input_error)


# print(convertFahrToCels(76.20))
