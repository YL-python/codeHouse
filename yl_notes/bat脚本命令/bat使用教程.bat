@rem ������ע��
:: ����Ҳ��ע��

::ÿ��ָ��ǿ����ںڴ����Ͽ����� ��@���ſ�������ָ��
@title redis������

::@echo XXX   ������ʾ��� ����print 
@echo ����Ϊ���� redis

::start ��������ܶཨ��ٶ�
::/min��ʾ��С������
:: �������ķֺŲ�����
::start "" "D:\Notepad++\notepad++.exe"
::�ȼ���start /min "D:\Notepad++\" notepad++.exe

start /low "" "D:\Notepad++\notepad++.exe"
@echo qidon------------------
start /high "" "D:\Sublime\Sublime Text 3\sublime_text.exe"

::@D:\Notepad++\notepad++.exe

@echo �����ɹ�

::��ͣ���� /T������ͣʱ�� -1��������ͣ
:: ��ͣ��ʱ����԰������������ͣ
::  /NOBREAK ����ȡ���������������ֻͣ���� ctrl+C����ǰ��ͣ
::@echo ��ʼ��ͣ
::TIMEOUT /T 300
::TIMEOUT /T 300 /NOBREAK
::@echo ��ͣ����

::@echo ��ʼ��ͣ
::echo CreateObject("Scripting.FileSystemObject").DeleteFile(WScript.ScriptFullName) >%Temp%\Wait.vbs
::echo wscript.sleep 2000 >>%Temp%\Wait.vbs
::start /wait %Temp%\Wait.vbs
::@echo ��ͣ����


::pause��ͣ����
pause

::exit�˳�����
::exit