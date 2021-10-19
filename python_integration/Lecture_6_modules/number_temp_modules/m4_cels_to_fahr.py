def convertCelsToFahr(cels_num: float):
    try:
        if type(cels_num) != float:
            raise Exception("Input has to be a float.")
        else:
            fahr_num = round((cels_num * 1.8 + 32), 2)
            return fahr_num
    except Exception as incorrect_input_error:
        print("Invalid input: ", incorrect_input_error)


# print(convertCelsToFahr(24.5))
