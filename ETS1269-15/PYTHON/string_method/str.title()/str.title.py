# str_title.py

data = "python is best programming language"
titled = data.title()                     # => "Python Is Best Programming Language"
final = titled[0] + titled[1:].lower()    # Convert everything except the first char to lowercase
print(final)    
