@echo off
chcp 65001 >nul
echo === Creando ControlInventario.exe ===
where python >nul 2>nul || (echo Necesitas instalar Python desde python.org ^(marca "Add to PATH"^) & pause & exit /b)
python -m pip install --quiet pyinstaller
python -m PyInstaller --onefile --noconsole --name ControlInventario --add-data "inventario.html;." launcher.py
copy /Y dist\ControlInventario.exe . >nul
rmdir /S /Q build dist 2>nul
del ControlInventario.spec 2>nul
echo.
echo Listo: ControlInventario.exe creado en esta carpeta.
pause
