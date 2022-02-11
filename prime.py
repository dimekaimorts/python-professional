from cmath import sqrt


def is_prime(num: int) -> bool:
    result_list = [x for x in range(2, int(num ** 1/2)+1) if num % x == 0]
    return len(result_list) == 0


def run():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
              71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163,
              167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269,
              271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383
              ]
    
    non_primes = [n for n in range(2,100) if (n^1 == n+1)]
    for prime in primes+non_primes:
        print("{} is prime? {}".format(prime, is_prime(prime)))


if __name__ == "__main__":
    run()
