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
print("First Train:\n")
print(train)
print(Border)

#                New       After
train.add_after(gondola, box_cart)
train.add_before(hopper, gondola)
train.remove_carriage(box_cart)
print("First Train carriage count after adding after and add before method is called: "+str(train.get_carriage_count()))
# Output should be 3
print(Border)


# Second train
second_train = TrainLinkedList()
box_cart1 = BoxCar(50, 200)
box_cart1.add_cargo('Food', 30)
cistern1 = Cistern(10, 250)
gondola1 = Gondola(15, 350)
cistern1.add_cargo('Oil', 30)
gondola1.add_cargo('Coal', 21)

second_train.add_first(box_cart1)
second_train.add_last(gondola1)
#                       New        After
second_train.add_after(cistern1, box_cart1)

train_manager = TrainManager()
train_manager.add_train(train)
train_manager.add_train(second_train)
print(train_manager.avg_mean_carriages())
print(train_manager.std_carriage())
#
#
# train_manager.export_as_json('temp.json')
