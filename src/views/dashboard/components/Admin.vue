<template>
  <el-card class="app-container center">
    <el-empty description="欢迎来到 admin 角色专属首页" />
    <el-input v-model="inputValue" class="input" placeholder="请输入数字数组（用逗号分隔）" />
    <el-button type="primary" @click="handleClick" class="button">提交</el-button>
    <el-button type="danger" @click="clearOutput" class="button">清空输出</el-button>
    <el-card class="output">{{ outputValues.join(", ") }}</el-card>
  </el-card>
</template>

<script setup lang="ts">
import { ref } from "vue"

const inputValue = ref<string>("") // 修改为字符串
const outputValues = ref<number[]>([])

const handleClick = () => {
  const trimmedValue = inputValue.value.trim()

  // 检查是否包含逗号
  if (trimmedValue.includes(",")) {
    const valuesArray = trimmedValue.split(",").map((item) => item.trim())

    // 类型检查：确保每个元素都是数字
    const isValidArray = valuesArray.every((item) => !isNaN(Number(item)) && item.length > 0)

    if (isValidArray) {
      outputValues.value.push(...valuesArray.map(Number)) // 转换为数字并添加数组
      outputValues.value = optimizedFastSort(outputValues.value) // 使用优化后的快速排序
      inputValue.value = "" // 清空输入框
    } else {
      alert("请输入有效的数字数组")
    }
  } else {
    alert("请输入用逗号分隔的数组")
  }
}

const clearOutput = () => {
  outputValues.value = [] // 清空输出数组
}

/**
function bubbleSort(arr: number[]) {
  const n = arr.length
  let swapped
  do {
    swapped = false
    for (let i = 0; i < n - 1; i++) {
      if (arr[i] > arr[i + 1]) {
        ;[arr[i], arr[i + 1]] = [arr[i + 1], arr[i]] // 使用解构赋值交换
        swapped = true
      }
    }
  } while (swapped)
  return arr
}
 */

/**
function fastSort(arr: number[]) {
  if (arr.length <= 1) {
    return arr // 基本情况：数组长度为0或1时，直接返回
  }

  const pivot = arr[arr.length - 1] // 选择最后一个元素作为基准
  const left = [] // 存放小于基准的元素
  const right = [] // 存放大于基准的元素

  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i] < pivot) {
      left.push(arr[i]) // 小于基准的元素
    } else {
      right.push(arr[i]) // 大于基准的元素
    }
  }

  // 递归调用并合并结果
  return [...fastSort(left), pivot, ...fastSort(right)]
}
*/

function optimizedFastSort(arr: any[]): number[] {
  if (arr.length <= 1) {
    return arr // 基本情况
  }

  // 选择基准元素（使用三数取中法）
  const mid = Math.floor(arr.length / 2)
  const pivot = medianOfThree(arr[0], arr[mid], arr[arr.length - 1])

  const left = []
  const right = []

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < pivot) {
      left.push(arr[i])
    } else if (arr[i] > pivot) {
      right.push(arr[i])
    }
  }

  // 使用插入排序处理小数组
  if (left.length < 10) {
    return [...insertionSort(left), pivot, ...optimizedFastSort(right)]
  } else {
    return [...optimizedFastSort(left), pivot, ...optimizedFastSort(right)]
  }
}

function medianOfThree(a: number, b: number, c: number) {
  return a > b ? (b > c ? b : a > c ? c : a) : a > c ? a : b > c ? c : b
}

function insertionSort(arr: number[]) {
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
</script>

<style lang="scss" scoped>
.center {
  height: 100%;
}
.output {
  margin-top: 20px;
  padding: 10px;
}
.button {
  margin-top: 20px;
}
.input {
  margin-top: 20px;
}
</style>
