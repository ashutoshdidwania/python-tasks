# a=int(input("Enter the number:"))
# if a%2==0:
#     print(str(a) + " is an even number")
# else:
#     print(str(a) + " is an odd number")

n=int(input("Enter the number:"))
def fact(n):
    if n<2:
        return 1
    else:
        return n * (fact(n-1))
sample_number = fact(5)
print("Factorial of 5 is", sample_number)
