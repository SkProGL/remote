```powershell
cd C:\Users\g2-leonovs; curl.exe -L "https://github.com/SkProGL/remote/archive/refs/heads/main.zip" -o repo.zip; Expand-Archive repo.zip -Force; del repo.zip; cd repo/remote-main; .\setup.ps1
```


```powershell
cd C:\Users\g2-leonovs; curl.exe -L "https://github.com/SkProGL/experimental_dragon_hatchling/archive/refs/heads/main.zip" -o bdh.zip; Expand-Archive bdh.zip -Force; del bdh.zip; Move-Item .\bdh\experimental_dragon_hatchling-main .\repo\remote-main\ -Force; cd .\repo\remote-main\experimental_dragon_hatchling-main; `
.\setup.ps1
```
