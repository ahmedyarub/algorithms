import threading


class TrafficLight:
    def __init__(self):
        self.lock = threading.Lock()
        self.greenOnA = True

    def carArrived(
            self,
            carId: int,  # ID of the car
            roadId: int,  # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
            direction: int,  # Direction of the car
            turnGreen: 'Callable[[], None]',  # Use turnGreen() to turn light to green on current road
            crossCar: 'Callable[[], None]'  # Use crossCar() to make car cross the intersection
    ) -> None:
        with self.lock:
            if (roadId == 1 and not self.greenOnA or roadId == 2 and self.greenOnA):
                turnGreen()
                self.greenOnA = not self.greenOnA
            crossCar()
