import ("slices"
        "cmp"
)

func threeSum(nums []int) [][]int {
    slices.SortFunc(nums, func(a, b int) int {
		return cmp.Compare(a, b)
	})

    triplets := make([][]int, 0)
    n := len(nums)

    for i := 0; i < n; i++ {
        if i > 0 && nums[i] == nums[i-1] {
            continue
        }
       
        j := i + 1
        k := n - 1

        for j < k {
            sum := nums[j] + nums[k]
            if sum == -nums[i] {
                triplets = append(triplets, []int{nums[i], nums[j], nums[k]})
                // Preventing duplicate (i, j)
                for j = j + 1; j < k && nums[j] == nums[j-1]; j++ {}
            } else if sum < -nums[i] {
                j++
            } else {
                k--
            }
        }
    }
    return triplets
}