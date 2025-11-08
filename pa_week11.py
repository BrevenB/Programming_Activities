# 1.) Create and Display a list of your 3 favorite colors
colors = ["Red", "White", "Blue"]

fav_colors = "My Favorite Colors are: "

# Convert the list to a comma separated string using join()
color_string += ", ".join(colors)

print(fav_colors)



# 2.) Asks the user to enter their address
address = input("Enter your address: ")
address.strip()

# Use the isalnum() function to verify the entered a valid address, replace non alphanumeric characters
address = address.replace(" ", "")
address = address.replace(".", "")
address = address.replace(",", "")
print("address:", address, address.isalnum())
