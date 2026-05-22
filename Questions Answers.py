# Q1: Grocery discount final bill

amount = float(input("Enter purchase amount: "))

if amount >= 5000:
    discount_percent = 20
elif amount >= 3000:
    discount_percent = 15
elif amount >= 1000:
    discount_percent = 10
else:
    discount_percent = 0

discount = (discount_percent / 100) * amount
final_bill = amount - discount

print(f"Discount Applied: {discount_percent}%")
print(f"Discount Amount: {discount:.2f}")
print(f"Final Bill: {final_bill:.2f}")

# Q2: Bonus eligibility checker

attendance = float(input("Enter attendance percentage: "))
rating = int(input("Enter performance rating (1-5): "))

if attendance >= 85 and rating >= 4:
    print("Eligible for bonus")
else:
    print("Not eligible for bonus")


# Q3: Credential verification

PREDEFINED_USERNAME = "admin"
PREDEFINED_PASSWORD = "Admin@123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == PREDEFINED_USERNAME and password == PREDEFINED_PASSWORD:
    print("Login successful")
else:
    print("Invalid username or password")

# Q4: Speed monitoring

speed = int(input("Enter vehicle speed (km/h): "))
speed_limit = int(input("Enter speed limit (km/h): "))

if speed > speed_limit:
    print("Speed limit exceeded!")
else:
    print("Within speed limit.")


# Q5: Simple Interest calculator

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest (%): "))
time = float(input("Enter time (years): "))

si = (principal * rate * time) / 100
print(f"Simple Interest: {si:.2f}")

# Q6: Movie ticket pricing

age = int(input("Enter age: "))

if age < 12:
    category = "Child"
    price = 100
elif age < 60:
    category = "Adult"
    price = 200
else:
    category = "Senior Citizen"
    price = 150

print(f"Category: {category}")
print(f"Ticket Price: {price}")

# Q7: Largest among three numbers

s1 = float(input("Enter sales 1: "))
s2 = float(input("Enter sales 2: "))
s3 = float(input("Enter sales 3: "))

largest = max(s1, s2, s3)
print(f"Largest sales figure: {largest}")

# Q8: Student grade system

marks = []
for i in range(1, 6):
    m = float(input(f"Enter marks for subject {i}: "))
    marks.append(m)

percentage = sum(marks) / 5

if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "D"

print(f"Percentage: {percentage:.2f}")
print(f"Grade: {grade}")

# Q9: Max 3 login attempts

CORRECT_PASSWORD = "python123"
attempt = 1
max_attempts = 3

while attempt <= max_attempts:
    password = input(f"Attempt {attempt}/{max_attempts} - Enter password: ")

    if password == CORRECT_PASSWORD:
        print("Login successful")
        break

    print("Wrong password")
    attempt += 1

if attempt > max_attempts:
    print("Account locked (max attempts reached)")

# Q10: Food app menu loop

while True:
    print("\n--- MENU ---")
    print("1. Pizza")
    print("2. Burger")
    print("3. Pasta")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("You selected Pizza")
    elif choice == "2":
        print("You selected Burger")
    elif choice == "3":
        print("You selected Pasta")
    elif choice == "4":
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice, try again.")

# Q11: Print even numbers from 1 to 100

for num in range(2, 101, 2):
    print(num)

# Q12: Count overdue books

borrowed_books = ["B101", "B102", "B103", "B104", "B105"]
overdue_books = ["B102", "B104"]

count = 0
for book_id in borrowed_books:
    if book_id in overdue_books:
        count += 1

print("Overdue books count:", count)

# Q13: Electricity bill calculator function

def calculate_electricity_bill(units: int) -> float:
    if units <= 100:
        return units * 5
    elif units <= 300:
        return (100 * 5) + (units - 100) * 7
    else:
        return (100 * 5) + (200 * 7) + (units - 300) * 10

units_consumed = int(input("Enter units consumed: "))
bill = calculate_electricity_bill(units_consumed)
print(f"Electricity Bill: {bill:.2f}")

# Q14: Annual salary function

def calculate_annual_salary(monthly_salary: float) -> float:
    return monthly_salary * 12

monthly = float(input("Enter monthly salary: "))
print("Annual salary:", calculate_annual_salary(monthly))


# Q15: Palindrome checker

def is_palindrome(text: str) -> bool:
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

value = input("Enter a string: ")
print("Palindrome" if is_palindrome(value) else "Not Palindrome")

# Q16: Store marks and display average

n = int(input("How many marks you want to enter? "))
marks_list = []

