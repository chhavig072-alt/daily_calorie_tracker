# Name: Chhavi Goyal 
# Date: 2-November-2025 
# Project Title: Daily Calorie Tracker CLI

import datetime

# --- Task 1: Welcome Message ---
print("=============================================")
print("   Welcome to the Daily Calorie Tracker!   ")
print("=============================================")
print("\nThis tool helps you log your meals and track")
print("your total calorie intake for the day.")
print("---------------------------------------------")
# --- Task 2: Input & Data Collection ---

# Initialize two empty lists to store the data
meal_names = []
meal_calories = []

# Ask the user how many meals they want to enter
# We use int() to convert the input string to a number
try:
    num_meals = int(input("\nHow many meals would you like to log? "))
except ValueError:
    print("Invalid input. Please enter a number. Defaulting to 1.")
    num_meals = 1

# Loop 'num_meals' times
for i in range(num_meals):
    print(f"\n--- Logging Meal #{i + 1} ---")
    
    # Get the meal name
    name = input("Enter meal name (e.g., Breakfast, Lunch): ")
    
    # Get the calorie amount
    # We use a loop here to make sure they enter a valid number
    while True:
        try:
            calories = int(input(f"Enter calories for {name}: "))
            break # Exit the loop if conversion to int is successful
        except ValueError:
            print("Invalid input. Please enter a whole number for calories.")
            
    # Add the data to our lists
    meal_names.append(name)
    meal_calories.append(calories)

# --- End of Task 2 ---

# Print the lists to check if it's working
print("\nMeals Logged:")
print(meal_names)
print("Calories Logged:")
print(meal_calories)
# --- Task 3: Calorie Calculations ---

# Calculate the total calories
# The sum() function adds up all numbers in a list
total_calories = sum(meal_calories)

# Calculate the average calories per meal
# We check if num_meals is not zero to avoid a ZeroDivisionError
if num_meals > 0:
    average_calories = total_calories / num_meals
else:
    average_calories = 0 # Default to 0 if no meals were entered

# Get the user's daily calorie limit
while True:
    try:
        daily_limit = int(input("\nWhat is your daily calorie limit? "))
        break # Exit loop if input is a valid number
    except ValueError:
        print("Invalid input. Please enter a whole number for your limit.")

# --- End of Task 3 ---

#  Print the results to check if it's working
print(f"\nTotal Calories: {total_calories}")
print(f"Average Calories: {average_calories:.2f}") # Formats to 2 decimal places
print(f"Daily Limit: {daily_limit}")
print(f"Total vs. Limit: {total_calories} / {daily_limit}")
# --- Task 4: Exceed Limit Warning System ---

# Compare the total calories to the daily limit
if total_calories > daily_limit:
    print("\n---------------------------------------------")
    print("   WARNING: You have exceeded your daily limit!   ")
    print(f"   You are {total_calories - daily_limit} calories over.")
    print("---------------------------------------------")
else:
    print("\n---------------------------------------------")
    print("   SUCCESS: You are within your daily limit.   ")
    print(f"   You have {daily_limit - total_calories} calories remaining.")
    print("---------------------------------------------")

# --- End of Task 4 ---
# --- Task 5: Neatly Formatted Output ---

print("\n\n--- Your Daily Calorie Report ---")

# Print the header for the table
# \t is a 'tab' character to create space
print("Meal Name\t\tCalories")
print("---------------------------------")

# Loop through the lists and print each meal
# We use zip() to loop through both lists at the same time
for name, calories in zip(meal_names, meal_calories):
    # {name:<15} adds padding to the right of the name
    # \t adds a tab before the calories
    print(f"{name:<15}\t{calories}")

print("---------------------------------")

# Print the final calculations
# {<15} is used again to align 'Total:' and 'Average:'
print(f"{'Total:':<15}\t{total_calories}")
print(f"{'Average:':<15}\t{average_calories:.2f}")

print("=================================")

# --- End of Task 5 ---

# --- Task 6 (Bonus): Save Session Log to File ---

# Ask the user if they want to save
# .lower() converts "Y" or "Yes" to "y" or "yes"
save_choice = input("\nDo you want to save this report to a file? (y/n): ").lower()

if save_choice == 'y' or save_choice == 'yes':
    # Get the current timestamp
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S") # Formats as "YYYY-MM-DD HH:MM:SS"
    
    # Use 'with open' to safely open and close the file
    # 'w' mode means 'write' (it will overwrite the file if it exists)
    try:
        with open("calorie_log.txt", "w") as f:
            # Write timestamp
            f.write(f"--- Calorie Log for: {timestamp} ---\n\n")
            
            # Write meal details
            f.write("Meal Name\t\tCalories\n")
            f.write("---------------------------------\n")
            for name, calories in zip(meal_names, meal_calories):
                f.write(f"{name:<15}\t{calories}\n")
            
            # Write summary
            f.write("---------------------------------\n")
            f.write(f"{'Total:':<15}\t{total_calories}\n")
            f.write(f"{'Average:':<15}\t{average_calories:.2f}\n")
            f.write(f"Daily Limit:\t{daily_limit}\n\n")
            
            # Write the limit status
            if total_calories > daily_limit:
                f.write(f"STATUS: Exceeded limit by {total_calories - daily_limit} calories.\n")
            else:
                f.write(f"STATUS: Within limit. {daily_limit - total_calories} calories remaining.\n")
            
        print(f"\nSuccessfully saved report to 'calorie_log.txt'")
        
    except IOError:
        print("\nError: Could not write to file. Please check permissions.")

else:
    print("\nReport not saved. Exiting.")

print("\n--- Thank you for using the Calorie Tracker! ---")

# --- End of Project ---