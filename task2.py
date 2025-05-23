user_input=input("Enter text to write to the file")
file=open('output.txt', 'w')
file.write(user_input + '\n')
print("Data successfully added to output.txt")

additional_input=input("Enter additional text to append")
file=open('output.txt','a')
file.write(additional_input + '\n')
print("Data successfully appended")

with open ('output.txt') as file:
    reading_file=file.read()
print(reading_file)