# Function to generate combinations and write to a file
def generate_combinations_and_write_to_file(filename="combinations.txt"):
    combinations = []
    
    # Loop through tens and ones digits
    for tens in range(10):
        for ones in range(10):
            # Convert digits to string and concatenate with prefix and suffix
            combination = "MAYA" + str(tens) + str(ones) + "24"
            combinations.append(combination)
    
    # Write combinations to a file
    with open(filename, 'w') as file:
        for i, combination in enumerate(combinations, start=1):
            file.write(f"{combination}\n")

# Generate combinations and write to file
generate_combinations_and_write_to_file()
