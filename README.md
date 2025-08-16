# Transcribe

A small Python-based audio transcription utility. This project relies on FFmpeg for audio processing and a Python stack defined in requirements.txt.

Note: Because this README was authored without opening the script internals, usage examples are generic. If your script supports flags like -h/--help, run python transcribe.py --help to see all options. If you want this README tailored to your exact CLI, let me know and I’ll update it.

## Prerequisites

- Python 3.8+ (recommended 3.10 or newer)
- FFmpeg installed and available on your PATH

### Install FFmpeg

Verify first:

- Windows/macOS/Linux: ffmpeg -version

If the command is not found, install FFmpeg:

- Windows (preferred via package manager):
  - Using winget (Windows 10/11):
    - winget install Gyan.FFmpeg
  - Using Chocolatey:
    - choco install ffmpeg
  - Manual download:
    - Download a static build from https://www.gyan.dev/ffmpeg/builds/ (or https://ffmpeg.org/download.html), extract, and add the bin folder to your PATH.
  - After install, open a new terminal and run: ffmpeg -version

- macOS (Homebrew):
  - brew install ffmpeg

- Ubuntu/Debian:
  - sudo apt update && sudo apt install -y ffmpeg

- Fedora:
  - sudo dnf install -y ffmpeg

- Arch/Manjaro:
  - sudo pacman -S ffmpeg

### Add FFmpeg to PATH (Windows, if needed)

If ffmpeg is installed but not recognized, ensure the bin folder is in your PATH:

1) Press Win, search for "Environment Variables" and open "Edit the system environment variables".
2) Click "Environment Variables...".
3) Under "User variables" or "System variables", select Path -> Edit.
4) Add the full path to your FFmpeg bin folder (e.g., C:\\ffmpeg\\bin) and click OK.
5) Restart your terminal and run ffmpeg -version again.

## Project Setup

Using PowerShell (Windows):

- Create and activate a virtual environment
  - py -3 -m venv venv
  - .\venv\Scripts\Activate.ps1
  - Optional: python -m pip install --upgrade pip

- Install dependencies
  - pip install -r requirements.txt

Using bash (macOS/Linux):

- Create and activate a virtual environment
  - python3 -m venv venv
  - source venv/bin/activate
  - Optional: python -m pip install --upgrade pip

- Install dependencies
  - pip install -r requirements.txt

## Usage

Basic example (PowerShell on Windows):

- Activate the venv if not already active:
  - .\venv\Scripts\Activate.ps1

- Transcribe an audio file:
  - python transcribe.py path\to\audio.wav
  - python transcribe.py transcript.wav   # example using the sample provided here

Basic example (bash on macOS/Linux):

- source venv/bin/activate
- python transcribe.py path/to/audio.wav

Tips:

- If your input is not WAV, FFmpeg can convert it:
  - ffmpeg -i input.mp3 -ac 1 -ar 16000 input.wav
  - This converts to mono, 16 kHz, which many STT models prefer.
- If the script supports -h/--help, run:
  - python transcribe.py --help

## Troubleshooting

- "ffmpeg: command not found" or "The term 'ffmpeg' is not recognized":
  - Install FFmpeg (see above) and verify ffmpeg -version in a new terminal.
  - On Windows, ensure the bin directory is on PATH.

- PowerShell execution policy prevents venv activation:
  - In the current session: Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
  - Then: .\venv\Scripts\Activate.ps1

- Missing Python packages:
  - Ensure you installed dependencies inside the venv: pip install -r requirements.txt

- Audio format issues:
  - Try normalizing/convert with FFmpeg (mono, 16 kHz): ffmpeg -i input.ext -ac 1 -ar 16000 input.wav

## Development

- Lint/format (if configured in requirements):
  - ruff .
  - black .
  - flake8 .

- Run tests (if present):
  - pytest -q

## License

Add your license choice here (e.g., MIT).
