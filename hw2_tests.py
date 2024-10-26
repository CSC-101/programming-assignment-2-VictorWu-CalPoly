import hw2
import unittest
from data import Point, Rectangle, Duration, Song

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle_1(self):
        p1 = Point(2,2)
        p2 = Point(10,10)
        result = hw2.create_rectangle(p1, p2)
        expected = Rectangle(Point(2,10), Point(10,2))
        self.assertEqual(result, expected)

    def test_create_rectangle_2(self):
        p1 = Point(10,5)
        p2 = Point(2,4)
        result = hw2.create_rectangle(p1, p2)
        expected = Rectangle(Point(2,5), Point(10,4))
        self.assertEqual(result, expected)

    def test_create_rectangle_3(self):
        p1 = Point(2,2)
        p2 = Point(2,10)
        result = hw2.create_rectangle(p1, p2)
        expected = Rectangle(Point(2,10), Point(2,2))
        self.assertEqual(result, expected)

    def test_create_rectangle_4(self):
        p1 = Point(2,2)
        p2 = Point(5,2)
        result = hw2.create_rectangle(p1, p2)
        expected = Rectangle(Point(2,2), Point(5,2))
        self.assertEqual(result, expected)

    # Part 2
    def test_duration_1(self):
        d1 = Duration(4,2)
        d2 = Duration(4,5)
        result =  hw2.shorter_duration_than(d1, d2)
        expected = False
        self.assertEqual(result, expected)

    def test_duration_2(self):
        d1 = Duration(10,7)
        d2 = Duration(10,5)
        result =  hw2.shorter_duration_than(d1, d2)
        expected = True
        self.assertEqual(result, expected)

    # Part 3
    def test_songs_1(self):
        song1 = Song('Fuel', 'Shimmer', Duration(3,34))
        song2 = Song('Travis Scott', 'Apple Pie', Duration(3,39))
        song3 = Song('Green Day', 'American Idiot', Duration(3,56))
        song4 = Song('Linkin Park', 'Lost', Duration(3,19))
        list_of_songs = [song1, song2, song3, song4]
        result = hw2.song_shorter_than(list_of_songs, Duration(3,40))
        expected = [song1, song2, song4]
        self.assertEqual(result, expected)

    def test_songs_2(self):
        song1 = Song('The Fray', 'How to Save a Life', Duration(2,34))
        song2 = Song('Hoobastank', 'The Reason', Duration(3,39))
        song3 = Song('Paramore', 'Aint It Fun', Duration(3,56))
        song4 = Song('blink-182', 'All The Small Things', Duration(3,19))
        list_of_songs = [song1, song2, song3, song4]
        result = hw2.song_shorter_than(list_of_songs, Duration(2,35))
        expected = [song1]
        self.assertEqual(result, expected)

    # Part 4
    def test_running_time_1(self):
        song1 = Song('Fuel', 'Shimmer', Duration(3,34))
        song2 = Song('Travis Scott', 'Apple Pie', Duration(3,39))
        song3 = Song('Green Day', 'American Idiot', Duration(3,56))
        song4 = Song('Linkin Park', 'Lost', Duration(3,19))
        result = hw2.running_time([song1, song2, song3, song4], [0,1,2,3,3])
        expected = Duration(17,47)
        self.assertEqual(result, expected)

    def test_running_time_2(self):
        song1 = Song('The Fray', 'How to Save a Life', Duration(2,34))
        song2 = Song('Hoobastank', 'The Reason', Duration(3,39))
        song3 = Song('Paramore', 'Aint It Fun', Duration(3,56))
        song4 = Song('blink-182', 'All The Small Things', Duration(3,19))
        result = hw2.running_time([song1, song2, song3, song4], [0, 1, 2, 2, 0])
        expected = Duration(16, 39)
        self.assertEqual(result, expected)

    # Part 5
    def test_validate_route_1(self):
        result = (hw2.validate_route
        ([['san luis obispo', 'santa margarita'],['san luis obispo', 'pismo beach'],['atascadero', 'santa margarita'],['atascadero', 'creston']],
            ['san luis obispo', 'santa margarita', 'atascadero']))
        expected = True
        self.assertEqual(result, expected)

    def test_validate_route_2(self):
        result = (hw2.validate_route
        ([['san luis obispo', 'santa margarita'],['san luis obispo', 'pismo beach'],['atascadero', 'santa margarita'],['atascadero', 'creston']],
         ['san luis obispo', 'atascadero']))
        expected = False
        self.assertEqual(result, expected)

    # Part 6
    def test_longest_repetition_1(self):
        nums = [1,1,1,2,2,1,1,1,1,3,3,3]
        result = hw2.longest_repetition(nums)
        expected = 5
        self.assertEqual(result, expected)

    def test_longest_repetition_2(self):
        nums = [0,0,2,2,1,1,3,3,3]
        result = hw2.longest_repetition(nums)
        expected = 6
        self.assertEqual(result, expected)



if __name__ == '__main__':
    unittest.main()
