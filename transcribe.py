import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from pathlib import Path
import whisper

# Load model once
model = whisper.load_model("turbo")

# Current folder
root = Path(".").resolve()

# Output subdirectory inside current folder
out_dir = root / "transcripts"
out_dir.mkdir(exist_ok=True)

# Media extensions to process
media_exts = {".mp4", ".mp3", ".m4a", ".wav", ".mov", ".mkv"}

for media_file in root.iterdir():
    if not media_file.is_file():
        continue
    if media_file.suffix.lower() not in media_exts:
        continue

    out_file = out_dir / f"{media_file.stem}.txt"

    if out_file.exists():
        print(f"Skipping {media_file.name} (transcript already exists)")
        continue

    print(f"Transcribing {media_file.name}...")
    result = model.transcribe(str(media_file))
    out_file.write_text(result["text"], encoding="utf-8")
    print(f"Saved {out_file}")
