from typing import Sequence, Callable, TypeVar
from af_stats_module import SummaryStatistics

T = TypeVar("T")


class Input:
    # prompts the user to select an option from a list of options
    # returns the index of the selected option
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

    # prompts the user to enter a float
    # returns the float, or None if the user enters the quit_on string
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

    # prompts the user to enter a sequence of floats, terminated by quit_on
    # returns the sequence
    @staticmethod
    def get_floats(prompt: str, quit_on: str = "done") -> Sequence[float]:
        numbers = []
        while True:
            number = Input.get_float(prompt, quit_on)
            if number is None:
                return numbers
            numbers.append(number)


class Output:
    # prints the name and value of a function
    @staticmethod
    def print_fn(fn: Callable[[], float]):
        print(f"{fn.__name__} = {fn()}")

    # prints the name and value of a function applied to an argument
    @staticmethod
    def print_fn1(fn: Callable[[T], float], x: T):
        print(f"{fn.__name__}({x}) = {fn(x)}")


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
            Output.print_fn(stats.mean)
        elif choice == 3:
            Output.print_fn(stats.variance)
        elif choice == 4:
            Output.print_fn(stats.stdev)
        elif choice == 5:
            Output.print_fn(stats.stderr)
        elif choice == 6:
            x = Input.get_float("Enter a number: ")
            Output.print_fn1(stats.z_score, x)
        elif choice == 7:
            print("Summary:")
            for fn in [
                stats.mean,
                stats.variance,
                stats.stdev,
                stats.stderr,
            ]:
                Output.print_fn(fn)
        elif choice == 8:
            break

        print("=========================================")


if __name__ == "__main__":
    main()
