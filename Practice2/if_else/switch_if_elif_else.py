status_code = 404

match status_code:
    case 200:
        print("Success")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case _:  
        print("Unknown Status")

#2 ex
day = 4

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case _:
        print("Other day")

#3 example
operation = "+"

match operation:
    case "+":
        print(10 + 5)
    case "-":
        print(10 - 5)
    case "*":
        print(10 * 5)
    case "/":
        print(10 / 5)
    case _:
        print("Unknown operation")

#4 example
choice = 2

match choice:
    case 1:
        print("Pizza")
    case 2:
        print("Burger")
    case 3:
        print("Pasta")
    case _:
        print("Invalid choice")

#ex5
color = "green"

match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Unknown color")