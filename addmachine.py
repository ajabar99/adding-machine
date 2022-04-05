while True:
    try:
        first_number = int(input('what is the first number you want to add?'))
        second_number = int(input('what is the second number you want to add?'))
        sum = first_number + second_number
        print('the sum of your two numbers are',sum)
        break
    except:
            print("you are so silly. thats is not an integer...")