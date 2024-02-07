import time


def how_long(func, *args):
    start_time = time.time()
    output = func(*args)
    end_time = time.time()
    print(f"{end_time - start_time} sec")
    return output


def factorize(*number):
    output = []
    for num in number:
        out = []
        i = 1
        while i**2 <= num:
            if num % i == 0:
                out.append(i)
                if i != num // i:
                    out.append(num // i)
            i += 1
        out.sort()
        output.append(out)
    return output

# print(factorize(36))

# print(factorize(128, 255, 99999, 10651060))

a, b, c, d  = factorize(128, 255, 99999, 10651060)

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

speed_test_input = (10**15, 10**13, 10**12, 10**14)

how_long(factorize, *speed_test_input)

# how_long(factorize)