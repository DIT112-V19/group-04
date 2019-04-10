import vehicle
import coordinate

startingPoint = coordinate.Coordinate(0, 0)
car = vehicle.Vehicle("Car 1", startingPoint, 0.0)

print(car.__dict__)
car.whereToDrive(coordinate.Coordinate(-3, 5))
print(car.__dict__)
car.whereToDrive(coordinate.Coordinate(4, 7))
print(car.__dict__)
car.whereToDrive(coordinate.Coordinate(9, 3))
print(car.__dict__)
car.whereToDrive(coordinate.Coordinate(9, 0))
print(car.__dict__)
car.whereToDrive(coordinate.Coordinate(1, 7))
print(car.__dict__)
car.whereToDrive(coordinate.Coordinate(4, 8))
print(car.__dict__)
car.whereToDrive(coordinate.Coordinate(3, 9))
print(car.__dict__)


