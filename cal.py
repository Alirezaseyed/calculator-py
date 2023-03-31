# در اینجا با تعریف متقیر به برنامه میگیم هر حرف چه کاری را انجام دهد
# ایکس و وای دو عدد هستند

# به برنامه میگیم حرف "add" یعنی جمع
def add(x, y):
    return x + y

# حرف "subtract"یعنی تفریق
def subtract(x, y):
    return x - y

# "multiply" یعنی ضرب
def multiply(x, y):
    return x * y

# "divide" یعنی تقسیم
def divide(x, y):
    return x / y

# وقتی که برنامه شروع می شود از کاربر میخواهد انتخاب کند که چه کاری را دوست دارد انجام دهد
# یا قرار دادن هر کدام از شکل ها عملگر انتخاب می شود
print("amalgar khod ra entekhab konid")
print("+.jam")
print("-.tafrigh")
print("*.zarb")
print("/.tagsim")

while True:
    # در اینجا عملگر کاربر را دریافت می کند
    choice = input("Enter choice(+/-/*/'/'): ")

    
    if choice in ('+', '-', '*', '/'):
        #در اینجا تو متغیر تعریف می کنیم
        num1 = float(input("adad aval ro vared konid: "))
        num2 = float(input("adad dovom ra vare konid: "))
#و میگیم اگر عملگر انتخاب شده پلاس بود جمع کند
        if choice == '+':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '/':
            print(num1, "/", num2, "=", divide(num1, num2))
        
#در این مرحله از کاربر می پرسد آیا دوست دارد ادامه دهد؟
#اگر کاربر yes را نوشت برنامه مجدد ران می شود
#اگر کاربر no نوشت برنامه بسته می شود
        next_calculation = input("aya dost darid adad digary ra emtehan konid? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")
