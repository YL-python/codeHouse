<template>
	<view>
		<view>
			<text>唱歌跳舞打篮球</text>
		</view>
		<view>
			<text selectable>唱歌跳舞打篮球</text>
		</view>
		<view>
			<text selectable space="emsp">唱歌    跳舞打篮球</text>
		</view>
		<view>
			<text selectable space="ensp">唱歌    跳舞打篮球</text>
		</view>
		<view>
			<text selectable space="nbsp" style="font-size: 30px;">唱歌    跳舞打篮球</text>
		</view>
		
		<view>
		  <!-- 是否解码 貌似现在平台都支持了，以前是不支持的 -->
		  <text decode='true'>&nbsp; &lt; &gt; &amp; &apos; &ensp; &emsp;</text>
		</view>
		<view>
		  <!-- 是否解码 -->
		  <text decode='false'>&nbsp; &lt; &gt; &amp; &apos; &ensp; &emsp;</text>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				
			}
		},
		methods: {
			
		}
	}
</script>

<style>

</style>
