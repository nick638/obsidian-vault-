import os
import traceback
import subprocess
import PIL.Image

# Patch de segurança para compatibilidade de versões do Pillow/MoviePy
if not hasattr(PIL.Image, 'ANTIALIAS'):
    PIL.Image.ANTIALIAS = PIL.Image.LANCZOS

try:
    print("🎬 Scissor V3: Adaptando motor para o Python 3.13 (Latest)...")
    try:
        # Tenta sintaxe MoviePy 2.x
        from moviepy import ImageClip, VideoFileClip, AudioFileClip, concatenate_videoclips, vfx
        IS_V2 = True
    except ImportError:
        # Fallback para 1.x se instalado
        from moviepy.editor import ImageClip, VideoFileClip, AudioFileClip, concatenate_videoclips, vfx
        IS_V2 = False

    from PIL import ImageDraw, ImageFont

    folder = r"C:\Users\lugzi\Downloads\video-dreamina"
    files = sorted([f for f in os.listdir(folder) if f.endswith(('.jpeg', '.mp4'))])

    texts = [
        "Você já teve aquela sensação...",
        "De que a vida está no piloto automático?",
        "E a culpa que bate quando você pensa...",
        "Isso é tudo que existe para mim?",
        "A verdade que ninguém te conta...",
        "Você não está perdido.",
        "Você só vive uma vida que não é sua.",
        "Existe outro caminho. Descubra a Holos."
    ]

    clips = []
    target_size = (1080, 1920)

    for i, file in enumerate(files):
        path = os.path.join(folder, file)
        text = texts[i] if i < len(texts) else ""
        
        # 1. GERAR LOCUÇÃO (VOICEOVER) COM EDGE-TTS
        audio_path = os.path.join(folder, f"audio_{i}.mp3")
        print(f"🎙️ Gravando locução da Cena {i+1}...")
        import sys
        subprocess.run([sys.executable, "-m", "edge_tts", "--voice", "pt-BR-AntonioNeural", "--text", text, "--write-media", audio_path])
        
        # Carrega o áudio gerado
        try:
            audio_clip = AudioFileClip(audio_path)
            scene_duration = audio_clip.duration + 0.5 
        except:
            scene_duration = 3.5
            audio_clip = None

        if file.endswith('.jpeg'):
            img = PIL.Image.open(path)
            img_ratio = img.width / img.height
            target_ratio = target_size[0] / target_size[1]
            
            if img_ratio > target_ratio:
                new_width = int(target_ratio * img.height)
                offset = (img.width - new_width) / 2
                img = img.crop((offset, 0, img.width - offset, img.height))
            else:
                new_height = int(img.width / target_ratio)
                offset = (img.height - new_height) / 2
                img = img.crop((0, offset, img.width, img.height - offset))
                
            img = img.resize(target_size, getattr(PIL.Image.Resampling, 'LANCZOS', PIL.Image.ANTIALIAS))
            draw = ImageDraw.Draw(img)
            
            try:
                font = ImageFont.truetype("arialbd.ttf", 60)
            except:
                font = ImageFont.load_default()
                
            x, y = 100, target_size[1] - 400
            draw.text((x+4, y+4), text, font=font, fill=(0,0,0))
            draw.text((x, y), text, font=font, fill=(255,255,255))
            
            temp_path = os.path.join(folder, f"temp_{i}.jpg")
            img.save(temp_path)
            
            # Criando o clipe
            clip = ImageClip(temp_path)
            if IS_V2:
                clip = clip.with_duration(scene_duration)
                if audio_clip: clip = clip.with_audio(audio_clip)
                try: clip = clip.with_effects([vfx.CrossFadeIn(1.0)])
                except: pass
            else:
                clip = clip.set_duration(scene_duration)
                if audio_clip: clip = clip.set_audio(audio_clip)
                try: clip = clip.crossfadein(1.0)
                except: pass
                
            clips.append(clip)
            print(f"✅ Cena {i+1} pronta: Áudio Sincronizado ({scene_duration:.1f}s).")
            
        elif file.endswith('.mp4'):
            clip = VideoFileClip(path)
            if IS_V2:
                clip = clip.with_duration(scene_duration)
                try: clip = clip.with_effects([vfx.CrossFadeIn(1.0)])
                except: pass
            else:
                clip = clip.set_duration(scene_duration)
                try: clip = clip.crossfadein(1.0)
                except: pass
                
            if audio_clip:
                clip = clip.with_audio(audio_clip) if IS_V2 else clip.set_audio(audio_clip)
            clips.append(clip)
            print(f"✅ Cena {i+1} pronta (Vídeo).")

    print("🔥 Scissor: Juntando transições e renderizando arquivo final...")
    final = concatenate_videoclips(clips, method="compose")
    
    output_path = os.path.join(folder, "Holos_Premium_V3.mp4")
    if IS_V2:
        final.write_videofile(output_path, fps=24, logger=None, audio_codec="aac")
    else:
        final.write_videofile(output_path, fps=24, logger=None, audio_codec="aac")

    # Limpeza de lixo temporário
    for i in range(len(files)):
        temp_path = os.path.join(folder, f"temp_{i}.jpg")
        audio_path = os.path.join(folder, f"audio_{i}.mp3")
        if os.path.exists(temp_path): os.remove(temp_path)
        if os.path.exists(audio_path): os.remove(audio_path)

    print(f"🚀 SUCESSO! Vídeo salvo em: {output_path}")

except Exception as e:
    with open(r"C:\Jarvis\DEV\render_error_v3.log", "w", encoding="utf-8") as f:
        f.write(traceback.format_exc())
    print("❌ ERRO! Log gravado em render_error_v3.log")
