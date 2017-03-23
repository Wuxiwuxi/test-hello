'''
# a small test of making statements one by noe
f = open(r"/home/wuxi/Downloads/testfile")
lines = f.readlines()

name = lines[0].split()[0]
id = lines[0].split()[1]
gender =  lines[0].split()[2]
major = lines[0].split()[3]

# make sure that the first line is taoyongxue's massage
assert name == "taoyongxue"
assert id == "15121611"
assert gender == "female"
assert major == "physics"

#another test add labels to simplify the code
lables = lines[1].split()
name = lables[0]
id = lables[1]
gender =  lables[2]
major = lables[3]
print name,id,gender,major
'''

# A simple test of classfication
# define the class "person"
class Person(object):
    def __init__(self,name,id,gender,major):
        self.name = name
        self.id = id
        self.gender = gender
        self.major = major


 # make sure the person is a sophomore
    def check(id) :
        if id[3:] == "1512":
            return "sophomore"
        else :
            return "not a sophomore"


f = open(r"/home/wuxi/Downloads/testfile")
lines = f .readlines()

'''
define a group of people
give the characters for each people
'''
people = []
for line in lines :
    lables =line .split()
    people.append(Person(lables[0], lables[1], lables[2], lables[3]))

#print for check
for person in people:
    print "Name:{} id:{} gender:{} major:{} {}".format(person.name,person.id,person.gender,person.major,check(person.id))
