from typing import Sequence
from af_stats_module import SummaryStatistics


class Input:
    @staticmethod
    def select(options: Sequence[str]) -> int:
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        while True:
            try:
                choice = int(input("Enter your choice: "))
                if choice < 1 or choice > len(options):
                    raise ValueError
                return choice
            except ValueError:
                print("Invalid choice. Try again.")

    @staticmethod
    def get_float(prompt: str, quit_on: str | None = None) -> float | None:
        while True:
            try:
                inp = input(prompt)
                if quit_on is not None and inp == quit_on:
                    return None
                return float(inp)
            except ValueError:
                print("Invalid input. Try again.")

    @staticmethod
    def get_floats(prompt: str, quit_on: str = "done") -> Sequence[float]:
        numbers = []
        while True:
            number = Input.get_float(prompt, quit_on)
            if number is None:
                return numbers
            numbers.append(number)


def main():
    stats = SummaryStatistics([])
    while True:
        print(f"Select an option: [n = {stats.n()}]")
        choice = Input.select([
            "Input new data",
            "Mean",
            "Variance",
            "Standard deviation",
            "Standard error",
            "Z-score",
            "Summary",
            "Quit"])
        if choice == 1:
            print("Input data:")
            data = Input.get_floats("Enter a number (or 'done' to finish): ")
            stats.set_data(data)
        elif choice == 2:
            print(f"Mean = {stats.mean()}")
        elif choice == 3:
            print(f"Variance = {stats.variance()}")
        elif choice == 4:
            print(f"Standard deviation = {stats.stdev()}")
        elif choice == 5:
            print(f"Standard error = {stats.stderr()}")
        elif choice == 6:
            x = Input.get_float("Enter a number: ")
            print(f"Z-score = {stats.z_score(x)}")
        elif choice == 7:
            print("Summary:")
            summary = stats.summary()
            for key, value in summary.items():
                print(f"{key} = {value}")
        elif choice == 8:
            break

        print("=========================================")


if __name__ == "__main__":
    main()
