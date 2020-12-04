# Lab3-scav
Lab 3. SCAV subject. UPF.

# Quim Marcé - 205523

Previous steps)

Download the BigBuckBunny(refered to as BBB from now on) video in .mp4 from this link: https://peach.blender.org/download/ 

Remember to cut the first minute of the video using the following command:

ffmpeg -i BBB.mp4 -s 00:00:00 -t 00:01:00 BBBcut.mp4

Exercise 1)

Corresponding files: the ones in folder "Screenshots"

This statement was pretty simple and many of the asked things have been seen in previous labs and seminars. Therefore, I just implemented it directly from terminal using ffmpeg commands. All of these commands can be found in the screenshots folder. The first one corresponds to extracting its audio in mono, the second one consists on extracting its audio in a lower bitrate (64kB to be more specific), the third one corresponds to putting subtitles in the video and the last one creates a container with all these files created.

In order to put subtitles in the video I used the information found in the following link.

Source 1: https://stackoverflow.com/questions/8672809/use-ffmpeg-to-add-text-subtitles


Exercise 2) Automatization of containers

Corresponding files: ex2.py

This file is aimed to be run from terminal with the following command: python3 ex2.py x y z

Where x is the video file, y the audio file and z the subtitles file. The script basically maps the different desired inputs into an output. If there is no audio nor subtitles, it just copies the input x. If it has an added audio it uses this one and if it also has a subtitles it maps it all into the output.


Exercise 3) Broadcasting analyzer

Corresponding files: ex3.py

This file is aimed to be run from terminal with the following command: python3 ex3.py x

Where x is the file we want to analyze. The script first uses the tool ffmprobe to get the different audio and video codecs as we saw in the last lab/seminar together with subprocess, a python packet useful to run the terminal from a python file. Finally, it just compares these codecs with the ones that fit the different broadcasting standards and gives an answer according to this.


Exercise 4) Creating containers and launching them against ex3

Corresponding files: ex4.py

This file is aimed to be run from terminal in the same way we did in exercise 2.

We first generate the container launching exercise 2 according to the number of inputs we have and later we compare launch the resulting file against exercise 3.


Exercise 5) Integrate everything into a class

This script just contains the definition of the class, implementing the codes from both exercises 2 and 3. The initialization method already includes the automatized generation of the container seen in exercise 2 with a novelty, in this case we can have a subtitle input without having an audio per se. The other method defined is analyzing its compatibility with the different broadcasting standards, most of the code is reused from exercise 3 obviously, except for the part where we check what inputs do we have, in order to pick the correct file that was generated previously.






