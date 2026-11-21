def moveZeroes(nums: list[int]):
        j=0
        for i in range(0, len(nums)):
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1

        for i in range(j, len(nums)):
            nums[j]=0
            j+=1

        return nums
    
print(moveZeroes([0,1,0,3,12]))