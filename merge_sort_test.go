package main

import (
	"fmt"
	"math/rand"
	"testing"
	"time"
)

func TestMegeredTress(t *testing.T) {
	s := rand.NewSource(time.Now().UnixNano())
	r := rand.New(s)
	for i := 0; i < 100; i++ {
		// reset
		countInvered = 0
		size := r.Intn(500)

		a := make([]int, size)
		aux := make([]int, size)
		for i := 0; i < size; i++ {
			a[i] = r.Intn(5)
			aux[i] = a[i]
		}

		navive := naiveInversionCount(a)
		mergeSort(a)

		if navive != countInvered {
			fmt.Printf("Failed  %d - %d", navive, countInvered)
			fmt.Println(aux)
			return
		}
		fmt.Println("Passed, ", size)
	}
}

func TestBottomMerge(t *testing.T) {
	s := rand.NewSource(time.Now().UnixNano())
	r := rand.New(s)

	for i := 0; i < 100; i++ {
		size := r.Intn(100)

		arr := make([]int, size)

		for j := 0; j < size; j++ {
			arr[j] = r.Intn(100)
		}

		bottomMerge(arr)

		for j := 0; j < size-1; j++ {
			if arr[j] > arr[j+1] {
				t.FailNow()
				return
			}
		}
		fmt.Println("Pass : i = ", size)
	}
}
