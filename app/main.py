class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: int,
        clean_power: int,
        average_rating: int,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> int:
        suma = 0
        for car in cars:
            if self.clean_power > car.clean_mark:
                suma += self.wash_single_car(car)
                car.clean_mark = self.clean_power

        return round(suma, 1)

    def calculate_washing_price(self, car: Car) -> int:
        return self.wash_single_car(car)

    def wash_single_car(self, car: Car) -> None:
        clean_deferance = self.clean_power - car.clean_mark
        return (
            car.comfort_class
            * clean_deferance
            * self.average_rating
            / self.distance_from_city_center
        )

    def rate_service(self, rate: int) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rate)
            / (self.count_of_ratings + 1),
            1,
        )
        self.count_of_ratings += 1
