class Circle:
    def __init__(self, center: tuple[int, int], radius: int):
        # an underscore denotes that it's a private field (it still can be accessed tho-it's a convention)
        self._center = center
        self._radius = radius
        self._distance = self.update_distance()

    # traditional getter / setter
    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        self._radius = radius

    # modern getter / setter
    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, center):
        self._center = center
        self._distance = self.update_distance()

    def update_distance(self) -> float:
        x, y = self._center
        return (x**2 + y**2) ** 0.5
    
    @property
    def distance(self):
        return self._distance
