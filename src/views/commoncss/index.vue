<script lang="ts" setup></script>
<template>
  <h2>浮动</h2>
  <div>指将元素脱离文档流向左或者向右布局</div>
  <div>使用float属性来设置元素的浮动</div>
  <div>默认值为none，也就是不浮动；还可以设置left向左浮动；right向右浮动</div>
  <h2>浮动的特点</h2>
  <div>一旦对元素设置浮动后，不论之前元素是内联元素还是块级元素，都会被当作块级元素处理</div>
  <div>一旦对元素设置浮动后，该元素便会脱离标准流，会造成其父元素的内容塌陷</div>
  <div class="box1">
    华为云
    <div class="swim0">荣耀</div>
  </div>
  <div class="a" />
  <div class="b" />
  <div class="c" />
  <h2>清除浮动</h2>
  <div class="box2">
    <div class="left0">华为left</div>
    <div class="right0">华为right</div>
    <!-- <div class="clear"></div> --><!--若插入内联级的内容还是会塌陷-->
  </div>
  <div>为什么要清除浮动：元素设置为浮动时引起父元素内容塌陷，影响布局效果</div>
  <div>clear属性用于设置元素哪一侧不允许浮动</div>
  <div>默认值为none，表示不进行控制</div>
  <div>当设置为left时，表示左侧不允许浮动</div>
  <div>当设置为right时，表示右侧不允许浮动</div>
  <div>当设置为both时，表示两侧都不允许浮动</div>
  <div>overflow属性：用于设置元素不够容纳内容时的显示方式</div>
  <div>默认值为visible</div>
  <div>当值为auto时，自动添加滚动条</div>
  <div>当值为hidden时，会用匿藏掉超出的内容</div>
  <div>当值为scroll时，会一直显示滚动条</div>
  <div class="box3">
    目前世界正处在大发展大变革的时期。从经济总量来看，国际力量正朝着更均衡的方向发展。改变了西方世界在国际政治经济格局中占据主导地位的现象。世界权力中心将逐步由欧洲、美洲等发达国家向金砖国家等发展中国家分布转移，由大西洋向太平洋转移。在全球构成“你中有我，我中有你”的态势。
  </div>
  <h2>常用技巧</h2>
  <div class="box4 clearfix">
    <div class="left2" />
    <div class="right2" />
  </div>
  <div>企业级应用中清除浮动的最佳方法</div>
  <div>clearfix方案</div>
  <div>使用伪元素after在父元素尾部添加一个元素</div>
  <div>对这个添加的伪元素应用清除浮动的样式</div>
  <div>必备三大样式：content、clear、display</div>
  <div>可选三大样式：height、font-size、visibility（可见不可见）</div>
</template>

<style>
.box1 {
  border: 1px solid red;
}
.swim0 {
  width: 100px;
  height: 100px;
  background: yellow;
  /* float: left; */
  float: right;
}
.box2 {
  border: 1px solid blue;
  width: 500px;
  /* height: 200px;指定高度防止塌陷 */
  overflow: hidden;
}
.left0 {
  width: 200px;
  height: 200px;
  background: green;
  float: left;
}
.right0 {
  width: 200px;
  height: 200px;
  background: yellow;
  float: right;
}
.clear {
  clear: both;
}
.box3 {
  border: 1px solid blue;
  width: 500px;
  height: 30px;
  overflow: scroll;
}
.box4 {
  border: 1px solid red;
}
.left2 {
  width: 200px;
  height: 200px;
  background: green;
  float: left;
}
.right2 {
  width: 200px;
  height: 200px;
  background: yellow;
  float: right;
}
.clearfix:after {
  content: ""; /*内容为空*/
  clear: both;
  display: block;
  height: 0px;
  font-size: 0px;
  visibility: hidden; /*不可见*/
}
.a {
  height: 200px;
  width: 200px;
  background-color: red;
}
.b {
  height: 200px;
  width: 200px;
  background-color: green;
}
.c {
  height: 200px;
  width: 200px;
  background-color: blue;
}
.a,
.b,
.c {
  float: left;
}
</style>
