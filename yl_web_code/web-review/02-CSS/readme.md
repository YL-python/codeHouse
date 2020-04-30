# CSS复习

## css背景属性-Background

```
+ background：在一个声明中设置所有的背景属性。
+ background-attachment：属性设置背景图像是否固定或者随着页面的其余部分滚动。
	scroll	默认值。背景图像会随着页面其余部分的滚动而移动。根据当前容器进行定位。
	fixed	当页面的其余部分滚动时，背景图像不会移动。根据当前页面进行定位。
+ background-color：属性设置元素的背景颜色。
	默认是透明颜色。
	可以是颜色名称（red,blue），可以是十六进制，可以是rgb，也可以是rgba
+ background-image：设置元素的背景图像。
	默认是没有，使用 background-image: url('URL')；指向图像的路径。
	默认地，背景图像位于元素的左上角，并在水平和垂直方向上重复。
+ background-position：设置背景图像的开始位置。
	默认值是 0% 0%。
	可以是名称（top left center right bottom ），需要设置两个值，写一个的时候，后面一个默认是center
	可以是百分比 x% y%
	可以是具体的像素值 10px 5px
+ background-repeat：设置是否及如何重复背景图像。
	repeat	默认。背景图像将在垂直方向和水平方向重复。
    repeat-x	背景图像将在水平方向重复。
    repeat-y	背景图像将在垂直方向重复。
    no-repeat	背景图像将仅显示一次。
+ background-clip：规定背景的绘制区域。
	border-box	默认值,背景被裁剪到边框盒。
    padding-box	背景被裁剪到内边距框。
    content-box	背景被裁剪到内容框。
+ background-origin：规定背景图片的定位区域。
	padding-box	默认值,背景图像相对于内边距框来定位。
    border-box	背景图像相对于边框盒来定位。	
    content-box	背景图像相对于内容框来定位。
    background-attachment 属性为 "fixed"，则该属性没有效果。
+ background-size：规定背景图片的尺寸。
	100px 100px	 设置背景图像的宽度喝高度。如果只设置一个值，则第二个值会被设置为 "auto"。
    50% 50%  以父元素的百分比来设置背景图像的宽度和高度。
    cover	 把背景图像扩展至足够大，容器等比例方法，背景会超出容器
    contain	把图像图像扩展至最大尺寸，以使其宽度和高度完全适应内容区域。最大不会超出容器，会有白边
```

##  CSS 边框属性（Border 和 Outline）

```
+ border：在一个声明中设置所有的边框属性。
+ border-color：设置四条边框的颜色。
+ border-style：设置四条边框的样式。
+ border-width：设置四条边框的宽度。
+ border-top/bottom/left/right-width/style/color：设置四个方向的三个属性
+ border-radius：圆角简写属性
	设置所有四个 border-*-radius 属性。可以是具体像素，也可以是百分比
	可以单独设置某个角的圆角属性
+ box-shadow：向方框添加一个或多个阴影。
	box-shadow: h-shadow v-shadow blur spread color inset;
	h-shadow	必需。水平阴影的位置。允许负值。
    v-shadow	必需。垂直阴影的位置。允许负值。
    blur	可选。模糊距离。
    spread	可选。阴影的尺寸。
    color	可选。阴影的颜色。请参阅 CSS 颜色值。
    inset	可选。将外部阴影 (outset) 改为内部阴影。
    该属性是由逗号分隔的阴影列表，每个阴影由 2-4 个长度值、可选的颜色值以及可选的 inset 关键词来规定。
+ border-image：将图片规定为包围 div 元素的边框。
	border-image-source	用在边框的图片的路径。	
    border-image-slice	图片边框向内偏移。	
    border-image-width	图片边框的宽度。	
    border-image-outset	边框图像区域超出边框的量。	
    border-image-repeat	图像边框是否应平铺(repeated)、铺满(rounded)或拉伸(stretched)。
```

## CSS 尺寸属性（Dimension）

