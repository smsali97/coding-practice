import heapq
from collections import defaultdict
class Apartment:
    def __init__(self, apt_number, num_rooms):
        self.apt_number = apt_number
        self.num_rooms = num_rooms
        self.unassigned_rooms = num_rooms

    def __lt__(self, apt):
        return self.num_rooms <= apt.num_rooms

class Person :
    def __init__(self, name, wants_housemates):
        self.name = name
        self.wants_housemates = wants_housemates

    def __lt__(self, person):
        return self.wants_housemates <= person.wants_housemates


def assignApartments(apts, people):
    assignments = defaultdict(list)

    single_room_apts = [apt for apt in apts if apt.num_rooms == 1]
    multi_room_apts = [apt for apt in apts if apt.num_rooms > 1]
    multi_room_apts.sort(reverse=True)
    single_preference_person = [person for person in people if person.wants_housemates == 0]
    multi_preference_person = [person for person in people if person.wants_housemates == 1]

    #Assign single rooms
    single_preference_person_pointer = 0 #single_preference_person_pointer
    apt_single_room = 0
    while apt_single_room < len(single_room_apts) and single_preference_person_pointer < len(single_preference_person) :
        assignments[single_room_apts[apt_single_room].apt_number].append(single_preference_person[single_preference_person_pointer].name)
        single_room_apts[apt_single_room].unassigned_rooms -= 1
        single_preference_person_pointer += 1
        apt_single_room += 1

    #Assign multi rooms
    multi_preference_person_pointer = 0 #multi_preference_person_pointer
    apt_multi_room = 0
    while apt_multi_room < len(multi_room_apts) and multi_preference_person_pointer < len(multi_preference_person) :
        assignments[multi_room_apts[apt_multi_room].apt_number].append(multi_preference_person[multi_preference_person_pointer].name)
        multi_preference_person_pointer += 1
        multi_room_apts[apt_multi_room].unassigned_rooms -= 1
        if multi_room_apts[apt_multi_room].unassigned_rooms == 0:
            apt_multi_room += 1

    #Now provide single rooms to multi_preference_person
    while multi_preference_person_pointer < len(multi_preference_person) and apt_single_room < len(single_room_apts):
        assignments[single_room_apts[apt_single_room].apt_number].append(multi_preference_person[multi_preference_person_pointer].name)
        multi_preference_person_pointer += 1
        single_room_apts[apt_single_room].unassigned_rooms -= 1
        apt_single_room += 1

    #Now provide multi rooms to single_preference_person
    while single_preference_person_pointer < len(single_preference_person) and apt_multi_room < len(multi_room_apts):
        assignments[multi_room_apts[apt_multi_room].apt_number].append(single_preference_person[single_preference_person_pointer].name)
        single_preference_person_pointer += 1
        multi_room_apts[apt_multi_room].unassigned_rooms -= 1
        if multi_room_apts[apt_multi_room].unassigned_rooms == 0:
            apt_multi_room += 1

    return assignments


people = []
apts = []

apt1 = Apartment(101, 1)
apt2 = Apartment(102, 2)
apt3 = Apartment(103, 3)


apts.append(apt1)
apts.append(apt2)
apts.append(apt3)
#apts.append(apt4)


person1 = Person("Jean", 1)
person2 = Person("xyz", 1)
person3 = Person("Jeann", 0)
person4 = Person("abcd", 0)
person5 = Person("abcs", 1)
person6 = Person("abcds", 1)

people.append(person1)
people.append(person2)
people.append(person3)
people.append(person4)
people.append(person5)
people.append(person6)

print(assignApartments(apts, people))