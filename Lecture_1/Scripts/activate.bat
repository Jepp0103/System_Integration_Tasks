@echo off
set "VIRTUAL_ENV=C:\Users\Jeppe N. Dyekjær\Documents\4.Softwareudvikling_KEA\6. Semester\Git_Projekter\System_Integration_Tasks"

if not defined PROMPT (
    set "PROMPT=$P$G"
)

if defined _OLD_VIRTUAL_PROMPT (
    set "PROMPT=%_OLD_VIRTUAL_PROMPT%"
)

if defined _OLD_VIRTUAL_PYTHONHOME (
    set "PYTHONHOME=%_OLD_VIRTUAL_PYTHONHOME%"
)

set "_OLD_VIRTUAL_PROMPT=%PROMPT%"
set "PROMPT=(System_Integration_Tasks) %PROMPT%"

if defined PYTHONHOME (
    set "_OLD_VIRTUAL_PYTHONHOME=%PYTHONHOME%"
    set PYTHONHOME=
)

if defined _OLD_VIRTUAL_PATH (
    set "PATH=%_OLD_VIRTUAL_PATH%"
) else (
    set "_OLD_VIRTUAL_PATH=%PATH%"
)

set "PATH=%VIRTUAL_ENV%\Scripts;%PATH%"

:END
