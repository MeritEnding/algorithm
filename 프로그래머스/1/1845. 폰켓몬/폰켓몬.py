def solution(nums):
    n_dict={}
    
    for i in nums:
        n_dict[i]=1
    
    if len(nums)//2 < len(n_dict):
        return len(nums)//2
    else:
        return len(n_dict)