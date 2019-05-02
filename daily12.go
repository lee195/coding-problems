package main

import "fmt"

func LongestWithDistinct(s string, k int) string {
	longest := ""
	var candidate string
	for i := 0; i < len(s); i++ {
		for j := 1; j < len(s)-i; j++ {
			candidate = s[i:i+j]
			if CountDistinctChar(candidate) <= k && len(candidate) > len(longest) {
				longest = candidate
			}
		}
	}
		
	return longest
}

func CountDistinctChar(s string) int {
    seen := make(map[rune]struct{}, len(s))
    j := 0
    for _, v := range s {
        if _, ok := seen[v]; ok {
            continue
        }
        seen[v] = struct{}{}
        j++
    }
    return j
}

func main() {
	fmt.Println(LongestWithDistinct("abcba", 2))
}