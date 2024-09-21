def max_product(n):
    # We use memoization to store intermediate results
    memo = {}

    def opt(i, n):
        # Base cases
        if n == 0:
            # We need at least two numbers, so return 1 if we have formed a valid product
            return 1 if i > 1 else 0
        if n < 0 or i > n:
            return float('-inf')

        # Check if result is already computed
        if (i, n) in memo:
            return memo[(i, n)]

        # Option 1: Include the number 'i' in the product and subtract it from 'n'
        include = i * opt(i, n - i)
        # Option 2: Skip the number 'i' and move to the next number
        skip = opt(i + 1, n)

        # Take the maximum of both options
        memo[(i, n)] = max(include, skip)
        return memo[(i, n)]

    # Start from number 1
    result = opt(1, n)
    return result

for n in range(3, 10):
    print("Maximum product:", max_product(n))
'''
# Example usage:
n = int(input("Enter an integer n (n >= 3): "))
print("Maximum product:", max_product(n))
'''