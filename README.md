# super-taxi
Simple api for taxi booking

## Dependencies
- [Flask](https://github.com/pallets/flask)

## Installing

```sh
pip install super-taxi-api==0.0.1
```
To install test package
```sh
pip install -i https://test.pypi.org/simple/ super-taxi==0.0.2
```

## Running
Execute below in terminal
```sh
super-taxi-api
```

### APIs

Rest apis for book a taxi

#### `POST /api/book`

Pick the nearest available car to the customer location and return the total time taken to travel from the current car location to customer location then to customer destination.

- Request payload
```json
{
  "source": {
    "x": 0,
    "y": 0
  },
  "destination": {
    "x": 2,
    "y": 3
  }
}
```

- Response payload
```json
{
  "car_id": 1,
  "total_time": 10
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