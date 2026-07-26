func removeDuplicates(nums []int) int {
    n := len(nums)
    write := 1
    for read := 1; read < n; read++ {
        if nums[read] != nums[write - 1] {
            nums[write] = nums[read]
            write++
        }
    }
    return write
}