```
+ height：设置元素高度。
+ width：设置元素的宽度。
+ + max-height：设置元素的最大高度。
+ max-width：设置元素的最大宽度。
+ min-height：设置元素的最小高度。
+ min-width：设置元素的最小宽度。
```

## CSS 字体属性（Font）

```
+ font：在一个声明中设置所有字体属性。	
+ font-family：规定文本的字体系列。
	font-family:"Times New Roman",Georgia,Serif;
+ font-size：规定文本的字体尺寸。
+ font-style：规定文本的字体样式。
    normal	默认值。浏览器显示一个标准的字体样式。
    italic	浏览器会显示一个斜体的字体样式。
    oblique	浏览器会显示一个倾斜的字体样式。
+ font-weight：规定字体的粗细。
    normal	默认值。定义标准的字符。
    bold	定义粗体字符。
    bolder	定义更粗的字符。
    lighter	定义更细的字符。
    可以是数值100-900，400 等同于 normal，而 700 等同于 bold。
```

## CSS 文本属性（Text）

```
+ color：设置文本的颜色。
+ direction：规定文本的方向 / 书写方向。
	ltr	默认。文本方向从左到右。rtl	文本方向从右到左。
+ letter-spacing：设置字符间距。数值，5px,1rem
+ line-height：设置行高。
+ text-align：规定文本的水平对齐方式。
+ text-decoration：规定添加到文本的装饰效果。
	none	默认。定义标准的文本。
    underline	文本下划线。
    overline	文本下划线。
    line-through	穿过文本下的一条线。
    blink	定义闪烁的文本。
+ text-indent：规定文本块首行的缩进。
+ text-transform：控制文本的大小写。
	none	默认。定义带有小写字母和大写字母的标准的文本。
    capitalize	文本中的每个单词以大写字母开头。
    uppercase	定义仅有大写字母。
    lowercase	定义无大写字母，仅有小写字母。
+ text-overflow：规定当文本溢出包含元素时发生的事情。
    clip	默认修剪文本。	
    ellipsis	显示省略符号来代表被修剪的文本。
    string	使用给定的字符串来代表被修剪的文本。
```

## 定位

```
+ display：属性规定元素应该生成的框的类型。
	none	此元素不会被显示。
    block	此元素将显示为块级元素，此元素前后会带有换行符。
    inline	默认。此元素会被显示为内联元素，元素前后没有换行符。
    inline-block	行内块元素。（CSS2.1 新增的值）
    table-cell	此元素会作为一个表格单元格显示（类似 <td> 和 <th>）
     。。。还有很多，list-item，run-in，compact，marker，table，inline-table，table-row-group	，table-header-group，table-footer-group，table-row，table-column-group，table-column，table-cell	，table-caption，inherit
+ visibility：规定元素是否可见。
    visible	默认值。元素是可见的。
    hidden	元素是不可见的。
+ overflow：规定当内容溢出元素框时发生的事情。
    visible	默认值。内容不会被修剪，会呈现在元素框之外。
    hidden	内容会被修剪，并且其余内容是不可见的。
    scroll	内容会被修剪，但是浏览器会显示滚动条以便查看其余的内容。
    auto	如果内容被修剪，则浏览器会显示滚动条以便查看其余的内容。
+ float：规定框是否应该浮动。
	以往这个属性总应用于图像，使文本围绕在图像周围，不过在 CSS 中，任何元素都可以浮动。**浮动元素会生成一个块级框**，而不论它本身是何种元素。
+ clear：规定元素的哪一侧不允许其他浮动元素。
+ position：规定元素的定位类型。
	这个属性定义建立元素布局所用的定位机制。任何元素都可以定位，**不过绝对或固定元素会生成一个块级框**，而不论该元素本身是什么类型。相对定位元素会相对于它在正常流中的默认位置偏移。
	static	默认值。没有定位，元素出现在正常的流中
	absolute	生成绝对定位的元素，相对于 static 定位以外的第一个父元素进行定位。
    relative	生成相对定位的元素，相对于其正常位置进行定位。
    fixed	生成绝对定位的元素，相对于浏览器窗口进行定位。
    sticky : 黏性定位 没有到达指定位置的时候，是没有定位效果的，到达了指定位置，就变成了固定模式。
+ bottom/left/right/top：设置定位元素bottom/left/right/top外边距边界与其包含块bottom/left/right/top边界之间的偏移。
```

