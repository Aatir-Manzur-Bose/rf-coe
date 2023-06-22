This is an example python module that provides a simple interface class to the Vaunix LDA DLL for Windows
and it also has an example command line program. The command line program interprets its options in order
and can be used to control the parameters of one or more LDA devices.

The -h option will display a list of the command line options
The -r option displays the current settings. If no other options are selected it will display the settings for all devices and channels. The -r option, if
used should be the last option in the command line
The -i option selects one or more devices to apply commands to. Its argument can be a single number, or a set of numbers separated by the ":" character
The -c option selects one or more channels to apply commands to. Its argument can be a single number, or a set of numbers separated by the ":" character

For both the -i and -c options entering the character a as the argument selects all devices or channels.

Examples:

python -m ldausbcli_007 -i 21244 -c 1 -a 35.4 -r

The command above will select the LDA device with serial number 21244, select channel 1, and set the attenuation to 35.4 db. It will then report
the settings for the selected device and channel.

python -m ldausbcli_007 -i 21244 -c 1:2 -a 36.4 -i 27231 -c 4 -a 62.0 -r

The command above will select the LDA with serial number 21244, set channels 1 and 2 to 36.4 db attenuation, and then select the LDA with serial number
27231 and set its channel 4 to 62 db attenuation. Finally, the program will report the settings for the selected devices and channels.

8/21/22