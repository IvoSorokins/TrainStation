from BoxCar import BoxCar
from Cistern import Cistern
from Gondola import Gondola
from Hopper import Hopper
from TrainLinkedList import TrainLinkedList
from TrainManager import TrainManager


train = TrainLinkedList()

Border = ('\033[33m'+"================================================================================================="
                     "========" + '\033[0m')  # Just for visuals

# First train

box_cart = BoxCar(tare=10, length=200)
cistern = Cistern(tare=10, length=250)
gondola = Gondola(tare=15, length=350)
hopper = Hopper(tare=20, length=120)

# Adding cargo to Carriages
box_cart.add_cargo('Cattle', 20)
cistern.add_cargo('Oil', 15)
hopper.add_cargo('Sand', 20)
gondola.add_cargo('Coal', 20)

# Carriage print out
print(Border+"\nFirst Train Carriages:\n")

print(box_cart)
print(cistern)
print(hopper)
print(gondola)

print(Border)


train.add_first(box_cart)
train.add_last(cistern)


#                New       After
train.add_after(gondola, box_cart)
train.add_before(hopper, gondola)
train.remove_carriage(box_cart)
print("First Train:\n")
print(train)
print(Border)
print("First Train carriage count after adding after and add before method is called: "+str(train.get_carriage_count()))
# Output should be 3
print(Border)


# Second train
second_train = TrainLinkedList()
box_cart1 = BoxCar(50, 200)
cistern1 = Cistern(10, 250)
gondola1 = Gondola(15, 350)
hopper1 = Hopper(30, 200)

box_cart1.add_cargo('Food', 30)
cistern1.add_cargo('Oil', 30)
gondola1.add_cargo('Coal', 21)
hopper1.add_cargo('Sand', 20)


second_train.add_first(box_cart1)
second_train.add_last(gondola1)

#                       New        After
second_train.add_after(cistern1, box_cart1)
second_train.add_before(hopper1, gondola1)
print("Second Train Carriages:\n")

print(box_cart1)
print(cistern1)
print(gondola1)

print(Border)

print("Second Train:\n")
print(second_train)
print(Border)
print("Seconbd Train carriage count after adding first and last: "+str(second_train.get_carriage_count()))
# Output should be 4
print(Border)

train_manager = TrainManager()
train_manager.add_train(train)
train_manager.add_train(second_train)

print("Average Carriages per train: " + str(train_manager.avg_mean_carriages()))
print("STD Formula results: " + str(train_manager.std_carriage(second_train)))
print(Border)


Find_by_id = "BC-1"  # Enter ID for carriage you want to find
which_train = second_train  # Enter for which train
print("Carriage with id of "+Find_by_id+": "+str(which_train.find_carriage_by_id(Find_by_id)))
print(Border)

add_json = "add_json"  # Name of file to import
output_json = "json_output"  # Name of the file to output

try:
    train_manager.add_trains_from_json(add_json)
    print("JSON file successfully imported.")
except Exception as e:
    print("Error importing from JSON file:", e)

try:
    train_manager.export_as_json(output_json)
    print("JSON file successfully created.")
except Exception as e:
    print("Error creating JSON file:", e)
print(Border + "\nSuccess!")
