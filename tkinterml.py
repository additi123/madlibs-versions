import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("Madlibs")
label = tk.Label(root, text="Madlibs!", font=('Arial', 20))
label.pack(padx=20, pady=20)

instruction = tk.Label(root, text="Click any of the stories: ", font=('Arial', 15))
instruction.place(x=40, y=65)

def madlib_queen():
    thing = input("Enter thing: ")
    place = input("Enter a place: ")
    adverb = input("Enter a adverb ending with ly: ")
    clothing = input("Enter a clothing: ")
    adjective = input("Enter a adjective: ")
    things = input("Enter things (plural): ")
    adjective1 = input("Enter another adjective: ")
    place1 = input("Enter another place: ")
    phrase = input("Enter a phrase/lyrics/saying: ")


    print("Today I met the Queen of "+ place1 + " during a quick trip to "+ place + "." )
    print("I had left the hosue beacuse I really needed to pick up a dozen "+ adjective1)
    print( clothing + "  in order to repair my "+ things + ".")
    print( "I wasn't planning on meeting her or I probably wouldn't have worn my " + adjective + " " + clothing + ".")
    print("I know most people would have bowed, but I forgot and decided to " + verb + " " + adverb + " instead.")
    print('She smiled politely and then said, "' + phrase + '". '  )


def madlib_butterflies():
    things = input("Enter things (plural): ")
    insect = input("Enter a insect: ")
    verb = input("Enter a verb: ")
    phrase = input("Enter a phrase/lyrics/saying: ")
    colour = input("Enter a colour: ")
    adjective = input("Enter a adjective: ")
    food = input("Enter a food: ")
    person = input("Enter a person: ")
    adjective1 = input("Enter another adjective: ")
    place = input("Enter a place: ")

    print (" Last night I dreamed I was a " + adjective1)
    print( " butterfly with colour splotches that looked like things.")
    print(" I flew to place with my best friend, " + person + ", who was a " + adjective + " insect")
    print ("We ate some food when we got there and then decided to" + verb + ". ")
    print("The dream ended when I said, " + '"'+ phrase +'". ')

def madlib_gingerbread():
    place = input("Enter a place: ")
    adjective = input("Enter a adjective: ")
    verb = input("Enter a verb: ")
    food = input("Enter a food: ")
    things = input("Enter things (plural): ")
    profession = input("Enter a profesion: ")
    thing = input("Enter a thing: ")
    colour = input("Enter a colour: ")
    celebrity = input("Enter a celebrity: ")
    animal = input("Enter a animal: ")

    print("There once was a gingerbread man who had two " + things)
    print(" for eyes and a " + food + " for a nose.")
    print('He always said, "' + verb + 'as fast as you can, you can\'t catch me I\'m the gingerbread man."')
    print("One day he ran past a " + adjective + " " +  profession + " , but they couldn't catch him.")
    print("He kept running until he passed a " + animal + ", but they couldn't catch him either.")
    print("Suddenly, he came across a river near " + place + ".")
    print("How would he cross? Then he saw a " + colour + " " + thing + " floating by.")
    print("He jumped on it, but it was actually " + celebrity + "--who just so happened to love cookies :))")





story1 = tk.Button(root, text="Queen", bg='blue', height=2, width=35, command=madlib_queen, font=('Arial', 15))
story1.place(x=55, y=100)

story2 = tk.Button(root, text="Gingerbread Man", bg='yellow', height=2, width=35, command=madlib_gingerbread, font=('Arial', 15))
story2.place(x=55, y=200)

story3 = tk.Button(root, text="Butterflies", bg='red', height=2, width=35, command=madlib_butterflies, font=('Arial', 15))
story3.place(x=55, y=300)


root.mainloop()