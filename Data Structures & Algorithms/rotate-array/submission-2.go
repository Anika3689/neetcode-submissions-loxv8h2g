func reverse(nums []int, l int, r int) {
    for l < r {
        temp := nums[r]
        nums[r] = nums[l]
        nums[l] = temp
        l++
        r--
    }
}

func rotate(nums []int, k int)  {
    k %= len(nums)
    if k == 0 {
        return
    }
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)
}