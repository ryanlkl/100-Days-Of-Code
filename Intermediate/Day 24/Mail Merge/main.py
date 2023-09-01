#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

# Hint 1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint 2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint 3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("Day 24\\Mail Merge\\Input\\Names\\invited_names.txt","r") as names_file:
    names = names_file.read()
    names = names.split("\n")

with open("Day 24\\Mail Merge\\Input\\Letters\\starting_letter.txt","r") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        new_letter = letter_contents.replace(PLACEHOLDER,name)
        with open(f"Day 24\\Mail Merge\\Output\\ReadyToSend\\letter_for_{name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
