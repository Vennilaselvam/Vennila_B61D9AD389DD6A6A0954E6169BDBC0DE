class Player:

  def Play(self):
    print("Player is playing cricket")


class Batsman(Player):

  def Play(self):
    print("Batsman is batting")


class Bowler(Player):

  def Play(self):
    print("Bowler is bowling")


# Creating objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# Calling the Play method for each object
batsman.Play()
bowler.Play()
