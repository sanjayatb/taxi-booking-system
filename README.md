# super-taxi-api
Simple api for taxi booking named as super-taxi

## Dependencies
- [Flask](https://github.com/pallets/flask)

## Installing
To install the api execute below command
```sh
pip install super-taxi-api
```
If you want to install from test org, for development mode use below
```sh
pip install -i https://test.pypi.org/simple/ super-taxi-api
```

## Running
To run with rest api tick option which update system service time,
Execute below in terminal to start the api
```sh
super-taxi-api
```
To run with system clock enable. This will internally start a clock which update the time tick
```sh
super-taxi-api --clock
```

### APIs

Rest apis for book a taxi. All cars starts at (0,0) position of the map

#### `POST /api/book`

Pick the nearest available car to the customer location and return the total time taken to travel from the current car location to customer location then to customer destination.

- Request payload
```json
{
  "source": {
    "x": 1,
    "y": 0
  },
  "destination": {
    "x": 1,
    "y": 1
  }
}
```

- Response payload
```json
{
  "car_id": 1,
  "total_time": 2
}
```
- All car are available initially, and become booked once it is assigned to a customer. It will remain booked until it reaches its destination, and immediately become available again.
- In the event that there are more than one car near the customer location, your service should return the car with the smallest id.
- Only one car be assigned to a customer, and only one customer to a car.
- Cars can occupy the same spot, e.g. car 1 and 2 can be at point (1, 1) at the same time.
- If there is no available car that can satisfy the request, your service should return an empty response, not an error

#### `POST /api/tick`
Advance service time by 1 time unit

#### `PUT /api/reset` 
reset all cars data back to the initial state regardless of cars that are currently booked.


For test the service use [basic_solution_checker.py](basic_solution_checker.py)
```python
python3 basic_solution_checker.py
```