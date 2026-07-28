func twoSum(numbers []int, target int) []int {
	l := 0
	r := len(numbers) - 1
	for l < r {
		sum := numbers[l] + numbers[r]
		if sum == target {
			break
		}
		if sum > target {
			r -= 1
		} else {
			l += 1
		}
	}
	return []int{l + 1, r + 1}
}
