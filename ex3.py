import sys
import os
import subprocess as sp

source = sys.argv[1]

commandv = "ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of default=nokey=1:noprint_wrappers=1 {}".format(source)
commanda = "ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of default=nokey=1:noprint_wrappers=1 {}".format(source)

audio_codec = sp.getoutput(commanda)
video_codec = sp.getoutput(commandv)
broadcast_std = ""
if video_codec == "mpeg2" or "h264": #it accepts all of them

    if audio_codec == "mp3":
        broadcast_std = "DVB and DTMB"

    elif audio_codec == "aac":
        broadcast_std = "DVB, ISDB and DTMB"

    elif audio_codec == "ac-3":
        broadcast_std = "DVB, ATSC and DTMB"

    elif audio_codec == "dra" or "mp2":
        broadcast_std = "DTMB"

    else:
        print("ERROR, the container does not fit any broadcasting standard")

elif (video_codec == "avs" or "avs+") and (audio_codec == "dra" or "aac" or "ac-3" or "mp2" or "mp3"):
    broadcast_std = "DTMB"

else:
    print("ERROR, the container does not fit any broadcasting standard")

print("The container fits the following broadcasting standards: {}".format(broadcast_std))
