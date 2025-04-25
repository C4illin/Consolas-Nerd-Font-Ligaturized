# Consolas-Nerd-Font-Ligaturized

Consolas is property of Microsoft so it can't be redistributed here. But it is included in all versions of Windows. Here is a script to patch it. This can probably be used with other fonts too.

## How to use

1. Install git, fontforge and python3 eg with `winget install Git.Git FontForge.FontForge Python3`. Add FontForge bin folder to PATH.
2. Clone this repo with `git clone --recurse-submodules --remote-submodules https://github.com/C4illin/Consolas-Nerd-Font-Ligaturized.git` (this will take a while)
3. Locate the four Consolas font files on your system and copy them to `Original`. They are usually located in `C:\Windows\Fonts` and are named `consola.ttf`, `consolab.ttf`, `consolai.ttf` and `consolaz.ttf`. Here you can actually drop any font you want to patch, but do them one at a time.
4. Install `requests` from pip and run `python patch.py`
5. Install the patched font from the `Output` folder

### Use in VSCode

1. Set `"editor.fontFamily": "'LigaConsola Nerd Font', ...`
2. Set `"editor.fontLigatures": true,`
3. You may also set `"debug.console.fontFamily":` and `"terminal.integrated.fontFamily":`

## Update

1. Run `git pull`
2. Run `git submodule update --recursive --remote`
3. Run `python patch.py` which will also update the Nerd Font patcher
