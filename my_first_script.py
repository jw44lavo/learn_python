"""
Welcome to your first python script.
"""





























# comments
"""
This is a comment.
"""

""" This is a comment. """

'''
This is a comment.
'''

''' This is a comment. '''

# This is a comment.




















# print to terminal
print("Hello world!")

print("This is my first python script.")

print("Beste Leben!!!")

a = "This is my first python script."
b = "Beste Leben!!!"

print(a,"\n",b)

print("{}\n{}".format(a,b))

























# variables, values and assignments
a = 1
b = "1"
c = True
d = []























# simple data structures
#print(type(a))
#print(type(b))
#print(type(c))
#print(type(d))


# characters and strings





# intergers, floats and doubles
a = 3
b = 3.14
c = 3.14159265358979323846264338327950288419




# booleans
t = True
f = False





# lists





# dictionaries















# parsing
a = 1
#print(a,'\t', type(a))

a = float(a)
#print(a,'\t', type(a))
















# loops
i = 0   # integer, stores a count
while i < 10:   # while-loop, iterates over i
    i += 1  # add +1 to current i
    #print(i)    # print current i

for i in range(10):
    pass
    #print(i)























# conditions



























# functions and parameters

def addition(a,b):
    return a + b

c = addition(1,2)

#print(c)





























# classes, objects and instances

class Room():
    def __init__(self, length, width, height, corners, windows):
        self.length = length
        self. width = width
        self.height = height
        self.corners = corners
        self.windows = windows

    def get_length(self):
        return self.length

    def get_ground_space(self):
        return self.length * self.width

    def get_room_volume(self):
        return self.length * self.width * self.height

    def set_length(self, x):
        self.length = x
        return

r = Room(3,4,2,4,1)
r_1 = Room(3,4,2,4,1)
r_2 = Room(1,1,1,1,1)

#print(r)
#print(r.corners)
#print(r.get_ground_space())
#print(r.get_room_volume())

#print(r.get_length()) # print(r.length)
r.set_length(1) #r.length = 1
#print(r.length)

r_3 = Room(2,2,2,2,2)

rooms = [r_1, r_2, r_3]

total_volume = 0
for r in rooms:
    volume = r.get_room_volume()
    total_volume += volume

#print(total_volume)
