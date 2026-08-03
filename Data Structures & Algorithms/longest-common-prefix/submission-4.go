func longestCommonPrefix(strs []string) string {
	if len(strs) == 1 {
		return strs[0]
	}
	minLen := 200	
	for _, str := range strs {
		if len(str) == 0 {
			return ""
		}
		minLen = min(minLen, len(str))
	}

    var prefix strings.Builder
	letterIndex := 0
	for letterIndex < minLen {
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
