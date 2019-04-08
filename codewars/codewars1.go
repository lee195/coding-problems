package main

import (
	"fmt"
	"sort"
	"strings"
)

/*
* From https://www.reddit.com/r/golang/comments/5ia523/idiomatic_way_to_remove_duplicates_in_a_slice/
* by reddit user dchapes
* implementation adjusted to work for string slices
*/
func SliceUniqMap(s []string) []string {
    seen := make(map[string]struct{}, len(s))
    j := 0
    for _, v := range s {
        if _, ok := seen[v]; ok {
            continue
        }
        seen[v] = struct{}{}
        s[j] = v
        j++
    }
    return s[:j]
}

func StrArrContains(strArr []string, other string) bool {
	for _, str := range strArr {
		if strings.Contains(str, other) {
			return true
		}
	}
	return false
}

func InArray(array1 []string, array2 []string) []string {
	isInArr := []string{}
	for _, str := range array1 {
		if StrArrContains(array2, str){
			isInArr = append(isInArr, str)
		}
	}
	sort.Strings(isInArr)
	return SliceUniqMap(isInArr)
}

func main() {
	fmt.Println(InArray([]string{"arp", "live", "strong", "strong"}, []string{"lively", "alive", "harp", "sharp", "armstrong"}))
}