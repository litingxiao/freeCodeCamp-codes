import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = [k for k, v in kwargs.items() for _ in range(v)]

    def draw(self, num):
        if num > len(self.contents):
            tmp = self.contents
            self.contents = []
            return tmp
        else:
            drawn = random.sample(self.contents, num)
            for b in drawn:
                self.contents.remove(b)
            return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for n in range(num_experiments):
        # need to deep copy the hat object in each exp
        now_hat = copy.deepcopy(hat)

        # draw and count the drawn balls
        drawn_balls = now_hat.draw(num_balls_drawn)
        counts = {b: drawn_balls.count(b) for b in set(drawn_balls)}
        
        # check if this exp succeeds
        passed = True
        for b, v in expected_balls.items():
            if counts.get(b, 0) < v:
                passed = False
                break
        
        if passed:
            success += 1

    return success / num_experiments