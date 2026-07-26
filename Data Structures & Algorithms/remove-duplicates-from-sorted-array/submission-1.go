func removeDuplicates(nums []int) int {
    n := len(nums)
    write := 1
    unique := 1
    for ; write < n && unique < n; write++ {

        for ; unique < n && nums[unique] == nums[write - 1]; unique++ {}
        if unique >= n {
            break
        }
        nums[write] = nums[unique]
    }
    return write
}