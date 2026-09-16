class MonkeyBanana:
    def __init__(self):
        self.monkey = 3
        self.box = 3
        self.banana = 3
        self.level = "Down"

    def climb_box(self):
        print("Monkey climbs the box")
        self.level = "Up"

    def get_banana(self):
        if self.level == "Up":
            print("Monkey gets the banana")

    def solve(self):
        self.climb_box()
        self.get_banana()


problem = MonkeyBanana()
problem.solve()
