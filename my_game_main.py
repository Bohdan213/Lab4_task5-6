import my_game

Kozelnicka = my_game.Street("Kozelnicka st.")
Kozelnicka.set_description("Welcome to UCU, destroy the final enemy")

Ivana_Franka = my_game.Street("Ivana Franka st.")
Ivana_Franka.set_description("What a beautiful Stryiskyi park!!!")

Yaroslavenka = my_game.Street("Yaroslavenka st.")
Yaroslavenka.set_description("Long silent street")

Panasa_Mirnogo = my_game.Street("Panasa Mirnogo st.")
Panasa_Mirnogo.set_description("Pretty good street")

Ugorska = my_game.Street("Ugorska st.")
Ugorska.set_description("Very busy street")

Ugorska.link_room(Panasa_Mirnogo, "west")
Panasa_Mirnogo.link_room(Ugorska, "east")
Ugorska.link_room(Yaroslavenka, "north")
Yaroslavenka.link_room(Ugorska, "south")
Yaroslavenka.link_room(Ivana_Franka, "west")
Ivana_Franka.link_room(Yaroslavenka, "east")
Panasa_Mirnogo.link_room(Kozelnicka, "west")
Kozelnicka.link_room(Panasa_Mirnogo, "east")
Ivana_Franka.link_room(Kozelnicka, "south")
Kozelnicka.link_room(Ivana_Franka, "north")

Bob = my_game.Friend("Bob", "A little boy")
Bob.set_conversation("What's bro. How are you?")
Bob.present = "pellet gun"
Bob.issue = "Can you count 2+2*2?"
Bob.answer = "6"
Ugorska.set_character(Bob)
print(Bob.status())

Librarian = my_game.Friend("Librarian", "A very kind librarian")
Librarian.set_conversation("Nice to meet you.")
Librarian.present = "book"
Librarian.issue = "Do you the number of faculties in UKU for bachelors?"
Librarian.answer = "5"
Yaroslavenka.set_character(Librarian)

Orc = my_game.Enemy("Orc", "Orc which Smell to bad")
Orc.set_conversation("Eeee...Org...EEEE, I'm hate books")
Orc.enemies_weakness = "book"
Panasa_Mirnogo.set_character(Orc)
print(Orc.enemies_weakness)

Knight = my_game.Enemy("Knight", "Knight in armor")
Knight.set_conversation("Prepare for battle, only with swords!")
Knight.enemies_weakness = "pellet gun"
Ivana_Franka.set_character(Knight)

Ktulhu = my_game.Enemy("Ktulhu", "Ouuuu, it is Ktulhu")
Ktulhu.set_conversation("You will die")
Ktulhu.enemies_weakness = "pikestaff"
Kozelnicka.set_character(Ktulhu)


pikestaff = my_game.Helpful_Item("pikestaff")
pikestaff.set_description("A large staff against monsters")
Ivana_Franka.set_item(pikestaff)

cheese = my_game.Unhelpful_Item("cheese")
cheese.set_description("A large piece of cheese")
Panasa_Mirnogo.set_item(cheese)

current_street = Ugorska
backpack = []

dead = False

while dead == False:

    print("\n")
    current_street.get_details()

    inhabitant = current_street.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_street.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        try:
            if inhabitant.status() == "enemy" and current_street.move(command).get_character().status == "enemy":
                print("Firstly win the enemy")
            else:
                current_street = current_street.move(command)
        except:
            current_street = current_street.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None:
            if inhabitant.status() == "friend":
                print("No fight with friend")
            else:
                print("What will you fight with?")
                print(backpack)
                fight_with = input()
                if fight_with in backpack:
                    if inhabitant.fight(fight_with) == True:
                        print("Hooray, you won the fight")
                        current_street.set_character(None)
                        print("cool")
                        if inhabitant.name == "Ktulhu":
                            print("You win the game!!!")
                            exit()
                    else:
                        print("Oh dear, you lost the fight.")
                        print("That's the end of the game")
                        dead = True
                else:
                    print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "gift":
        if inhabitant.status() == "enemy":
            print("No gift from enemy")
        else:
            if inhabitant.issue is not None:
                print(inhabitant.issue)
                answer = input()
                if inhabitant.answer == answer:
                    backpack.append(inhabitant.gift())
                    print(f"Congratulation, your gift is {inhabitant.present}")
                    inhabitant.present = None
                    inhabitant.issue = None
                else:
                    print("Wrong!\nTry again!")
            else:
                print("You received the gift earlie")
    elif command == "take":
        if item is not None:
            if current_street.get_character() is None:
                if item.is_helpful():
                    print("It's helpful item, you lucky!!!\nYou put the " + item.get_name() + " in your backpack")
                    backpack.append(item.get_name())
                    current_street.set_item(None)
                else:
                    print("It's unhelpful item, you unlucky:(")
            else:
                print("Firstly win the enemy")
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)