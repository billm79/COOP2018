# -*- mode: python -*-

block_cipher = None


a = Analysis(['U10_Ex02_Babysitter.py'],
             pathex=['/Users/bill/PycharmProjects/COOP2017/Chapter10'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='U10_Ex02_Babysitter',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='icon-windowed.icns')
app = BUNDLE(exe,
             name='U10_Ex02_Babysitter.app',
             icon='icon-windowed.icns',
             bundle_identifier=None)
