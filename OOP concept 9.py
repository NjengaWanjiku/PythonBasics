# class keyword
# indented to the right
# should be in title case
class building():
    rooms=6
    windows=8
    doors=5
    garage=True
    lawn =True
    windows=10
    swimming_pool=False

    # method should be inside a class;a function inside a class
    def open_bilding(self):
        # print("This building is now open")
        # print(f"{} is now open")
        print(f"{self.name} is now open")

    def close_building(self):
        print("This building is now closed")

    def vacant_rooms(self):
        vacant = self.rooms-self.occupied
        print(vacant," empty rooms")
# namespace is a list of variable identifiers

def open_door(door_number):
    print(f"door_number{door_number} opened")

jamii=building.doors
print(jamii)


# class
cornerhouse=building()
cornerhouse.rooms=100
print(cornerhouse.rooms)
cornerhouse.securityguards=12
print(cornerhouse.securityguards)
cornerhouse.name="shaka"
print(cornerhouse.name)
cornerhouse.open_bilding()
cornerhouse.close_building()
cornerhouse.occupied=42
print(cornerhouse.occupied)
print(cornerhouse.vacant_rooms())

kimathihouse=building()
# calls object
kimathihouse.rooms=150
print(kimathihouse.rooms)
kimathihouse.basement=True
print(kimathihouse.basement)
kimathihouse.securityguards=8
# assigning specific attribute
print(kimathihouse.securityguards)
kimathihouse.name="roses"
print(kimathihouse.name)
kimathihouse.open_bilding()
kimathihouse.close_building()
kimathihouse.occupied=100