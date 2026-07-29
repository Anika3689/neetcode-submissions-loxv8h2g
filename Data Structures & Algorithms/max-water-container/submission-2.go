func maxArea(height []int) int {
    l := 0
    r := len(height) - 1
    maxArea := 0

    for l < r {
        maxArea = max(maxArea, (r - l) * min(height[l], height[r]))
        if height[l] < height[r] {
            l++
        } else {
            r--
        }
    }
    return maxArea
}