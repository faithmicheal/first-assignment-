pizza = int(input("Enter the amount of pizza you started with: "))
eaten_pizza = int(input("Enter the amount of pizza you already eaten: "))

total_pizza_left = pizza - eaten_pizza

print("You have", total_pizza_left, "Pizza left")