package main

import (
	"fmt"
	"sync"
)

func main() {
	out, done := goroutine()

	var total int
loop:
	for {
		select {
		case i := <-out:
			total += i
		case <-done:
			break loop
		default:
			continue
		}
	}

	fmt.Println("total is: ", total)
}

func goroutine() (chan int, chan struct{}) {
	out := make(chan int, 1)
	done := make(chan struct{}, 1)
	go func() {
		var wg sync.WaitGroup
		for i := 0; i < 400000; i++ {
			wg.Add(1)
			go func(i int) {
				defer wg.Done()
				out <- i
			}(i)
		}
		wg.Wait()
		done <- struct{}{}
	}()

	return out, done
}
