class Orc:
  #Constructor
  def __init__(self,_name, _health = 100, _damage = 50, _speed = 10):
    # properties
    self.name = _name
    self.health = _health
    self.damage = _damage
    self.speed = _speed
    self.MAX_HEALTH = 100 #class property
    self.HEAL_VAL = 5
  def attack(self):
    pass
  def defend(self):
    pass
  def heal(self):
    thealth = self.health + 5
    if thealth < self.MAX_HEALTH:
      self.health = thealth
    else:
      self.health = self.MAX_HEALTH
  def isAlive(self):
    return self.health > 0


class Elf:
  #Constructor
  def __init__(self,_name, _health = 100, _damage = 50, _speed = 10):
    # properties
    self.name = _name
    self.health = _health
    self.damage = _damage
    self.speed = _speed
    self.MAX_HEALTH = 100 #class property
    self.HEAL_VAL = 5
  def attack(self):
    pass
  def defend(self):
    pass
  def heal(self):
    thealth = self.health + 5
    if thealth < self.MAX_HEALTH:
      self.health = thealth
    else:
      self.health = self.MAX_HEALTH
  def isAlive(self):
    return self.health > 0

class Fairy:
  #Constructor
  def __init__(self,_name, _health = 100, _damage = 50, _speed = 10):
    # properties
    self.name = _name
    """Maybe we add functionality to give the player a random number of 'points' and allow them to allocate the 'points' to health, damage and speed"""
    self.health = _health
    self.damage = _damage
    self.speed = _speed
    self.MAX_HEALTH = 100 #class property
    self.HEAL_VAL = 5
  def attack(self):
    pass
  def defend(self):
    pass
  def heal(self):
    thealth = self.health + 5
    if thealth < self.MAX_HEALTH:
      self.health = thealth
    else:
      self.health = self.MAX_HEALTH
  def isAlive(self):
    return self.health > 0

