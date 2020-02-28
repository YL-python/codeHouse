@rem 这里是注释
:: 这样也是注释

::每个指令都是可以在黑窗口上看见的 用@符号可以隐藏指令
@title redis启动器

::@echo XXX   给出提示语句 类似print 
@echo 正在为您打开 redis

::start 命令参数很多建议百度
::/min表示最小化启动
:: 语句里面的分号不能少
::start "" "D:\Notepad++\notepad++.exe"
::等价于start /min "D:\Notepad++\" notepad++.exe

start /low "" "D:\Notepad++\notepad++.exe"
@echo qidon------------------
start /high "" "D:\Sublime\Sublime Text 3\sublime_text.exe"

::@D:\Notepad++\notepad++.exe

@echo 开启成功

::暂停操作 /T设置暂停时间 -1是无限暂停
:: 暂停的时候可以按任意键结束暂停
::  /NOBREAK 参数取消按任意键结束暂停只能用 ctrl+C来提前暂停
::@echo 开始暂停
::TIMEOUT /T 300
::TIMEOUT /T 300 /NOBREAK
::@echo 暂停结束

::@echo 开始暂停
::echo CreateObject("Scripting.FileSystemObject").DeleteFile(WScript.ScriptFullName) >%Temp%\Wait.vbs
::echo wscript.sleep 2000 >>%Temp%\Wait.vbs
::start /wait %Temp%\Wait.vbs
::@echo 暂停结束


::pause暂停窗口
pause

::exit退出窗口
::exit