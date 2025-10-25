# Enhanced FizzBuzz Program

def enhanced_fizzbuzz(start, end, fizz_word="Fizz", buzz_word="Buzz"):
    """
    Prints numbers in a range with FizzBuzz rules.
    Multiples of 2 → buzz_word
    Odd numbers → fizz_word
    Multiples of both 2 and 3 → combined word
    """
    for i in range(start, end + 1):
        output = ""
        
        # Multiple of 2
        if i % 2 == 0:
            output += buzz_word
        # Odd numbers
        else:
            output += fizz_word
        # Additional fun: mark multiples of 3
        if i % 3 == 0:
            output += "!"  # mark multiples of 3 with "!"
        
        # If nothing special, print the number
        if output == "":
            output = str(i)
        
        print(f"{i}: {output}")


# User inputs
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
fizz_word = input("Enter word for odd numbers (default 'Fizz'): ") or "Fizz"
buzz_word = input("Enter word for even numbers (default 'Buzz'): ") or "Buzz"

# Run enhanced FizzBuzz
enhanced_fizzbuzz(start, end, fizz_word, buzz_word)
