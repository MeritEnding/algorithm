def solution(phone_book):
    
    hash_map={}
    
    for nums in phone_book:
        hash_map[nums]=1
    
    for nums in phone_book:
        answer = ''
        for num in nums:
            answer += num
            if answer in hash_map and answer != nums:
                return False
    return True