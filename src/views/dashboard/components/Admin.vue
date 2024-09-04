<script setup lang="ts">
import { ref } from "vue"
import { sortArray, selectedAlgorithm } from "./Sort"

const inputValue = ref<string>("")
const outputValues = ref<number[]>([])
const executionTime = ref<number>(0) // 用于存储排序时间

const handleClick = () => {
  const trimmedValue = inputValue.value.trim()

  if (trimmedValue.includes(",")) {
    const valuesArray = trimmedValue.split(",").map((item) => item.trim())
    const isValidArray = valuesArray.every((item) => !isNaN(Number(item)) && item.length > 0)

    if (isValidArray) {
      outputValues.value.push(...valuesArray.map(Number))
      const startTime = performance.now() // 开始计时
      outputValues.value = sortArray(outputValues.value) // 根据选择的算法排序
      const endTime = performance.now() // 结束计时
      executionTime.value = endTime - startTime // 计算运行时间
      inputValue.value = ""
    } else {
      alert("请输入有效的数字数组")
    }
  } else {
    alert("请输入用逗号分隔的数组")
  }
}

const clearOutput = () => {
  outputValues.value = []
  executionTime.value = 0 // 清空排序时间
}
</script>

<template>
  <el-card class="app-container center">
    <el-empty description="欢迎来到 admin 角色专属首页" />
    <el-input v-model="inputValue" class="input" placeholder="请输入数字数组（用逗号分隔）" />

    <el-select v-model="selectedAlgorithm" class="select" placeholder="选择排序算法">
      <el-option label="优化快速排序" value="optimizedFastSort" />
      <el-option label="冒泡排序（不推荐使用）" value="bubbleSort" />
      <el-option label="快速排序" value="fastSort" />
    </el-select>

    <el-button type="primary" @click="handleClick" class="button">提交</el-button>
    <el-button type="danger" @click="clearOutput" class="button">清空输出</el-button>

    <el-card class="output" style="overflow-y: auto; max-height: 200px">{{ outputValues.join(", ") }}</el-card>
    <div class="time">排序时间: {{ executionTime }} 毫秒</div>
    <!-- 显示排序时间 -->
  </el-card>
</template>

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
.select {
  margin-top: 20px;
}
.time {
  margin-top: 20px;
  font-weight: bold;
}
</style>
