

#def print_buzz():
 #   for i in range(1, 100):
  #      if i % 3 == 0 and i % 5 == 0:
   #         print("FizzBuzz")
    #    elif i % 3 == 0:
     #       print("Fizz")
      #  elif i % 5 == 0:
       #     print("Buzz")
        #else:
          #  print(i)

def test_buzz(testcase):
        if testcase % 3 == 0 and testcase % 5 == 0:
            return "FizzBuzz"
        elif testcase % 3 == 0:
            return "Fizz"
        elif testcase % 5 == 0:
            return "Buzz"
        else:
            return testcase

