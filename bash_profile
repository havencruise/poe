PS1='[\u@\h \W]\$ '
export CLICOLOR=1;
export PATH=/usr/local/bin:/usr/local/mysql/bin:$HOME/android-sdk-macosx/platform-tools:$HOME/android-sdk-macosx/tools:$PATH
export PYTHONSTARTUP=$HOME/.python_rc.py
export NODE_PATH="/usr/local/lib/node_modules"
alias ll='ls -lhF'
alias la='ls -A'
alias l='ls -CF'
alias vi='vim'
alias grep='grep --color=auto'
alias subl='/Applications/Sublime\ Text\ 2.app/Contents/SharedSupport/bin/subl'
alias chrome_debug='adb forward tcp:9222 localabstract:chrome_devtools_remote'
alias serv_here='$HOME/Projects/poe/server.py'