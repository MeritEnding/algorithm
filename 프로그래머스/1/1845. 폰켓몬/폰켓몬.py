def solution(nums):
    n_dict =dict()

    for n in nums:
        n_dict[n]=1
    
    if len(nums) // 2 <=len(n_dict):
        return len(nums)//2
    

    return len(n_dict)