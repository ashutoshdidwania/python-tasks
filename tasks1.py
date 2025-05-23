try:
    file=open('sample.txt','r')
    reading_file=file.read()
    print(reading_file)
except:
    print("The file sample.txt was not found")

