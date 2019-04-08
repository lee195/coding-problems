package main

import "fmt"

func CollatzSequence(n int) []int {
	var collatzSeq []int
	i := n
	for i != 1 {
		if i % 2 == 0 {
			i = i/2
		} else {
			i = 3*i + 1
		}
		collatzSeq = append(collatzSeq, i)
	}
	return collatzSeq
}

func main() {
	longestSeq := 0
	var num, currentLen int
	for i := 999999; i > 0; i-- {
		currentLen = len(CollatzSequence(i))
		if (currentLen > longestSeq) {
			longestSeq = currentLen
			num = i
		}
	}
	fmt.Println(num, longestSeq)
}