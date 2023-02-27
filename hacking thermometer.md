# The thermometer



This thermometer communicates with a wireless sensor that emmits information in the radiofrequency of 433Mhz, a very common frequency since it is unregulated in the EU.

![image](https://user-images.githubusercontent.com/70759474/221677212-d112b899-70cd-4187-b36a-8b2787b75274.png)

The sensor emmits a message with the temperature and humidity that it detects once every 50 seconds, when the thermometer detects a message it updates its display with the new temperature and humudity sent by the sensor.

# The message

I can use an RTL-SDR dongle (A Software Defined Radio) to listen to this message

![image](https://user-images.githubusercontent.com/70759474/221678924-e9f628f4-4d0a-4ab4-a757-f6cb98388871.png)

^SDR# software listening to 433MHz frequency (the high peak is the message being sent by the sensor)

After recording the message in RIFF format (.wav file), I can use the functions I created in this post to turn the message into a sequence of ints, each representing how long the antenna was on or off for during the message transmission. First of all, the message looks like this:

![image](https://user-images.githubusercontent.com/70759474/221680437-217e985e-9cdd-4b31-8d33-ffb4d0e7ea5f.png)

This is a portion of the message, as we can see, there are some short 'high' or '1' states which are immediatly followed by long 'low' or '0' states. After looking at the duration of each pulse, I found out that all the '1' states are 520 microseconds long, and the '0' pulses are either 1930 or 3850 microseconds long.

# Decoding

I made a guess that a 520 microseconds '1' pulse followed by a 1930 '0' pulse would represent a binary 0, and if it was followed by a 3850 microseconds '0' pulse, then it would represent a binary 1. Using this criteria I translated the missage to binary and it looked like this:

1001011011010000000011010101001011111

This 37 bit message is actually repeated 8 times during the transmission from the sensor, I guess for redundancy.

Since I have the duration of how long the antenna is on or off for during the transmission I can reproduce the message that I recorded from the sensor with an arduino and also a 433MHz transmitter that I bought (3€ in aliexpress). I did some tests transmitting different messages that I had recorded with differents temperatures and humidities and then I compared the messages in binary with the temperature and humidity that the message represented. And after some tests I found out which bits of the message represented both temperature and humidity

The first 12 bits I think are just there so that the thermometer doesn't confuse random noise with a transmission from the sensor, so the thermometer will just listen to transmissions that get the first 12 bits right, I think some of those bits also tell the channel number (the thermometer can listen to 3 different channels at the same time and the sensor can transmit to any one of those 3 channels, all tests I did were on channel 1, so I don't know which of those bits represent the channel number)

The temperature is stored in the 16 bits from bit number 12 to bit number 27 (starting from bit 0), and its stored multiplied by 10, for example, if the temperature that the sensor reads is 15.7 degrees celsius, then the binary number that will be sent in those 16 bits will be 0000000010011101, which is 157 in binary.

The humidity is stored normally, if the humidity is 43%, then the 8 bits, from bit 28 to bit 35 will be 00101011, which is 43 in binary.

The 36th bit is always 1.

Now knowing which bits represent humidity and which represent temperature, I can generate new messages from zero, making the thermometer display whatever values I want.

I 3d printed a case which holds an arduino nano, the 433MHz transmitter, a battery and a button, and programmed the arduino to transmit whatever message I want.

![image](https://user-images.githubusercontent.com/70759474/221691606-e0907eaf-0c49-463a-b863-fbe4681e86eb.png)

Given a temperature value and a humidity value it creates the 37 bit sequence, then it turns that sequence into how long the antenna should be on or off, and then the arduino controlls the antenna to be on or off during those periods, after hearing the transmission the thermometer then displays the values that the message wants. For example, setting the temperature to 42.0 degrees celsius and the humidity to 69% I can transmit the message with the arduino and the thermometer will display the numbers:

![image](https://user-images.githubusercontent.com/70759474/221692596-1fdd4aa2-e804-4901-8035-ddc1255724cd.png)
