# ParkingLot
Dependencies Needed
1. It is python3 compatible. Install dependency from here https://www.python.org/downloads/ 

Description: 
This parking lot design takes greedy approach to park the cars.
1. Create_parking_lot N : Create a parking lot with the given capacity.
2. Park KA-01-HH-1234 driver_age X : Parks the car in the nearest emoty slot. If all the slots are full it shows a message corresponding to that.
3. Slot_numbers_for_driver_of_age X : Returns the list of slot number where driver age == X
4. Slot_number_for_car_with_number PB-01-HH-1234 : Returns the slot number corresponding to given Registration no.
5. Leave Y : Remove vehicle from this slot. 
6. Vehicle_registration_number_for_driver_of_age X: Returns the list of Registration No where driver age == X

Test cases are added to test all the above 6 functionality in testCases.py using unittest module.

Setup to run:
1. Clone this repo.
2. Use command ```python parkingLot.py ```. It opens a shell where you can test the above functionalities.
3. Use command python parkingLot -f input.txt to run with the help of text file.
4. Use command python testCases.py to run the test cases.


