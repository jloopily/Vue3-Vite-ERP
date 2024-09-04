import { ref } from "vue"

export const selectedAlgorithm = ref<string>("optimizedFastSort") // 默认选择的排序算法

// 选择算法
export const sortArray = (arr: number[]): number[] => {
  switch (selectedAlgorithm.value) {
    case "bubbleSort":
      return bubbleSort(arr)
    case "fastSort":
      return fastSort(arr)
    case "optimizedFastSort":
    default:
      return optimizedFastSort(arr)
  }
}

// 冒泡排序
function bubbleSort(arr: number[]): number[] {
  const n = arr.length
  let swapped: boolean
  do {
    swapped = false
    for (let i = 0; i < n - 1; i++) {
      if (arr[i] > arr[i + 1]) {
        ;[arr[i], arr[i + 1]] = [arr[i + 1], arr[i]]
        swapped = true
      }
    }
  } while (swapped)
  return arr
}

// 快速排序
function fastSort(arr: number[]): number[] {
  if (arr.length <= 1) {
    return arr
  }
  const pivot = arr[arr.length - 1]
  const left: number[] = []
  const right: number[] = []

  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i] < pivot) {
      left.push(arr[i])
    } else {
      right.push(arr[i])
    }
  }
  return [...fastSort(left), pivot, ...fastSort(right)]
}

// 优化快速排序
function optimizedFastSort(arr: number[]): number[] {
  if (arr.length <= 1) {
    return arr
  }
  const mid = Math.floor(arr.length / 2)
  const pivot = medianOfThree(arr[0], arr[mid], arr[arr.length - 1])
  const left: number[] = []
  const right: number[] = []

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < pivot) {
      left.push(arr[i])
    } else if (arr[i] > pivot) {
      right.push(arr[i])
    }
  }
  if (left.length < 10) {
    return [...insertionSort(left), pivot, ...optimizedFastSort(right)]
  } else {
    return [...optimizedFastSort(left), pivot, ...optimizedFastSort(right)]
  }
}

function medianOfThree(a: number, b: number, c: number): number {
  return a > b ? (b > c ? b : a > c ? c : a) : a > c ? a : b > c ? c : b
}

function insertionSort(arr: number[]): number[] {
  for (let i = 1; i < arr.length; i++) {
    const key = arr[i]
    let j = i - 1
    while (j >= 0 && arr[j] > key) {
      arr[j + 1] = arr[j]
      j--
    }
    arr[j + 1] = key
  }
  return arr
}
