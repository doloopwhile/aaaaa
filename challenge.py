import sys

def square_sum(numbers, sum=0):
    if not numbers:
        return sum
    x = numbers[0]
    if x > 0:
        sum += x * x
    return square_sum(numbers[1:], sum)

def rec_process_lines(sequence_lines):
    if not sequence_lines:
        return
    line = sequence_lines[0]
    numbers = list(map(int, line.split()))
    print(square_sum(numbers))
    return rec_process_lines(sequence_lines[1:])

def main():
    lines = sys.stdin.readlines()
    sequence_lines = lines[2::2]
    rec_process_lines(sequence_lines)

if __name__ == '__main__':
    main()
