class Book:
    def __init__(self, title, author):
        self.tital = title
        self.author = author
    def __str__(self):
        return f"'{self.tital}' by {self.author}"
b = Book("1984" , "George orwell")
print(b)
print()

#Example 2: Song playlist
class Playlist:
    def __init__(self, songs):
        self.songs = songs
    def __len__(self):
        return len(self.songs)
    def __add__(self, other):
        return Playlist(self.songs + other.songs)
p1 = Playlist(["song1","song2"])
p2 = Playlist(["song3"])
print(len(p1))
print(len(p1 + p2))
print()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __add__(self,other):
        if not isinstance(other, Point):
            return NotImplemented
        return(self.x + other.x, self.y + other.y)
p1 = Point(2 ,5)
p2 = Point(6 , 7)
print(p1 + p2)
