
package main

import "fmt"
func main()  {
	// var c chan struct{}
	// c := make(chan struct{}, 3)
	// for i := 0; i < 3; i++{
	// 	c <- struct{}
	// 	go Do()
		
	// }
	// ,<-c
	S()
	 
	
}
// func Do() {
// 	// do something
// 	fmt.Println("Do")

// 	// 
// 	a := c->
// }

// a = [1, 3, 5, 4, 6, 2, 9, 10]
// output = [3, 5, 6 ,6, 9, 9, 10, -1]

func S() {
	var a []int = []int{1, 3, 5, 4, 6, 2, 9, 10}
	n := len(a)
	var ret []int
	s := a[:]
	for i , j := 0, 0; i < n && j < n; {
		if a[i] == s[j] {
			j++
			continue
		}
		if a[i] < s[j] {
			ret = append(ret, s[j])
			i++
			continue
		}
		
		j++
	}
	fmt.Println(ret)
	// return ret
}