from typing import Sequence, Mapping


class SummaryStatistics:
    def __init__(self, data: Sequence[float]):
        self.data = data

    def mean(self) -> float:
        return sum(self.data)/len(self.data)

    def variance(self) -> float:
        mean = self.mean()
        return sum([(x - mean)**2 for x in self.data])/len(self.data)

    def stdev(self) -> float:
        return self.variance()**0.5

    def stderr(self) -> float:
        return self.stdev()/len(self.data)**0.5

    def z_score(self, x: float) -> float:
        return (x - self.mean())/self.stdev()

    def summary(self) -> Mapping[str, float]:
        return {
            "mean": self.mean(),
            "variance": self.variance(),
            "stdev": self.stdev(),
            "stderr": self.stderr()}
