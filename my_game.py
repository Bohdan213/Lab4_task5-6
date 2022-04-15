class Hero:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def set_conversation(self, conversation):
        self.enemies_conv = conversation

    def talk(self):
        print(self.enemies_conv)

    def describe(self):
        print(self.description)

class Friend(Hero):

    def __init__(self, name, description):
        super().__init__(name, description)
        self.__issue = None
        self.__answer = None
        self.__present = None

    @property
    def issue(self):
        return self.__issue

    @issue.setter
    def issue(self, issue):
        self.__issue = issue

    @property
    def answer(self):
        return self.__answer

    @answer.setter
    def answer(self, answer):
        self.__answer = answer

    @property
    def present(self):
        return self.__present

    @present.setter
    def present(self, present):
        self.__present = present

    def gift(self):
        return self.present

    def status(self):
        return "friend"

class Enemy(Hero):
    defeated = 0
    def __init__(self, name, description):
        super().__init__(name, description)
        self.__enemies_weakness = None

    @property
    def enemies_weakness(self):
        return self.__enemies_weakness

    @enemies_weakness.setter
    def enemies_weakness(self, weakness):
        self.__enemies_weakness = weakness

    def fight(self, tool):
        if self.enemies_weakness == tool:
            return True
        return False

    def status(self):
        return "enemy"

class Item:
    def __init__(self, item):
        self.item = item


    def is_helpful(self):
        return isinstance(self, Helpful_Item)

    def get_name(self):
        return self.item

class Helpful_Item(Item):

    def __init__(self, item):
        super().__init__(item)

    def set_description(self, description):
        self.description = description

    def describe(self):
        print(self.description)

class Unhelpful_Item(Item):

    def __init__(self, item):
        super().__init__(item)
        self.description = None

    def set_description(self, description):
        self.description = description

    def describe(self):
        print(self.description)

class Street:
    def __init__(self, street):
        self.street = street
        self.links = dict()
        self.street_character = None
        self.street_item = None

    def set_description(self, street_description):
        self.street_descr = street_description

    def link_room(self, street, link):
        self.links[link] = street

    def set_character(self, enemy):
        self.street_character = enemy

    def set_item(self, item):
        self.street_item = item

    def get_details(self):
        a = f'{self.street}\n--------------------\n{self.street_descr}\n'
        for i in self.links.keys():
            a += f'The {self.links[i].street} is {i}\n'
        print(a)

    def get_character(self):
        return self.street_character

    def get_item(self):
        return self.street_item

    def move(self, link):
        if link in self.links:
            return self.links[link]
        else:
            print(f"The are not way on {link}.")
            return self
