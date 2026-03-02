import os
VS_ROOT = r"C:\Program Files\Microsoft Visual Studio\2022\Professional"
# MSVC_VER = "14.44.35207"
MSVC_BASE = os.path.join(VS_ROOT, r"VC\Tools\MSVC")

MSVC_VER = next(
    v for v in os.listdir(MSVC_BASE)
    if v.startswith("14.44")
)


MSVC_BIN = rf"{VS_ROOT}\VC\Tools\MSVC\{MSVC_VER}\bin\Hostx64\x64"
MSVC_INC = rf"{VS_ROOT}\VC\Tools\MSVC\{MSVC_VER}\include"
MSVC_LIB = rf"{VS_ROOT}\VC\Tools\MSVC\{MSVC_VER}\lib\x64"

# WINSDK_VER = "10.0.26100.0"
WINSDK_BASE = r"C:\Program Files (x86)\Windows Kits\10"

WINSDK_INC_BASE = os.path.join(WINSDK_BASE, "Include")
WINSDK_VER = next(
    v for v in os.listdir(WINSDK_INC_BASE)
)

WINSDK_INC = rf"{WINSDK_BASE}\Include\{WINSDK_VER}"
WINSDK_LIB = rf"{WINSDK_BASE}\Lib\{WINSDK_VER}"

os.environ["PATH"] = MSVC_BIN + ";" + os.environ.get("PATH", "")

os.environ["INCLUDE"] = ";".join([
    MSVC_INC,
    WINSDK_INC + r"\ucrt",
    WINSDK_INC + r"\shared",
    WINSDK_INC + r"\um",
    WINSDK_INC + r"\winrt",
])

os.environ["LIB"] = ";".join([
    MSVC_LIB,
    WINSDK_LIB + r"\ucrt\x64",
    WINSDK_LIB + r"\um\x64",
])

os.environ["CC"] = "cl"
os.environ["CXX"] = "cl"

print(MSVC_VER)
print(WINSDK_VER)
