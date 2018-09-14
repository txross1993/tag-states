
def findSumsToK(inputArray, k):
    sums = []

    if not isinstance(inputArray, list):
        inputArray = list(inputArray)

    for index, n in enumerate(inputArray):
        y = inputArray.pop(index)
        complement = k-y
        for item in inputArray:
            if item == complement:
                sums.append((y, item))
    
    return set(sums)

def test_answer():
    nums = [1,3,2,3,2,5,46,6,7,4]
    k = 5

    print(findSumsToK(nums, k)) == set([(1,4), (3,2)])

#    nums = [1,3,4,2]

test_answer()
