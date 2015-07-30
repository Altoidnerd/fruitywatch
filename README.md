## fruitywatch

Fruitywatch is a big fruity command line clock.

![Uh oh: img not found](http://full/path/to/img.jpg "Fruitywatch running on OSX Yosemite")

## linux installation

    sudo apt-get install figlet toilet
    cd && git clone https://github.com/altoidnerd/fruitywatch
    cd fruitywatch
    ./install_fruitywatch

Note: depending on your system settings, you might need to make the installer executable.  

    chmod +x install_fruitywatch

alternatively, you may just run this command if you have the figlet and toilet dependencies

    cd && echo 'watch -tcpn.5 '\''figlet -f big -W "$(date +%l:%M:%S)"|toilet -f term --gay'\' > fruitywatch && chmod +x fruitywatch; mv ./fruitywatch /usr/local/bin && fruitywatch

You will need sudo unless you change the destination directory.

# osx installation

You need the homebrew package manager.  If you need to install homebrew, 

    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

OSX does not come with watch out of the box, so

    brew install toilet
    brew install figlet
    brew install watch`

Then the procedure is the same.  You will need sudo unless you change the destination directory


    cd && git clone https://github.com/altoidnerd/fruitywatch
    cd fruitywatch
    ./install_fruitywatch
   

 
Note: depending on your system settings, you might need to make the installer executable. 

    chmod +x install_fruitywatch

Alternatively, run this as root:

    cd && echo 'watch -tcpn.5 '\''figlet -f big -W "$(date +%l:%M:%S)"|toilet -f term --gay'\' > fruitywatch && chmod +x fruitywatch; mv ./fruitywatch /usr/local/bin && fruitywatch


## shell alias  

Alternatively you may add this line to you bashrc:

    alias fruitywatch="watch -tcpn.5 'figlet -f big -W \"$(date +%l:%M:%S)\" |  toilet -f term --gay'"

This approach may be useful if you are not an administrator.
