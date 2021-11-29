# Keypad_Configurator


## Working

This program can connect to a usb device through serial communication. Once the communication is established using the config file you can pass serial bytes from 'A' to 'P' and the actions programmed in the config file are executed as keyboard presses or mouse movements.

## Purpose

The whole reason behind this project is that I made a keypad using a ESP8266 dev board only to realize that the Arduino keyboard library doesn't work with the ESP8266. That is why I made this program so I could still use my keypad as a custom keyboard.

In the process however I made the whole thing customizable and made it so that it can have a wide range of applications and implementations.

## Config file

This is the place where you actually store the key strokes that you want to be executed when you press a key on the keypad.

Currently I am just using a 'csv' file as my config file as it is simply easy to open and use in python and also has a user friendly UI outside of python.

I have attached a sample Config file with all the different options included. You can chain the commands which ever way you wish and make the program do what ever you want.



All and all this for a fun weekend proj and just wanted to share this in case someone was looking for something similar.

Cheers!