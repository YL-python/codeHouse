# button 元素

`<button>`元素继承了`HTMLButtonElement`接口。它有以下的实例属性。

**（1）HTMLButtonElement.accessKey**

`HTMLButtonElement.accessKey`属性返回一个字符串，表示键盘上对应的键，通过`Alt + 这个键`可以让按钮获得焦点。该属性可读写。

**（2）HTMLButtonElement.autofocus**

`HTMLButtonElement.autofocus`属性是一个布尔值，表示页面加载过程中，按钮是否会自动获得焦点。该属性可读写。

**（3）HTMLButtonElement.disabled**

`HTMLButtonElement.disabled`属性是一个布尔值，表示该按钮是否禁止点击。该属性可读写。

**（4）HTMLButtonElement.form**

`HTMLButtonElement.form`属性是一个表单元素，返回该按钮所在的表单。该属性只读。如果按钮不属于任何表单，该属性返回`null`。

**（5）HTMLButtonElement.formAction**

`HTMLButtonElement.formAction`返回一个字符串，表示表单提交的 URL。该属性可读写，一旦设置了值，点击按钮就会提交到该属性指定的 URL，而不是`<form>`元素指定的 URL。

**（6）HTMLButtonElement.formEnctype**

`HTMLButtonElement.formEnctype`属性是一个字符串，表示数据提交到服务器的编码类型。该属性可读写，一旦设置了值，点击按钮会按照该属性指定的编码方式，而不是`<form>`元素指定的编码方式。

该属性可以取以下的值。

- `application/x-www-form-urlencoded`（默认值）
- `multipart/form-data`（上传文件的编码方式）
- `text/plain`

**（7）HTMLButtonElement.formMethod**

`HTMLButtonElement.formMethod`属性是一个字符串，表示浏览器提交表单的 HTTP 方法。该属性可读写，一旦设置了值，点击后就会采用该属性指定的 HTTP 方法，而不是`<form>`元素指定的编码方法。

**（8）HTMLButtonElement.formNoValidate**

`HTMLButtonElement.formNoValidate`属性是一个布尔值，表示点击按钮提交表单时，是否要跳过表单校验的步骤。该属性可读写，一旦设置会覆盖`<form>`元素的`novalidate`属性。

**（9）HTMLButtonElement.formTarget**

`HTMLButtonElement.formTarget`属性是一个字符串，指定了提交了表单以后，哪个窗口展示服务器返回的内容。该属性可读写，一旦设置会覆盖`<form>`元素的`target`属性。

**（10）HTMLButtonElement.labels**

`HTMLButtonElement.labels`返回`NodeList`实例，表示那些绑定按钮的`<label>`元素。该属性只读。

```
/* HTML 代码如下
  <label id="label1" for="test">Label 1</label>
  <button id="test">Button</button>
  <label id="label2" for="test">Label 2</label>
*/

const button = document.getElementById('test');

for(var i = 0; i < button.labels.length; i++) {
  console.log(button.labels[i].textContent);
}
// "Label 1"
// "Label 2"
```

上面代码中，两个`<label>`元素绑定`<button>`元素。`button.labels`返回这两个`<label>`元素。

**（11）HTMLButtonElement.name**

`HTMLButtonElement.name`属性是一个字符串，表示按钮元素的`name`属性。如果没有设置`name`属性，则返回空字符串。该属性可读写。

**（12）HTMLButtonElement.tabIndex**

`HTMLButtonElement.tabIndex`是一个整数，代表按钮元素的 Tab 键顺序。该属性可读写。

**（13）HTMLButtonElement.type**

`HTMLButtonElement.type`属性是一个字符串，表示按钮的行为。该属性可读写，可能取以下的值。

- `submit`：默认值，表示提交表单。
- `reset`：重置表单。
- `button`：没有任何默认行为。

**（14）HTMLButtonElement.validationMessage**

`HTMLButtonElement.validationMessage`属性是一个字符串，表示没有通过校验时显示的提示信息。该属性只读。

**（15）HTMLButtonElement.validity**

`HTMLButtonElement.validity`属性返回该按钮的校验状态（`ValidityState`）。该属性只读。

**（16）HTMLButtonElement.value**

`HTMLButtonElement.value`属性返回该按钮绑定的值。该属性可读写。

**（17）HTMLButtonElement.willValidate**

`HTMLButtonElement.willValidate`属性是一个布尔值，表示该按钮提交表单时是否将被校验，默认为`false`。该属性只读。

# option 元素

> `<option>`元素表示下拉框（`<select>`，`<optgroup>`或`<datalist>`）里面的一个选项。它是 HTMLOptionElement 接口的实例。

## 属性

除了继承 HTMLElement 接口的属性和方法，HTMLOptionElement 接口具有下面的属性。

- `disabled`：布尔值，表示该项是否可选择。
- `defaultSelected`：布尔值，表示该项是否默认选中。一旦设为`true`，该项的值就是`<select>`的默认值。
- `form`：返回`<option>`所在的表单元素。如果不属于任何表单，则返回`null`。该属性只读。
- `index`：整数，表示该选项在整个下拉列表里面的位置。该属性只读。
- `label`：字符串，表示对该选项的说明。如果该属性未设置，则返回该选项的文本内容。
- `selected`：布尔值，表示该选项是否选中。
- `text`：字符串，该选项的文本内容。
- `value`：字符串，该选项的值。表单提交时，上传的就是选中项的这个属性。

## Option() 构造函数

浏览器原生提供`Option()`构造函数，用来生成 HTMLOptionElement 实例。

```
new Option(text, value, defaultSelected, selected)
```

它接受四个参数，都是可选的。

- text：字符串，表示该选项的文本内容。如果省略，返回空字符串。
- value：字符串，表示该选项的值。如果省略，默认返回`text`属性的值。
- defaultSelected：布尔值，表示该项是否默认选中，默认为`false`。注意，即使设为`true`，也不代表该项的`selected`属性为`true`。
- selected：布尔值，表示该项是否选中，默认为`false`。

```
var newOption = new Option('hello', 'world', true);

newOption.text // "hello"
newOption.value // "world"
newOption.defaultSelected // true
newOption.selected // false
```

上面代码中，`newOption`的`defaultSelected`属性为`true`，但是它没有被选中（即`selected`属性为`false`）。