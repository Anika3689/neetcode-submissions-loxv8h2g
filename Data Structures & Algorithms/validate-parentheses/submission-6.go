func isValid(s string) bool {
	parenMap := map[rune]rune{
		')' : '(',
		'}'	: '{',
		']' : '[',
	}

	stk := []rune{}
	for _, ch := range s {
		complement, isClose := parenMap[ch]
		if !isClose {
			stk = append(stk, ch)
			continue
		}

		if len(stk) == 0 { // no matching open parenthesis
			return false
		}
		if stk[len(stk) - 1] == complement {
				stk = stk[:len(stk) - 1]
		} else {
			return false
		}
	}
	return len(stk) == 0
}




