# Assignment: Logic Builder (17/02/2026)
# Print numbers 1–50 with Fizz/Buzz logic and count occurrences

def fizzbuzz(n: int) -> str:
    """Return FizzBuzz result for a single number."""
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

def run_fizzbuzz(limit: int = 50):
    """Run FizzBuzz from 1 to limit and count occurrences."""
    fizz_count = 0
    buzz_count = 0
    fizzbuzz_count = 0
    number_count = 0

    print("=" * 40)
    print("       🔢 FizzBuzz: 1 to 50")
    print("=" * 40)

    results = []
    for i in range(1, limit + 1):
        result = fizzbuzz(i)
        results.append(result)

        if result == "Fizz":
            fizz_count += 1
        elif result == "Buzz":
            buzz_count += 1
        elif result == "FizzBuzz":
            fizzbuzz_count += 1
        else:
            number_count += 1

    # Print in rows of 10
    for i, val in enumerate(results):
        print(f"{val:>8}", end="")
        if (i + 1) % 10 == 0:
            print()

    print("\n" + "=" * 40)
    print("📊 Occurrence Count:")
    print(f"  Numbers  : {number_count}")
    print(f"  Fizz     : {fizz_count}  (multiples of 3 only)")
    print(f"  Buzz     : {buzz_count}  (multiples of 5 only)")
    print(f"  FizzBuzz : {fizzbuzz_count}  (multiples of both 3 & 5)")
    print(f"  Total    : {fizz_count + buzz_count + fizzbuzz_count + number_count}")
    print("=" * 40)

if __name__ == "__main__":
    run_fizzbuzz(50)
