#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("/Users/j9yim/Documents/Coding/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter:
    content = letter.read().strip()  # Read the letter content once

with open("/Users/j9yim/Documents/Coding/Mail Merge Project Start/Input/Names/invited_names.txt") as names:
    for name in names:
        message = content.replace("[name]", name.strip())  # Replace [name] with the current name
        with open(f"/Users/j9yim/Documents/Coding/Mail Merge Project Start/Output/ReadyToSend/{name}.txt", mode = 'w') as file:
            file.write(message)