for i in range(1, n + 1):
    marks = float(input(f"Enter marks {i}: "))
    marks_list.append(marks)

average = sum(marks_list) / len(marks_list)
print("Marks:", marks_list)
print(f"Average: {average:.2f}")

# Q17: Remove duplicates using set

product_ids = [101, 102, 103, 101, 104, 102, 105]
unique_ids = sorted(set(product_ids))

print("Original IDs:", product_ids)
print("Unique IDs:", unique_ids)

# Q18: City names in tuple

cities = ("Delhi", "Mumbai", "Lucknow", "Jaipur")
print("Cities visited:")
for city in cities:
    print(city)

# Q19: Character frequency

text = input("Enter a string: ")
freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print("Character frequency:", freq)



# Q20: Student record management

students = {}  # roll -> {name, marks}

while True:
    print("\n1. Add student")
    print("2. View student")
    print("3. View all")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        roll = int(input("Enter roll: "))
        name = input("Enter name: ")
        marks = float(input("Enter marks: "))
        students[roll] = {"name": name, "marks": marks}
        print("Student added/updated successfully.")

    elif choice == "2":
        roll = int(input("Enter roll to search: "))
        if roll in students:
            print("Record:", students[roll])
        else:
            print("Student not found.")

    elif choice == "3":
        print("All Records:", students)

    elif choice == "4":
        break
    else:
        print("Invalid choice.")

# Q21: Book search

inventory = ["Python", "Java", "C++", "SQL", "DSA"]
book = input("Enter book name to search: ")

if book in inventory:
    print("Book is available in inventory.")
else:
    print("Book not found in inventory.")

# Q22: Reverse each word

sentence = input("Enter a sentence: ")
words = sentence.split()

reversed_words = [w[::-1] for w in words]
result = " ".join(reversed_words)

print("Result:", result)


# Q23: Sort names

players = []
n = int(input("How many players? "))

for i in range(n):
    players.append(input("Enter player name: "))

players.sort()
print("Sorted player names:", players)

# Q24: Merge two lists and remove duplicates

list1 = [101, 102, 103, 104]
list2 = [103, 104, 105, 106]

merged_unique = sorted(set(list1 + list2))
print("Merged unique IDs:", merged_unique)


# Q25: Common elements of sets

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

common = set1.intersection(set2)
print("Common elements:", common)

# Q26: Receipt generation into a file

customer = input("Enter customer name: ")
items_count = int(input("How many items? "))

total = 0.0
lines = []
for i in range(1, items_count + 1):
    item = input(f"Item {i} name: ")
    price = float(input(f"Item {i} price: "))
    total += price
    lines.append(f"{i}. {item} - {price:.2f}")

filename = "receipt.txt"
with open(filename, "w") as file:
    file.write("----- RECEIPT -----\n")
    file.write(f"Customer: {customer}\n\n")
    file.write("\n".join(lines))
    file.write(f"\n\nTotal Amount: {total:.2f}\n")

print(f"Receipt saved in {filename}")

# Q27: Count words in a file

filename = input("Enter filename to read (example: receipt.txt): ")

try:
    with open(filename, "r") as file:
        content = file.read()

    words = content.split()
    print("Total words:", len(words))

except FileNotFoundError:
    print("File not found. Please check the filename.")


# Q28: Append feedback

feedback = input("Enter your feedback: ")
filename = "feedback.txt"

with open(filename, "a") as file:
    file.write(feedback + "\n")

print("Feedback saved successfully.")

# Q29: Attendance record system

attendance = {}  # roll -> status

n = int(input("How many students? "))
for i in range(n):
    roll = int(input("Enter roll number: "))
    status = input("Enter status (Present/Absent): ")
    attendance[roll] = status

search_roll = int(input("Enter roll to find attendance: "))

if search_roll in attendance:
    print("Attendance:", attendance[search_roll])
else:
    print("Roll number not found.")

# Q30: Department-wise employee details

company = {
    "IT": {"E101": "Rahul", "E102": "Neha"},
    "HR": {"E201": "Aman", "E202": "Priya"}
}

for dept, employees in company.items():
    print(f"\nDepartment: {dept}")
    for emp_id, emp_name in employees.items():
        print(emp_id, "-", emp_name)


# Q31: Highest temperature

temps = []
for day in range(1, 8):
    t = float(input(f"Enter temperature for day {day}: "))
    temps.append(t)

highest = max(temps)
print("Weekly temperatures:", temps)
print("Highest temperature:", highest)


