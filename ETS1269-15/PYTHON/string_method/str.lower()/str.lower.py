# str_lower.py

data = "PYTHON IS BEST PROGRAMMING LANGUAGE"
lowered = data.lower()                  # => "python is best programming language"
final = lowered[0].upper() + lowered[1:]  # Fix the first letter to uppercase
print(final)                            # "Python is best programming language"

