# Basics Assignment Week2

year_input = input("How many years:")
year_int = int(year_input)

second = year_int*365*24*60*60

birth = second/7
death = second/13
immigrant = second/35
current_pop = 307357870

population = birth - death + immigrant + current_pop

print("There will be ", population, "people after", year_input,"years")