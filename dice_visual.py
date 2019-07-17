import pygal
from die import Die

sides_1 = 6
sides_2 = 6
rolls = 100000

# Create two dice.
die_1 = Die(sides_1)
die_2 = Die(sides_2)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(rolls):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
all_results = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    all_results.append(value)
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = f"Results of rolling a D{sides_1} and a D{sides_2} {rolls:,} times."
hist.x_labels = all_results
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add(f'D{sides_1} + D{sides_2}', frequencies)
hist.render_to_file('dice_visuals.svg')
