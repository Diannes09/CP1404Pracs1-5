colours = {'AliceBlue': '#ff0f8ff', 'AntiqueWhite': '#faebd7', 'Azure1': '#f0fffff', 'Beige': '#f5f5dc', 'Black': '#0000000', 'Blue2': '#0000ee',
                'CadetBlue1': '#98f5ff', 'DarkOrchard1': '#bf3eff', 'DeepSkyBlue1': '#00bfff', 'Gold1': '#ffd700'}
list_of_colours = colours.keys()
print(list_of_colours)
choice = input("Please choose a colour: ")
if choice in colours.items():
    print(choice, colours[values])

