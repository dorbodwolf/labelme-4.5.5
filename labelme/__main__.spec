# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['__main__.py'],
             pathex=['C:\\Users\\jadymayor\\Source\\Repos\\dorbodwolf\\labelme-4.5.5\\labelme-4.5.5\\labelme'],
             binaries=[],
             datas=[('C:\\Users\\jadymayor\\Source\\Repos\\dorbodwolf\\labelme-4.5.5\\labelme-4.5.5\\labelme\\icons', 'labelme\\icons'), 
			 ('C:\\Users\\jadymayor\\Source\\Repos\\dorbodwolf\\labelme-4.5.5\\labelme-4.5.5\\labelme\\translate', 'translate')],
             hiddenimports=[],
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
          name='__main__',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='main.ico')
