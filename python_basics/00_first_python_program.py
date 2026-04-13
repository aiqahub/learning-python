print("Hello, world")

phrase = "Hello, world"
print(phrase)

numbers = [1, 2, 3, 4]
total = 0
for number in numbers:
    total += number
print(total)


colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "indigo",
    "violet"
]

for color in colors:
    print(color)

for index, color in enumerate(colors):
    print(index, "\t", color)

# Getting to Know Variables in Python
# variable_name = value


# Data Storage Variables
contacts = [
    ("Linda", "111-2222-3333", "linda@example.com"),
    ("Joe", "111-2222-3333", "joe@example.com"),
    ("Lara", "111-2222-3333", "lara@example.com"),
    ("David", "111-2222-3333", "david@example.com"),
    ("Jane", "111-2222-3333", "jane@example.com")
]

for contact in contacts:
    print(contact)

for name, phone, email in contacts:
    print(phone, name)

# Public and Non-Public Variable Names
_timeout = 30

def get_timeout():
    return _timeout

def set_timeout(seconds):
    global _timeout
    _timeout = seconds