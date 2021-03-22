export ZSH=$HOME/.oh-my-zsh

export PATH="$HOME/bin:$HOME/.local/bin:/opt/bin/:/usr/local/bin:/usr/local/sbin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"
source /opt/intel/oneapi/setvars.sh intel64
export NETGENDIR="/opt/netgen/bin"
export NEOPZDIR="/opt/neopz"
export PATH=$NETGENDIR:$PATH
export VPNUNICAMP=$HOME/Documents/client.ovpn
export PYTHONPATH=".":$NETGENDIR/../`python3 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1,0,''))"`:$PYTHONPATH


export LD_LIBRARY_PATH="$LD_LIBRARY_PATH"
export CC=/usr/bin/clang
export CXX=/usr/bin/clang++
#i promise to start using a virtualenv in the future
alias python=python3
