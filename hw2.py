import data
import math
from typing import Optional
from data import Point, Rectangle, Duration, Song
# Write your functions for each part in the space below.
# Part 1
def create_rectangle(p1:Point, p2:Point) -> Rectangle: #Function accepts INPUT: 2 parameters of class Point(x,y) and must return a OUTPUT: Rectangle(top_left, bottom_right) object.
    top_left = Point(0, 0)                       #Purpose is to determine which x and y values belong in the top left or bottom right.
    bot_right = Point(0, 0)

    #For top_left = take lowest x and highest y
    #For bot_right = take highest x and lowest y

    if p1.x <= p2.x:          #Check for lowest x for top left and greatest x for bottom right or if equal to.
        top_left.x = p1.x
        bot_right.x = p2.x

    else:                     #Else swap their values because then p2's x values must be less than p1.
        top_left.x = p2.x
        bot_right.x = p1.x

    if p1.y >= p2.y:          #Check for greatest y for top left and lowest y for bottom right or if equal to.
        top_left.y = p1.y
        bot_right.y = p2.y

    else:                     #Else swap y values because then p1's y values must be less than p2.
        top_left.y = p2.y
        bot_right.y = p1.y

    return Rectangle(top_left, bot_right)

# Part 2
def shorter_duration_than(x:Duration, y:Duration) -> bool:  #Function accepts INPUT: 2 parameters of class Duration(minutes, seconds) and must return either OUTPUT: True or False.
    if x.minutes > y.minutes:                               #Purpose is to determine if the 1st object's duration is greater than the 2nd object's duration. If so return true, if not return False.
        return True                                         #If the 1st duration's minutes > 2nd duration's minutes then automatically return true.
    elif x.minutes == y.minutes and x.seconds < y.seconds:  #If the minutes are the same but the 2nd duration's seconds is greater return False.
        return False
    elif x.minutes == y.minutes and x.seconds > y.seconds:  #If the minutes are the same and the 1st duration's seconds is greater return True.
        return True

# Part 3
def song_shorter_than(songs:list[Song], time:Duration) -> list[Song]: #Function accepts INPUT: a list of class Song(artist, title, Duration) and Duration. It must return OUTPUT: a list of class Song.
    list_x = []         #Placeholder                                  #Purpose is to determine which songs duration (minutes and seconds) are under or less than the set given duration
    for song in songs:
        if song.duration.minutes <= time.minutes and song.duration.seconds <=time.seconds:  #For each song in the list compare the minutes and seconds to the set duration. If it is shorter or equal to append to a list.
            list_x.append(song)
    return list_x

# Part 4
def running_time(songs:list[Song], ints:list[int]) -> Duration: #Function accepts INPUT: a list of class Song(artist, title, Duration) and a list of integers. It must return OUTPUT: a class Duration object.
    total_minutes = 0       #Placeholders                       #Purpose is to get the duration (minutes & seconds) for however many songs we want and add them all it together.
    total_seconds = 0

    for index in ints:                                      #Loop for every index in the given list:
        total_minutes += songs[index].duration.minutes          #Find the song via index and add its minutes
        total_seconds += songs[index].duration.seconds          #Find the song via index and add its seconds

    total_minutes += total_seconds // 60                    #If seconds exceed 60 add the base to minutes EX: 100//60 so add 1
    total_seconds = total_seconds % 60                      #Then total seconds will remain as the remainder value so 6
    return Duration(total_minutes, total_seconds)

# Part 5
def validate_route(city_links:list[list[str]], names:list[str]) -> bool: #Function accepts INPUT: a sublist of strings and a list of strings. It must return OUTPUT: True or False
    if names == []:     #If list is place return true                    #Purpose is to go through the given sublist that contains di-directional pairs of routes. We want to know if our inputted route will result
        return True                                                      #in an acceptable path between cities.

    for i in range(len(names) - 1):     #For every element in the list of names:
        city_a = names[i]                   #Compare the cities as pairs and go through to see if there's a link between them found in the sublist of pairs of strings.
        city_b = names[i+1]

        if [city_a, city_b] not in city_links and [city_b, city_a] not in city_links:   #If the pair cities is not found in either order in the list of pairs.
            return False                                                                #Return False
    return True                                                                         #Defaults to True


#Part 6
def longest_repetition(ints:list[int]) -> Optional[int]:  #Function accepts INPUT: a list of integers and must return OUTPUT: an integer or none:
                                                          #Purpose of this is to go through a list of integers and determine the index for which the longest repetition of a certain integer begins.
    longest_streak = 1          #Stores the length of the LONGEST repetition
    longest_start_index = 0     #Tracks starting index of LONGEST repetition
    current_streak = 1          #Tracks CURRENT repetition length
    current_start_index = 0     #Stores start index of CURRENT repetition

    for nums in range(1, len(ints)):    #Loop through each value in the list via index:
        if ints[nums] == ints[nums-1]:     #If 2nd number = 1st number:
            current_streak += 1            #Add to the streak
        else:

            if current_streak > longest_streak:         #If current streak > longest streak:
                longest_streak = current_streak            #Set longest streak to counter
                longest_start_index = current_start_index  #Stores starting index of longest streak

            current_streak = 1                             #Reset the counter for a new number or set of repetitions
            current_start_index = nums                     #Reset the start index for a new set of repetition

    if current_streak > longest_streak:                    #Final check for the last numbers
        longest_start_index = current_start_index

    return longest_start_index



