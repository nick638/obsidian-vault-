@echo off
color 0A
echo ===================================================
echo   JARVIS OS - Scissor Motor V3 (Correcao Total)
echo ===================================================
echo.
echo [1/2] Verificando Bibliotecas (Sem forcar downgrades agressivos)...
pip install moviepy pillow imageio-ffmpeg edge-tts -q --upgrade
echo.
echo [2/2] Gerando Locucoes, Transicoes e Renderizando...
echo O Scissor esta trabalhando. Aguarde a mensagem de sucesso final.
python c:\Jarvis\DEV\scissor_render_v3.py
echo.
echo ===================================================
echo ✅ PROCESSO V3 CONCLUIDO!
echo Verifique se o video Holos_Premium_V3.mp4 esta na pasta: Downloads\video-dreamina
echo ===================================================
pause