# Q32: Display multiplication tables

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

for i in range(start, end + 1):
    print(f"\nTable of {i}")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")

# Q33: Restaurant billing system

def show_menu():
    print("\n--- MENU ---")
    print("1. Pizza  - 250")
    print("2. Burger - 120")
    print("3. Pasta  - 180")
    print("4. Exit")

def get_price(choice: str) -> int:
    if choice == "1":
        return 250
    if choice == "2":
        return 120
    if choice == "3":
        return 180
    return 0

total_bill = 0

while True:
    show_menu()
    choice = input("Choose item: ")

    if choice == "4":
        break

    price = get_price(choice)
    if price == 0:
        print("Invalid choice.")
    else:
        total_bill += price
        print(f"Item added. Current total: {total_bill}")

print("Final Bill:", total_bill)


# Q34: Parcel tracking

parcel_status = {
    "P101": "Delivered",
    "P102": "In Transit",
    "P103": "Out for Delivery"
}

parcel_id = input("Enter parcel ID: ")
print("Status:", parcel_status.get(parcel_id, "Parcel ID not found"))

# Q35: Mobile number validation

mobile = input("Enter mobile number: ")

if mobile.isdigit() and len(mobile) == 10:
    print("Valid mobile number")
else:
    print("Invalid mobile number")

#Q36. Hotel Booking System – Check Room Availability
 
rooms = [101, 102, 103, 104]

room = int(input("Enter room number: "))

if room in rooms:
    print("Room Available")
else:
    print("Room Not Available")
    
#Q37. Highest Expense from List

def highest_expense(expenses):
    return max(expenses)

expenses = [1200, 4500, 2300, 8000, 3200]

print("Highest Expense:", highest_expense(expenses))

#Q38. Split Sentence and Count Words

sentence = input("Enter a sentence: ")

words = sentence.split()

print("Words:", words)
print("Total Words:", len(words))

#Q39. Identify Toppers from Student Marks

marks = [78, 95, 88, 95, 67]

highest = max(marks)

print("Topper Marks:", highest)

password = input("Enter password: ")

if len(password) >= 8:
    print("Strong Password")
else:
    print("Weak Password")
    
#Q40. Password Strength Checker

password = input("Enter password: ")

if len(password) >= 8:
    print("Strong Password")
else:
    print("Weak Password")

#Q41. Factorial Using While Loop

num = int(input("Enter a number: "))

fact = 1
i = 1

while i <= num:
    fact = fact * i
    i += 1
print("Factorial =", fact)


#Q42. Employee Salary Above Threshold

employees = {
    "Aman": 40000,
    "Ravi": 55000,
    "Neha": 70000
}

threshold = int(input("Enter threshold salary: "))

for name, salary in employees.items():
    if salary > threshold:
        print(name, salary)
        
#Q43. Celsius to Fahrenheit for Multiple Values

temps = [0, 25, 37, 100]

for c in temps:
    f = (9/5) * c + 32
    print(c, "C =", f, "F")
    
    
#Q44. Frequency of Vowels in Paragraph

text = input("Enter paragraph: ")

count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Total vowels:", count)

#Q45. Verify Seat Number in Reservation List

seats = [1, 2, 5, 8, 10]

seat = int(input("Enter seat number: "))

if seat in seats:
    print("Seat Exists")
else:
    print("Seat Not Found")
    
    
#Q46. Menu Driven Calculator Using Functions

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = int(input("Enter choice: "))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if choice == 1:
    print(add(a, b))
elif choice == 2:
    print(sub(a, b))
elif choice == 3:
    print(mul(a, b))
elif choice == 4:
    print(div(a, b))
else:
    print("Invalid Choice")
    
    
#Q47. Read Names from File and Sort

file = open("names.txt", "r")

names = file.readlines()

names.sort()

for name in names:
    print(name.strip())

file.close()


#Q48. Categorize Recharge Plans
price = int(input("Enter recharge amount: "))

if price < 200:
    print("Basic Plan")
elif price < 500:
    print("Standard Plan")
else:
    print("Premium Plan")
    
#Q49. Generate Usernames from Full Names

name = input("Enter full name: ")

username = name.lower().replace(" ", "")

print("Username:", username)

#Q50. Find Month with Maximum Sales

sales = {
    "Jan": 5000,
    "Feb": 7000,
    "Mar": 9000,
    "Apr": 6500
}

month = max(sales, key=sales.get)

print("Highest Sales Month:", month)
print("Sales:", sales[month])