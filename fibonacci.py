numbers = int(input("The total number input is = "))


n1, n2 = 0, 1
count = 0


if numbers <= 0:
   print("Please enter a positive integer")
   
   
elif numbers == 1:
   print("Fibonacci sequence upto",numbers)
   print(n1)
   
   
else:
   print("The Fibonacci sequence is :")
   while count < numbers:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1