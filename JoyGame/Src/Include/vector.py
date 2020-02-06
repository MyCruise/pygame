from math import sqrt, atan, atan2


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __self__(self):
        print("(%d, %d)" % (self.x, self.y))

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2(self.x * other.x, self.y * other.y)

    def __div__(self, other):
        return Vector2(self.x / other.x, self.y / other.y)

    def list2vector(self, list1):
        return Vector2(list1[0], list1[1])

    def from_point(self, p1, p2):
        return Vector2(p1[0] - p2[0], p1[1] - p2[1])

    def returnTuple(self, vector):
        ret = (vector.x, vector.y)
        return ret

    def returnRectTuple(self, p1, p2):
        ret = (p1.x, p1.y, p2.x, p2.y)
        return ret

    def getMagnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def angle(self, p1, p2):
        return atan2(p1.y - p2.y, p1.x - p2.x)

    def changeAngle(self, center, point, angle):
        pass


class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __self__(self):
        print("(%d, %d, %d)" % (self.x, self.y, self.z))

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)

    def __div__(self, other):
        return Vector3(self.x / other.x, self.y / other.y, self.z / other.z)

    def from_point(self, p1, p2):
        return Vector3(p1[0] - p2[0], p1[1] - p2[1], p1[2] - p2[2])

    def get_magnitude(self):
        return sqrt(sqrt(self.x ** 2 + self.y ** 2) ** 2 + sqrt(self.x ** 2 + self.z ** 2) ** 2)


if __name__ == '__main__':
    print(Vector3.__add__(Vector3(1, 2, 2), Vector3(1, 2, 2)).__self__())
