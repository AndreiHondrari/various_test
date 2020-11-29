def solution(i):
    primes = [2, 3, 5, 7]
    number_of_digits = 4

    current_number = 11

    final_str = "2357"

    while number_of_digits <= (i+5):

        is_prime = True
        for p in primes:
            if current_number % p == 0:
                is_prime = False
                break

            if p >= current_number:
                break

        if is_prime:
            current_number_str = str(current_number)
            final_str += current_number_str
            number_of_digits += len(current_number_str)
            primes.append(current_number)

        current_number += 1


    return int(final_str[i:i+5])

print(solution(0))
