powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
uv venv --python 3.11 --clear
$env:Path = "C:\Users\g2-leonovs\.local\bin;$env:Path"
. .\.venv\Scripts\activate
uv pip install -r requirements.txt
python main.py
$env:CUSTOM_MSVC = [Environment]::GetEnvironmentVariable("CUSTOM_MSVC","User")
$env:CUSTOM_WINSDK = [Environment]::GetEnvironmentVariable("CUSTOM_WINSDK","User")
cp rclone/rclone.conf C:\Users\g2-leonovs\AppData\Roaming\rclone\rclone.conf
