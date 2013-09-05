# Overview

## Description

This plug-in is used for navigating modules within browserified projects, specifically (exclusively?) those processed by [grunt-browserify-navigation](https://github.com/trabian/grunt-browserify-navigation). See [this screencast](http://www.screencast.com/t/0FKXptqa9) for a demo (within the screencast the Sublime Text command is being triggered via a keyboard shortcut).

# Installation

## via Source Control

Sublime stores packages in the following locations (replace '3' with '2' to use with Sublime Text 2):

    Nix: ~/.config/sublime-text-3/packages
    Mac: ~/Library/Application\ Support/Sublime\ Text\ 3/Packages
    Win: %APPDATA%\Sublime Text 3\Packages

### As a repository within the packages directory

Open a Terminal/Console and run the following commands, replacing `PACKAGE_PATH` with the path corresponding to your OS above.

    cd PACKAGE_PATH
    git clone https://github.com/trabian/BrowserifyNavigation.git

# Updating

If you are using Package Control, updating will be automatic and you don't have to worry about it.

If using Source Control:

    cd "PACKAGE_PATH/BrowserifyNavigation"
    git fetch origin
    git merge origin/master

# Shortcuts

You can access the commands either using the shortcuts.

    ctrl+r - Navigate to the module referenced within a `require` statement on the current line
    g+r - Same as above but when in `command` mode within Vintage Mode

Go to `Preferences > Package Settings > Browserify Navigation > Key Bindings - User` to change these shortcuts.

# Settings

Go to `Preferences > Package Settings > Browserify Navigation > Settings - User` to change settings.

```Javascript
{

  /*
    The namespace for the redis keys where the browserify references are stored. See https://github.com/trabian/grunt-browserify-navigation#options for details.
  */
  "namespace" : "browserify",

  /*
    Redis configuration options. The defaults below are the standard defaults for a Redis server running on the same development computer.
  */
  "redis_port": 6379,
  "redis_host": "localhost",
  "redis_db": 0
}
```
