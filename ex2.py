import os
import sys

#with just 1 input we assume we want the same video .mp4 format
if len(sys.argv)==2:
    video_source = sys.argv[1]
    command = "ffmpeg -i {} -c:v copy {}.mp4".format(video_source, video_source[:-4])
    os.system(command)
else:
    #for >1 input arguments we assume 2nd is audio and 3rd is subtitles
    if len(sys.argv)==3:
        video_source = sys.argv[1]
        audio_source = sys.argv[2]
        command = "ffmpeg -i {} -i {} -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 {}_{}.mp4".format(video_source, audio_source, video_source[:-4],audio_source[:-4])
        os.system(command)
    elif len(sys.argv)==4:
        video_source = sys.argv[1]
        audio_source = sys.argv[2]
        subtitle_source = sys.argv[3]
        command = "ffmpeg -i {} -i {} -i {} -c:v copy -c:a aac -c:s mov_text -map 0:v:0 -map 1:a:0 -map 2:s:0 {}_{}_{}.mp4".format(video_source, audio_source, subtitle_source, video_source[:-4],audio_source[:-4],subtitle_source[:-4])
        os.system(command)
    else:
        print("Number of input arguments not supported")
