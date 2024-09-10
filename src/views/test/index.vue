<script lang="ts" setup></script>

<template>
  <div class="container">
    <header class="header">
      <!-- Header content here -->
      <h1>11</h1>
    </header>
    <main class="main">
      <div class="column">
        <div class="post">
          <!-- Post content here -->
          <h1>Post 1</h1>
        </div>
        <div class="post">
          <!-- Post content here -->
          <h1>Post 3</h1>
        </div>
        <div class="post">
          <!-- Post content here -->
          <h1>Post 5</h1>
        </div>
        <div class="post">
          <!-- Post content here -->
          <h1>Post 7</h1>
        </div>
      </div>
      <div class="column">
        <div class="post">
          <!-- Post content here -->
          <h1>Post 2</h1>
        </div>
        <div class="post">
          <!-- Post content here -->
          <h1>Post 4</h1>
        </div>
        <div class="post">
          <!-- Post content here -->
          <h1>Post 6</h1>
        </div>
        <div class="post">
          <!-- Post content here -->
          <h1>Post 8</h1>
        </div>
      </div>
    </main>
    <footer class="footer">
      <!-- Footer content here -->
      <h1>44</h1>
    </footer>
  </div>
</template>

<style lang="scss" scoped>
.container {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.header {
  background-color: #ff4d5a;
  color: white;
  padding: 10px;
}

.main {
  flex: 1;
  display: flex;
}

.column {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.banner {
  background-color: #f0f0f0;
  padding: 20px;
}

.post {
  background-color: #ffffff;
  padding: 20px;
  margin: 20px;
  height: 200px;
}

.footer {
  background-color: #333333;
  color: white;
  padding: 10px;
}
</style>
