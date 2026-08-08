import (
	"slices"
)

func evalRPN(tokens []string) int {
	stk := []int{}
	operators := []string{"+", "-", "*", "/"}
	for _, token := range tokens {
		if !slices.Contains(operators, token) {
			tokenInt, _ := strconv.Atoi(token)
			stk = append(stk, tokenInt)
			continue
		}
		n := len(stk)
		op1, op2 := stk[n-2], stk[n-1]
		stk = stk[:n-2]
		if token == operators[0] {
			stk = append(stk, op1 + op2)
		} else if token == operators[1] {
			stk = append(stk, op1 - op2)
		} else if token == operators[2] {
			stk = append(stk, op1 * op2)
		} else {
			stk = append(stk, op1 / op2)
		}
	}
	
	return stk[0]
}
