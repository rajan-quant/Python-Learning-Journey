
try:
    file = open(r'C:\Users\rajat\OneDrive\Desktop\Programming\Python\Exception handling\errors.txt',"r")
    content = file.read()
    print(content)

except FileNotFoundError:
    print('File not found')

finally :
    file.close()
    print('file operation complete')