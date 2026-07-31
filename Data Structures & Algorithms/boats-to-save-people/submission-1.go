import (
	"slices"
)

func numRescueBoats(people []int, limit int) int {
	slices.Sort(people)

	l := 0
	r := len(people) - 1
	minBoats := 0

	for l <= r {
		minBoats++
		if l == r {
			break
		}

		if people[l] + people[r] <= limit {
			l += 1
			r -= 1
		} else {
			r -= 1
		}
	}

	return minBoats

}
