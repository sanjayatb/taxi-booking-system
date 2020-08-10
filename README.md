## super-taxi
Simple api for taxi booking

## Dependencies
- [Flask](https://github.com/pallets/flask)

## Installing

```sh
pip install super-taxi
```

### APIs

Rest apis for book a taxi

#### `POST /api/book`

Your system should pick the nearest available car to the customer location and return the total time taken to travel from the current car location to customer location then to customer destination.

- Request payload
```json
{
  "source": {
    "x": x1,
    "y": y1
  },
  "destination": {
    "x": x2,
    "y": y2
  }
}
```

- Response payload
```json
{
  "car_id": id,
  "total_time": t
}
```
- All car are available initially, and become booked once it is assigned to a customer. It will remain booked until it reaches its destination, and immediately become available again.
- In the event that there are more than one car near the customer location, your service should return the car with the smallest id.
- Only one car be assigned to a customer, and only one customer to a car.
- Cars can occupy the same spot, e.g. car 1 and 2 can be at point (1, 1) at the same time.
- If there is no available car that can satisfy the request, your service should return an empty response, not an error

#### `POST /api/tick`

To facilitate the review of this exercise, your service should expose /api/tick REST endpoint, when called should advance your service time stamp by 1 time unit.

#### `PUT /api/reset` 
Your service should also provide /api/reset REST endpoint, when called will reset all cars data back to the initial state regardless of cars that are currently booked.


Run the test cases in the file [basic_solution_checker.py](basic_solution_checker.py) to check whether your API works correctly
```python
python3 basic_solution_checker.py
```