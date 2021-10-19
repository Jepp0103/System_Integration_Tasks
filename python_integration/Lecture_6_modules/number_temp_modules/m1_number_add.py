def addOneToNumber(num: int):
    try:
        if num > 9 or num < 0 or type(num) != int:
            raise Exception("Number has to be lower than 9 and higher than 0")
        if num == 9:
            num = 0
            return num
        else:
            num += 1
            return num
    except Exception as incorrect_input_error:
        print("Incorrect number input", incorrect_input_error)


# print(addOneToNumber(5))
