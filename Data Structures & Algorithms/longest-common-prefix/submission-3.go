func longestCommonPrefix(strs []string) string {
	// base cases
	if len(strs) == 1 {
		return strs[0]
	}
	for _, str := range strs {
		if len(str) == 0 {
			return ""
		}
	}

    var prefix strings.Builder
	letterIndex := 0
	for {
		if letterIndex >= len(strs[0]) {
			break
		}
		curChar := strs[0][letterIndex]
		for i := 1; i < len(strs); i++ {
			if !(letterIndex < len(strs[i]) && strs[i][letterIndex] == curChar) {
				return prefix.String()
			}
		}
		prefix.WriteByte(curChar)
		letterIndex += 1
	}
	return prefix.String()
}
