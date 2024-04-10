import json
from collections import Counter
from typing import List, Tuple
import json
from collections import Counter
from typing import List, Tuple


def load_data(filename: str) -> List[int]:
    """Load a list of integers from a JSON file."""
    with open(filename, 'r') as file:
        data = json.load(file)
        return data['numbers']


def calculate_frequency(numbers: List[int]) -> List[Tuple[int, int]]:
    """Calculate the frequency of each unique number and return sorted by frequency descending."""
    frequency_counter = Counter(numbers)
    sorted_frequency = sorted(frequency_counter.items(), key=lambda x: x[1], reverse=True)
    return sorted_frequency


def get_third_highest_frequency(frequencies: List[Tuple[int, int]]) -> Tuple[int, int]:
    """Retrieve the third highest frequency from the list of (number, frequency) tuples."""
    if len(frequencies) < 3:
        raise ValueError("Less than 3 unique numbers provided")
    unique_frequencies = sorted(set(frequencies), key=lambda x: x[1], reverse=True)
    if len(unique_frequencies) < 3:
        raise ValueError("Less than 3 unique frequencies provided")
    return unique_frequencies[2]


def save_output(data: dict, filename: str) -> None:
    """Save the given data as JSON in a file."""
    with open(filename, 'w') as file:
        json.dump(data, file)


def main():
    numbers = load_data('data.json')
    frequencies = calculate_frequency(numbers)
    third_highest_freq = get_third_highest_frequency(frequencies)

    output = {
        "sorted_frequency_distribution": frequencies,
        "third_highest_frequency": third_highest_freq
    }

    save_output(output, 'output.json')

    print("Output saved to output.json")
    print("Third highest frequency:", third_highest_freq)


if __name__ == "__main__":
    main()
