from vehicle import Car
import argparse
import sys

if sys.version_info[0] == 2:
    input = raw_input


class ParkingLot:
    def __init__(self):
        self.capacity = 0
        self.slotid = 0
        self.numOfOccupiedSlots = 0

    def createParkingLot(self, capacity):
        self.slots = [-1] * capacity
        self.capacity = capacity
        return self.capacity

    def getEmptySlot(self):
        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                return i

    def park(self, registrationNumber, driverAge):
        if self.numOfOccupiedSlots < self.capacity:
            slotid = self.getEmptySlot()
            self.slots[slotid] = Car(registrationNumber, driverAge)
            self.slotid = self.slotid+1
            self.numOfOccupiedSlots = self.numOfOccupiedSlots + 1
            return slotid+1
        else:
            return -1

    def leave(self, slotid):

        if self.numOfOccupiedSlots > 0 and self.slots[slotid-1] != -1:
            self.slots[slotid-1] = -1
            self.numOfOccupiedSlots = self.numOfOccupiedSlots - 1
            return True
        else:
            return False

    def status(self):
        print("Slot No.\tRegistration No.\tDriver age")
        for i in range(len(self.slots)):
            if self.slots[i] != -1:
                print(str(i+1) + "\t\t" +
                      str(self.slots[i].registrationNumber) + "\t\t" + str(self.slots[i].driverAge))
            else:
                continue

    def getRegNoFromDriverAge(self, driverAge):

        registrationNumbers = []
        for i in self.slots:

            if i == -1:
                continue
            if i.driverAge == driverAge:
                registrationNumbers.append(i.registrationNumber)
        return registrationNumbers

    def getSlotNoFromRegNo(self, registrationNumber):

        for i in range(len(self.slots)):
            if self.slots[i] != -1 and self.slots[i].registrationNumber == registrationNumber:
                return i+1
            else:
                continue
        return -1

    def getSlotNoFromDriverAge(self, driverAge):
        slotnos = []
        for i in range(len(self.slots)):

            if self.slots[i] == -1:
                continue
            if self.slots[i].driverAge == driverAge:
                slotnos.append(str(i+1))
        return slotnos

    def show(self, line):
        if line.startswith('Create_parking_lot'):
            n = int(line.split(' ')[1])
            res = self.createParkingLot(n)
            print('Created a parking lot with '+str(res)+' slots')

        elif line.startswith('Park'):
            registrationNumber = line.split(' ')[1]
            driverAge = line.split(' ')[3]
            res = self.park(registrationNumber, driverAge)
            if res == -1:
                print("Sorry, parking lot is full")
            else:
                print('Allocated slot number: '+str(res))

        elif line.startswith('leave'):
            leave_slotid = int(line.split(' ')[1])
            status = self.leave(leave_slotid)
            if status:
                print('Slot number '+str(leave_slotid)+' is free')

        elif line.startswith('status'):
            self.status()

        elif line.startswith('Vehicle_registration_number_for_driver_of_age'):
            driverAge = line.split(' ')[1]
            registrationNumbers = self.getRegNoFromDriverAge(driverAge)
            print(', '.join(registrationNumbers))

        elif line.startswith('Slot_numbers_for_driver_of_age'):
            driverAge = line.split(' ')[1]
            slotnos = self.getSlotNoFromDriverAge(driverAge)
            print(', '.join(slotnos))

        elif line.startswith('Slot_number_for_car_with_number'):
            registrationNumber = line.split(' ')[1]
            slotno = self.getSlotNoFromRegNo(registrationNumber)
            if slotno == -1:
                print("Not found")
            else:
                print(slotno)
        elif line.startswith('exit'):
            exit(0)


def main():

    parkinglot = ParkingLot()
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action="store", required=False,
                        dest='src_file', help="Input File")
    args = parser.parse_args()

    if args.src_file:
        with open(args.src_file) as f:
            for line in f:
                line = line.rstrip('\n')
                parkinglot.show(line)
    else:
        while True:
            line = input("$ ")
            parkinglot.show(line)


if __name__ == '__main__':
    main()
