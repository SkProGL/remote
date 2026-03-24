echo "[python] setting up env"
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
cd C:\Users\g2-leonovs
uv venv --python 3.11 --clear
$env:Path = "C:\Users\g2-leonovs\.local\bin;$env:Path"

. .\.venv\Scripts\activate
cd repo\remote-main
python main.py
$env:CUSTOM_MSVC = [Environment]::GetEnvironmentVariable("CUSTOM_MSVC","User")
$env:CUSTOM_WINSDK = [Environment]::GetEnvironmentVariable("CUSTOM_WINSDK","User")

New-Item -ItemType Directory -Path "C:\Users\g2-leonovs\AppData\Roaming\rclone" -ErrorAction SilentlyContinue
$target = "C:\Users\g2-leonovs\AppData\Roaming\rclone\rclone.conf"
if (-not (Test-Path $target)) {
    echo "[rclone] not setup, copying config"
    Copy-Item .\rclone.conf $target -Force
    rclone\rclone.exe config
}

echo "done."
