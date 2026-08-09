func abs(val int) int {
	if val >= 0 {
		return val
	}
	return -1 * val
}

func asteroidCollision(asteroids []int) []int {
	stack := []int{}
	for _, asteroid := range asteroids {
		if asteroid > 0 {
			stack = append(stack, asteroid)
			continue
		}

		for n := len(stack); n > 0 && stack[n-1] > 0 && abs(asteroid) > abs(stack[n-1]); {
			stack = stack[:n - 1]
			n = len(stack)
		}
		if n := len(stack); n > 0 && stack[n-1] > 0 && abs(asteroid) == abs(stack[n-1]) {
			stack = stack[:n - 1]
			continue
		} 
		if n := len(stack); n > 0 && stack[n-1] > 0 && abs(asteroid) < abs(stack[n-1]) {
			continue
		}

		// current asteroid survived all possible collisions
		stack = append(stack, asteroid)
	}
	return stack
}

/* 
	- an asteroid moving to the left can't hit anything positioned to its right
		- bc a right neighbor will either be moving to the right (away from it)
			OR moving to the left at the same speed (meaning they will never collide)
		** THEREFORE only need to focus on interactions between left-moving asteroids and asteroids positioned before (to the left of) it

	- an asteroid moving to the right will hit the closest right-neighbor moving to 	the left before anything further away in the right direction (because all 			asteroids moving at same speed)
		** THEREFORE for every left-moving neighbor, consider collisions between closest left-hand neighbor(s) first 
*/