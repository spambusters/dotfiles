# Path to your oh-my-zsh installation.
export ZSH=$HOME/.oh-my-zsh

# Set name of the theme to load. Optionally, if you set this to "random"
# it'll load a random theme each time that oh-my-zsh is loaded.
# See https://github.com/robbyrussell/oh-my-zsh/wiki/Themes
ZSH_THEME="robbyrussell"

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
plugins=(git)

source $ZSH/oh-my-zsh.sh

export PATH=$PATH:$HOME/Downloads/PhantomJS/bin/

alias vim="nvim"

alias mp3="youtube-dl -x --audio-format mp3"
alias youtube="mpv --ytdl-format 22"
alias twitch="mpv --ytdl-format 720p"

alias update="sudo pacman -Syy"
alias upgrade="sudo pacman -Su"

alias backup="rsync -aP $HOME/Data/media/ /media/veracrypt1/media/"
