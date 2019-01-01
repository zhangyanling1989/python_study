class person():
    pass

p = person()
print(p)

class person:
    def say_hi(self):
        print('Hello, how are you?')

p=person()
p.say_hi()

class person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is ', self.name)

p = person ('Swaroop')
p.say_hi()


class Robot:

  population = 0

  def __init__(self, name):
        self.name = name
        print('Initializing {}'. format(self.name))
        Robot.population += 1
  def die(self):
        print('{} is being destroyed !'. format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print('{} was the last one'. format(self.name))
        else:
            print('There are still {:d} robots working'. format(Robot.population))
  def say_hi(self):
        print('Greetings, my masters call me {}'. format(self.name))

  @classmethod
  def how_many(cls):
        print('We have {:d} robots.'. format(cls.population))

droid1 = Robot("No1")
droid1.say_hi()
Robot.how_many()

droid2 = Robot('No2')
droid2.say_hi()
Robot.how_many()

print('\nRobots can do some work here.\n')

print('Robots have finished their work, so let\'s destroy them.' )
droid1.die()
droid2.die()

Robot.how_many()

