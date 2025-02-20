def solution(phone_book):
    hash_map={}
    
    for nums in phone_book:
        hash_map[nums]=1
    
    for nums in phone_book:
        answer=''
        for num in nums:
            answer+=num
            if answer != nums and answer in hash_map:
                return False
    return True