## CSS3 2D转换-transform

> 通过 CSS3 转换，我们能够对元素进行移动、缩放、转动、拉长或拉伸。

```
transform	向元素应用 2D 或 3D 转换。
transform-origin	允许你改变被转换元素的位置（基点）
	默认值是 center center就是元素中心位置
	0px,0px就是元素左上角

translate(x,y)	位移，沿着 X 和 Y 轴移动元素。
scale(x,y)	缩放，改变元素的宽度和高度。
rotate(angle)	旋转，在参数中规定角度。
skew(x-angle,y-angle)	倾斜转换，沿着 X 和 Y 轴。
```

## CSS 过度-transition

```
transition	简写属性，用于在一个属性中设置四个过渡属性。	
transition-property	规定应用过渡的 CSS 属性的名称。
	none	没有属性会获得过渡效果。
    all	默认值所有属性都将获得过渡效果。
    property	定义应用过渡效果的 CSS 属性名称列表，列表以逗号分隔。
transition-duration	定义过渡效果花费的时间。默认是 0。	
transition-timing-function	规定过渡效果的时间曲线。默认是 "ease"。
    linear	规定以相同速度开始至结束的过渡效果（等于 cubic-bezier(0,0,1,1)）。
    ease	规定慢速开始，然后变快，然后慢速结束的过渡效果（cubic-bezier(0.25,0.1,0.25,1)）。
    ease-in	规定以慢速开始的过渡效果（等于 cubic-bezier(0.42,0,1,1)）。
    ease-out	规定以慢速结束的过渡效果（等于 cubic-bezier(0,0,0.58,1)）。
    ease-in-out	规定以慢速开始和结束的过渡效果（等于 cubic-bezier(0.42,0,0.58,1)）。
    cubic-bezier(n,n,n,n)	在 cubic-bezier 函数中定义自己的值。可能的值是 0 至 1 之间的数值。
transition-delay	规定过渡效果何时开始。默认是 0。
```

## CSS动画-animation

```
使用 @keyframes定义一个动画
@keyframes myMove {
    0% { transform:translate(0,0); }
    25%{ transform:translate(300px,0); }
    50%{ transform:translate(300px,300px); }
    75%{ transform:translate(0,300px); }
    100% { transform:translate(0,0);}
}
animation	所有动画属性的简写属性，除了 animation-play-state 属性。	
animation-name	规定 @keyframes 动画的名称。	
animation-duration	规定动画完成一个周期所花费的秒（s）或毫秒(ms)。默认是 0。	
animation-iteration-count	规定动画被播放的次数。默认是 1。	
	n	定义动画播放次数的数值。
    infinite 规定动画应该无限次播放。
animation-delay	规定动画的延迟时间
animation-direction	规定动画是否在下一周期逆向地播放。默认是 "normal"。	
	alternate  :  一次正向(0%~100%)，一次反向(100%~0%)
    reverse : 永远都是反向 , 从100%~0%
    normal (默认值) : 永远都是正向 , 从0%~100%
animation-fill-mode	规定对象动画时间之外的状态。
    none (默认值) : 在运动结束之后回到初始位置，在延迟的情况下，让0%在延迟后生效
    backwards  :  在延迟的情况下，让0%在延迟前生效
    forwards  :  在运动结束的之后，停到结束位置
    both  :  backwards和forwards同时生效
animation-timing-function	规定动画的速度曲线。默认是 "ease"。	
animation-play-state	规定动画是否正在运行或暂停。默认是 "running"。	
```

## CSS3 3D转换-transform

