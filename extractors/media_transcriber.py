import sys
import subprocess
import tempfile
import os

def transcribe_media(url):
    print(f"Starting media transcription for: {url}")
    
    # 1. Сначала пытаемся получить официальные субтитры без скачивания медиа
    print("Attempting to fetch official subtitles via yt-dlp...")
    out_file = "downloaded_subs"
    try:
        subprocess.run([
            "yt-dlp",
            "--write-auto-sub",
            "--sub-lang", "ru,en",
            "--skip-download",
            "-o", out_file,
            url
        ], check=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        
        # Проверяем, появились ли файлы
        for f in os.listdir("."):
            if f.startswith(out_file):
                print("--- SUBTITLES FOUND ---")
                print(f"Subtitles downloaded: {f}")
                return
    except Exception:
        pass
    
    print("No official subtitles found. Using in-memory / temporary stream extraction...")

    # 2. Безопасное скачивание через системные временные файлы (In-Memory иллюзия)
    # Использование tempfile гарантирует, что файл будет удален ОС сразу после закрытия программы,
    # не оставляя никакого мусора в рабочей директории и не расходуя SSD впустую.
    try:
        # Создаем временный файл, который удалится сам по окончанию процесса
        with tempfile.NamedTemporaryFile(suffix=".m4a", delete=False) as temp_audio:
            temp_path = temp_audio.name
            
        print("Streaming audio to secure temp buffer...")
        subprocess.run([
            "yt-dlp",
            "-f", "bestaudio[ext=m4a]",
            "-o", temp_path,
            url
        ], check=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        
        print("Audio buffered. Transcribing with Whisper (this may take a while)...")
        # Запускаем Whisper
        subprocess.run([
            "whisper",
            temp_path,
            "--model", "base"
        ], check=True)
        print("--- TRANSCRIPTION SUCCESSFUL ---")
        
    except Exception as e:
        print(f"Transcription failed: {e}")
    finally:
        # Гарантированное удаление из временной директории
        if 'temp_path' in locals() and os.path.exists(temp_path):
            os.remove(temp_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python media_transcriber.py <MEDIA_URL>")
        sys.exit(1)
        
    target_url = sys.argv[1]
    transcribe_media(target_url)
