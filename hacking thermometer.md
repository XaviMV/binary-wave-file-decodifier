# The thermometer

This thermometers communicates with a wireless sensors that emmits information in a radiofrequency of 433Mhz, a very common frequency since it is unregulated in the EU.

^ This sensor sends a message every 50 seconds, and the thermomenter listens to it and displays both the temperature and the humidity that the message said.

I can use an RTL-SDR dongle with an antenna and a radio software (SDR#) to listen to this message

^ SDR# software listeniing to 433MHz frequency (the peak is so high because the wireless sensor is sending the message near the antenna)

After recording the message in RIFF format, I can use the functions in this post to turn the message into binary.

^ Message sent by the sensor sent shown in audacity

After decoding the message, making it show how long each state lasts for (in microseconds) I get the following list: (POSAR LA LLISTA DE VALORS)

There are basically 3 values of how long each state lasts for: 800 or 1600 followed by 3200. I guessed that the 800s followed by 3200 would be binary 0s and 1600 followed by 3200 woudl be considered binary 1s. Following that criteria I turned the duration of each state into binary, and got the following:

It turned out to be a sequence of 16 bits repeated 8 times. Since I have the duration of how long the antenna is on or off I can reproduce the message that I recorded with an arduino and a 433MHz transmitter that I bough (3€ in aliexpress). I did some tests repeating messages that I recorded with differents temperatures and humidities, then I compared the binary meaning of each and I found out the following: [ENSENYAR QUE VOL DIR CADA BIT DE LA SEQUENCIA EN BINARI]

Now knowing which bits represented humidity and which represented temperature, I could now generate new messages from zero, making the thermometer display whatever values I wanted.

I 3d printed a case which held an arduino nano, the 433MHz transmitter, a battery and a button, and coded it to transmit whichever message I wanted, given a temperature value and a humidity value it would create the 16 bit sequence, and then turn that into the duration of each binary state, which then sent to the transmitter to emmit, the thermometer then heard that message and displayed whatever values the message had.

