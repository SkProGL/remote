```powershell
cd C:\Users\g2-leonovs; curl.exe -L "https://github.com/SkProGL/remote/archive/refs/heads/main.zip" -o repo.zip; Expand-Archive repo.zip -Force; del repo.zip; cd repo/remote-main; .\setup.ps1
```
