func longestCommonPrefix(strs []string) string {
	if len(strs) == 1 {
		return strs[0]
	}
	minLen := len(strs[0])	
	for _, str := range strs {
		if len(str) == 0 {
			return ""
		}
		minLen = min(minLen, len(str))
	}

	letterIndex := 0
	for letterIndex < minLen {
		curChar := strs[0][letterIndex]
		for i := 1; i < len(strs); i++ {
			if strs[i][letterIndex] != curChar {
				return strs[i][:letterIndex]
			}
		}
		letterIndex += 1
	}
    return strs[0][:letterIndex]
}
