class Enemy:
    defeated = 0
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def set_conversation(self, conversation):
        self.enemies_conv = conversation

    def set_weakness(self, weakness):
        self.enemies_weakness = weakness

    def describe(self):
        print(self.description)

    def talk(self):
        print(self.enemies_conv)

    def get_defeated(self):
        return self.get_count_win()

    def fight(self, tool):
        if self.enemies_weakness == tool:
            self.count_win()
            return True
        return False

    @classmethod
    def count_win(cls):
        cls.defeated += 1

    @classmethod
    def get_count_win(cls):
        return cls.defeated

class Item:
    def __init__(self, item):
        self.item = item

    def set_description(self, description):
        self.description = description

    def describe(self):
        print(self.description)

    def get_name(self):
        return self.item


class Room:
    def __init__(self, room):
        self.room = room
        self.links = dict()
        self.room_character = None
        self.room_item = None

    def set_description(self, room_description):
        self.room_descr = room_description

    def link_room(self, room, link):
        self.links[link] = room

    def set_character(self, enemy: Enemy):
        self.room_character = enemy

    def set_item(self, item):
        self.room_item = item

    def get_details(self):
        a = f'{self.room}\n--------------------\n{self.room_descr}\n'
        for i in self.links.keys():
            a += f'The {self.links[i].room} is {i}\n'
        print(a)

    def get_character(self):
        return self.room_character

    def get_item(self):
        return self.room_item

    def move(self, link):
        if link in self.links:
            return self.links[link]
        else:
            return self
