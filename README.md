Open the file "hacking thermometer.md" to see a cool real world example of how this code can be used

# Description

This project turns .wav files to binary. Files must be RIFF (not RF64) and not very long, an error may occur when using some functions (numpy overflow or something like that), that is because the file is too long, shorten it and try it again.

The file "funcions_wave.py" has 3 functions: (file_name is the name of the wav file that has the binary sequence)

# show_graf(file_name)

When given a file name (.wav) it will show a graf with matplotlib of the value of every sample in the wav file.

# get_duration_vector(file_name, threshold)

This function returns a list with each value representing the duration of a state (0 or 1). The state division is given by the threshold (anything under the threshold is considered a 0 and anything over is a 1, the function show_graf(file_name) may help to determine this threshold). The wav file must have 2 channels.

EXAMPLE:

Using a file named test.wav

![image](https://user-images.githubusercontent.com/70759474/209836573-7a7a768c-5fc5-4f60-9712-3ed0a299904a.png)
^This image is the wav file that I want to interpret in binary


![image](https://user-images.githubusercontent.com/70759474/209836840-94de8ac1-de23-4f8c-b06e-04885fd8e48c.png)

^This is the graf given by the show_graf() function

In the graf I can see that the threshold I want to use is anywhere from 1000 to 2000 in order to filter out the noise.

Using get_duration("test.wav", 1500) i get the following list -> [871, 520, 1932, 520, 1931, 520, 3854, 521, 3853, 520]

![image](https://user-images.githubusercontent.com/70759474/209838594-0e5b2115-ab34-4ce3-85ce-bad01e3f88af.png)


The first value is how long the first "0" state lasts for, the next is how long the following "1" state last, then the next "0" state, and so on. The duration of the very last state is not saved. Each value is the number of microseconds that that state lasts for.


# get_values(file_name)

This function is not really necessary, it is used inside of the get_duration_vector() function. It gives an array with every element being the value of every sample.
