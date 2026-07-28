import ("slices"
        "cmp")

func fourSum(nums []int, target int) [][]int {

    slices.SortFunc(nums, func(a, b int) int {
		return cmp.Compare(a, b)
	})

    n := len(nums)
    quads := make([][]int, 0)
    for a := 0; a <= n - 4; a++ {
        if a > 0 && nums[a] == nums[a-1] {
            continue
        }
        for b := a + 1; b <= n - 3; b++ {
            if b > a + 1 && nums[b] == nums[b-1] {
                continue
            }
            c := b + 1
            d := n - 1
            for c < d {
                remaining := target - (nums[a] + nums[b])
                if nums[c] + nums[d] == remaining {
                    quads = append(quads, []int{nums[a], nums[b], nums[c], nums[d]})
                    c++
                    for c < d && nums[c] == nums[c-1] {
                        c++
                    }
                } else if nums[c] + nums[d] < remaining {
                    c++
                } else {
                    d--
                }
            }
        }
    }
    return quads
}