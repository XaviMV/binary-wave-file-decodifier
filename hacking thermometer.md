# The thermometer

This thermometers communicates with a wireless sensors that emmits information in a radiofrequency of 433Mhz, a very common frequency since it is unregulated in the EU. The sensor emmits a message with the temperature and humidity that it detects once every 50 seconds, when the thermometer detects a message it updates its display with the new temperature and humudity sent by the sensor.

# The message

I can use an RTL-SDR dongle (A Software Defined Radio) to listen to this message

^ SDR# software listeniing to 433MHz frequency (the high peak is the message being sent by the sensor)

After recording the message in RIFF format (.wav file), I can use the functions I created in this post to turn the message into a sequence of ints, each representing how long the antenna was on or off for during the message transmission.

This is a portion of the message, most of it looks like this, a short '1' pulse followed by an either short or long '0' pulse. The '1' pulse is about 520 microseconds and the '0' pulse can either be 870 microseconds or 1930 microseconds.

# Decoding

I guess that a 520 microseconds '1' pulse followed by an 870 '0' pulse is a binary 0, and if it is followed by a 1930 microseconds '0' pulse, then it is a binary 0. Using this criteria the message I recorded looks like this: [MOSTRAR CADENA DE BITS], it is basically a 16 bit message repeated 8 times.

Since I now have the duration of how long the antenna is on or off for I can reproduce the message that I recorded with an arduino and also a 433MHz transmitter that I bough (3€ in aliexpress). I did some tests transmitting different messages that I recorded with differents temperatures and humidities, then I compared the message in binary to what the humidity and temerature the thermometer displayed after hearing the message, and I found out the following: [ENSENYAR QUE VOL DIR CADA BIT DE LA SEQUENCIA EN BINARI]

Now knowing which bits represented humidity and which represented temperature, I can now generate new messages from zero, making the thermometer display whatever values I want.

I 3d printed a case which holds an arduino nano, the 433MHz transmitter, a battery and a button, and programmed the arduino to transmit whatever message I want. Given a temperature value and a humidity value it creates the 16 bit sequence, then it turns that sequence into how long the antenna should be on or off, and then the arduino controlls the antenna to be on or off during those periods, after hearing the transmission the thermometer then displays the values that the message wants.
