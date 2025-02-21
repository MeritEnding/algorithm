def solution(nums):
    answer = 0
    n_dict={}
    
    for num in nums:
        n_dict[num]=1
    
    if len(nums)//2 < len(n_dict):
        return len(nums)//2
    else:
        return len(n_dict)
    
    return answer