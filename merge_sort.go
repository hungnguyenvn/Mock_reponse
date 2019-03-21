package main

var countInvered = 0

func naiveInversionCount(arr []int) int {
	length := len(arr)
	countInveted := 0
	for i := 0; i < length-1; i++ {
		for j := i + 1; j < length; j++ {
			if arr[i] > arr[j] {
				countInveted++
			}
		}
	}
	return countInveted
}

func main() {

}

func mergeSort(arr []int) {
	aux := make([]int, len(arr))
	mergeSortPerform(arr, aux, 0, len(arr)-1)
}

func mergeSortPerform(arr []int, aux []int, l int, r int) {
	if l < r {
		m := (r + l) / 2
		mergeSortPerform(arr, aux, l, m)
		mergeSortPerform(arr, aux, m+1, r)
		merge(arr, aux, l, m, r)
	}
}

func bottomMerge(arr []int) {
	r := len(arr)
	m := r / 2
	_bottomMerge(arr, 0, r, m)
}

func _bottomMerge(arr []int, l int, r int, m int) {

}

func merge(arr []int, aux []int, l int, m int, r int) {

	for i := l; i <= r; i++ {
		aux[i] = arr[i]
	}

	i := l
	j := m + 1
	for k := l; k <= r; k++ {
		if i <= m && j <= r {
			if aux[i] <= aux[j] {
				arr[k] = aux[i]
				i++
			} else {
				arr[k] = aux[j]
				j++
				countInvered += (m - i + 1)
			}
			continue
		}

		if i <= m {
			arr[k] = aux[i]
			i++
			continue
		}
		if j < r {
			arr[k] = aux[j]
			j++
			continue
		}

	}
}
