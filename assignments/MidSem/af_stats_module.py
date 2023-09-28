from math import nan
from typing import Sequence, Mapping


class SummaryStatistics:
    def __init__(self, data: Sequence[float]):
        self.set_data(data)

    def set_data(self, data: Sequence[float]):
        self.data = data

    def n(self) -> int:
        return len(self.data)

    def mean(self) -> float:
        if len(self.data) == 0:
            return nan
        return sum(self.data)/len(self.data)

    def variance(self) -> float:
        if len(self.data) == 0:
            return nan
        mean = self.mean()
        return sum([(x - mean)**2 for x in self.data])/len(self.data)

    def stdev(self) -> float:
        return self.variance()**0.5

    def stderr(self) -> float:
        if len(self.data) == 0:
            return nan
        return self.stdev()/len(self.data)**0.5

    def z_score(self, x: float) -> float:
        return (x - self.mean())/self.stdev()

    def summary(self) -> Mapping[str, float]:
        return {
            "mean": self.mean(),
            "variance": self.variance(),
            "stdev": self.stdev(),
            "stderr": self.stderr()}
