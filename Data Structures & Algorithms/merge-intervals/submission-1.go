import ("cmp"
	 "slices"
)

func merge(intervals [][]int) [][]int {
    slices.SortFunc(intervals, func(a, b []int) int {
		return cmp.Compare(a[0], b[0])
	})
    nonOverlapping := make([][]int, 1)
    nonOverlapping[0] = intervals[0]

    for i := 1; i < len(intervals); i++ {
        curStart, curEnd := intervals[i][0], intervals[i][1]
        n := len(nonOverlapping)
        prevEnd := nonOverlapping[n-1][1]
        if curStart <= prevEnd && curEnd <= prevEnd {
            continue
        } else if curStart <= prevEnd {
            nonOverlapping[n - 1][1] = curEnd
        } else {
            nonOverlapping = append(nonOverlapping, intervals[i])
        }
    }
    return nonOverlapping
}