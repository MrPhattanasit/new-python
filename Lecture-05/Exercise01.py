def is_armstrong(number):
   num_str = str(number)
   num_digits = len(num_str)
   initial_total = 0

   for digit in num_str:
      initial_total += int(digit) ** num_digits
        
   return initial_total == number

print(is_armstrong(153)) #true
print(is_armstrong(9474)) #true
print(is_armstrong(123)) # false
