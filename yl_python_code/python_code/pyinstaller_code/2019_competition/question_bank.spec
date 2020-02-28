# -*- mode: python -*-

block_cipher = None


a = Analysis(['question_bank.py'],
             pathex=['read_code.py', 'E:\\PyCharm2019\\python_code\\pyinstaller_code\\2019_competition'],
             binaries=[],
             datas=[],
             hiddenimports=['read_code', 'question'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='question_bank',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='question.ico')
