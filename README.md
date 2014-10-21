# Overview

## Description

This plug-in is used for navigating modules within browserified projects. It's adapted from the package by https://github.com/trabianmatt but doesn't need redis.

# Installation

## via Source Control

Sublime stores packages in the following locations (replace '3' with '2' to use with Sublime Text 2):

    Nix: ~/.config/sublime-text-3/packages
    Mac: ~/Library/Application\ Support/Sublime\ Text\ 3/Packages
    Win: %APPDATA%\Sublime Text 3\Packages

### As a repository within the packages directory

Open a Terminal/Console and run the following commands, replacing `PACKAGE_PATH` with the path corresponding to your OS above.

    cd PACKAGE_PATH
    git clone https://github.com/davedx/sublime-text-browserify.git

# Updating

If you are using Package Control, updating will be automatic and you don't have to worry about it.

If using Source Control:

    cd "PACKAGE_PATH/BrowserifyNavigation"
    git fetch origin
    git merge origin/master

# Shortcuts

You can access the commands either using the shortcuts.

    ctrl+r - Navigate to the module referenced within a `require` statement on the current line
    alt-leftclick - Same as above. Note you need to click once to select the thing first..buggy.

Go to `Preferences > Package Settings > Browserify Navigation > Key Bindings - User` to change these shortcuts.
