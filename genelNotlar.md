

# Sanal Ortam

## Kurulum

### dilediğin bir isimlendirme örn. virtualEnv
python -m venv virtualEnv

### Sanal ortam geliştirmek için. Bu tek seferlik çalıştırılan ExecutionPolicy kuralını atlatmak için birer kod.
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted

## Çalıştırma

### Posix
	
bash/zsh
source <venv>/bin/activate
	
fish
. <venv>/bin/activate.fish
	
csh/tcsh
source <venv>/bin/activate.csh

### Windows os

cmd.exe
C:\> <venv>\Scripts\activate.bat

PowerShell
PS C:\> <venv>\Scripts\Activate.ps1