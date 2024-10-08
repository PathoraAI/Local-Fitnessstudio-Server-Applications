from src.exercies.Lunges import Lunges
from src.exercies.Pushup import Pushup
from src.exercies.Plank import Plank
from src.exercies.ShoulderTap import ShoulderTap
from src.exercies.Squat import Squat
from src.exercies.chestpress import Chestpress
from src.exercies.latzug import Latzug


class Starter:
    def __init__(self):
        self.pushup = Pushup()
        self.plank = Plank()
        self.squat = Squat()
        self.shoulderTap = ShoulderTap()
        self.lunges = Lunges()
        self.chestpress = Chestpress()
        self.latzug = Latzug()

    def rep(self, type, source):
        if type.lower() == str("pushup"):
            self.pushup.exercise(source)
        elif type.lower() == str("chestpress"):
            self.chestpress.exercise(source)
        elif type.lower() == str("latzug"):
            self.latzug.exercise(source)
        else:
            raise ValueError(f"Input {type} and/or {source} is not correct. \n Kindly refer to the documentation")


if __name__ == '__main__':
    gym = Starter()
    gym.rep("latzug", "resources/latzug.mp4")
