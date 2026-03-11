# your prompt here
def get_geometric_mean(*nums):
    product = 1
    for num in nums:
        product *= num
    return pow(product, 1 / len(nums))