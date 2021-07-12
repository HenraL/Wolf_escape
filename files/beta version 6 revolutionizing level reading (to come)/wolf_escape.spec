# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['wolf_escape.py', 'classes.py', 'constantes.py', 'liste.py'],
             pathex=['E:\\Henry PC\\Documents\\001 Github prog Sharing\\Wolf_escape\\files\\beta version 6 revolutionizing level reading (to come)'],
             binaries=[],
             datas=[],
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
          [],
          exclude_binaries=True,
          name='wolf_escape',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True , icon='wolf_icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='wolf_escape')
