@echo off
echo ========================================
echo   GERANDO APLICATIVO CURSO DE UMBANDA
echo ========================================
echo.

REM Criar pasta app se nao existir
if not exist "app" mkdir app

echo Gerando arquivos do app...
echo.

REM Copiar arquivos base
copy /Y index.html app\index.html >nul 2>&1

echo.
echo ARQUIVOS CRIADOS:
echo =================
dir /b app\

echo.
echo.
echo ========================================
echo   PROXIMOS PASSOS - PUBLICAR O APP
echo ========================================
echo.
echo 1. PUBLIQUE no GitHub Pages (gratuito):
echo    - Crie um repositorio no GitHub
echo    - Faça upload dos arquivos da pasta app/
echo    - Ative o GitHub Pages nas configuracoes
echo    - O app ficara disponivel em: seu-usuario.github.io/repositorio
echo.
echo 2. Netlify (gratuito):
echo    - Acesse netlify.com
echo    - Arraste a pasta app/ para publicar
echo    - Receba um link para o app
echo.
echo 3. Para Google Play Store:
echo    - Compile o app com Capacitor/Flutter
echo    - Crie conta de desenvolvedor (one-time fee)
echo    - Faca upload do APK
echo.
echo 4. Para Apple App Store:
echo    - Compile com Capacitor/Flutter
echo    - Crie conta Apple Developer ($99/ano)
echo    - Faca upload pelo App Store Connect
echo.
echo ========================================
pause
