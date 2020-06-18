'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n):
    # Your code here
    x = 1
    y = 0
    z = 0

    for i in range(n):
        x, y, z = x+y+z, x, y
    return x


# the cache allows us to save our work
# cache is a dictionary where the keys is the n, value is the answer
# def eating_cookies(n, cache):
#     if n < 0:
#         return 0
#     elif n == 0:
#         return 1
#     # check if the answer is in our cache
#     elif cache[n] > 0:
#         return cache[n]
#     else:
#         # otherwise, our cache doesn't contain the answer, so wee'll use our
#         # recursive logic to calculate it, and then save the answer in our
#         # cache for the future uses
#         return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
