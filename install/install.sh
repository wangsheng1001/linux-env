# /usr/bin/env bash

COMMAND=apt-get
# COMMAND=yum

sudo $COMMAND install devtoolset-7 llvm-toolset-7
sudo $COMMAND install llvm-toolset-7-clang-analyzer llvm-toolset-7-clang-tools-extra # optional
sudo $COMMAND install -y cmake
sudo $COMMAND install -y vim astyle
sudo $COMMAND install -y default-jdk
sudo $COMMAND install -y exuberant-ctags
sudo $COMMAND install -y curl
sudo $COMMAND install -y tmux
