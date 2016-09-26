PS1='[\u@\h \W]\$ '
export CLICOLOR=1;
export PATH=/usr/local/bin:/usr/local/sbin:/usr/local/mysql/bin:./node_modules/.bin:$PATH
export PYTHONSTARTUP=$HOME/.python_rc.py
export NODE_PATH="/usr/local/lib/node_modules"
export DYLD_LIBRARY_PATH=/usr/local/mysql/lib
export HOMEBREW_GITHUB_API_TOKEN="40bf1df1de7b0e36631d1f5c67cbf2c7841cda7b"
alias ll='ls -lhF'
alias la='ls -A'
alias l='ls -CF'
alias vi='vim'
alias grep='grep --color=auto'
alias serv_here='$HOME/Projects/poe/server.py'
alias subl='$HOME/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl'
alias pyenv='$HOME/virtualenv-master/virtualenv.py'

if [ -f $(brew --prefix)/etc/bash_completion ]; then
    . $(brew --prefix)/etc/bash_completion
fi
export DOCKER_HOST=tcp://192.168.99.100:2376
export DOCKER_CERT_PATH=/Users/ppadmanabh/.docker/machine/machines/default
export DOCKER_TLS_VERIFY=1
