func removeElement(nums []int, val int) int {
    write := -1
    for i := 0; i < len(nums); i++ {
        if nums[i] == val {
            write = i
            break
        }
    }
    if write == -1 {
        return len(nums)
    }

    for read := write + 1; read < len(nums); read++ {
        if nums[read] == val {
            continue
        }
        nums[write], nums[read] = nums[read], nums[write]
        for write < len(nums) && nums[write] != val {
            write++
        }
    }
    return write
}