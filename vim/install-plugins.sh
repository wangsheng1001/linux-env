# install pathogen
mkdir -p ~/.vim/autoload ~/.vim/bundle && \
  curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim

# install NERDTree
cd ~/.vim/bundle && git clone https://github.com/scrooloose/nerdtree.git

# install TagBar
cd ~/.vim/bundle && git clone git://github.com/majutsushi/tagbar

# install CtrlP
cd ~/.vim/bundle && git clone https://github.com/ctrlpvim/ctrlp.vim.git

# install YCM
cd ~/.vim/bundle && git clone https://github.com/Valloric/YouCompleteMe.git
cd YouCompleteMe && git submodule update --init --recursive
./install.sh --clang-completer
