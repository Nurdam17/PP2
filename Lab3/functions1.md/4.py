nums=[int(x) for x in input().split()]
new_array=[]
def filter_prime(nums):
    cnt_prime=0
    for i in range(len(nums)):
        if nums[i]==0 or nums[i]==1:
            continue
        else:
            for j in range(2, (nums[i]//2)+1):
                if nums[i]%j==0:
                    cnt_prime+=1
        if cnt_prime==0:
            new_array.append(nums[i])
        else:
            cnt_prime=0
filter_prime(nums)
print(new_array)