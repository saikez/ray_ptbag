class Player ():
  def __init__(self):
    self.inventory = []
    self.alive = true
    self.x, self.y = world.starting_position
    self.hidden
    self.victory = false

  def show_inventory(self):
    for item in self.inventory:
      print(item, '\n')

  def move(self, dx, dy):
    self.hidden = false
    self.x += dx
    self.y += dy

  def hide(self)
    self.hidden = true

  def wait(self)
    print('You wait...', '\n')
