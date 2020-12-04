import subprocess as sp

class container:
    def __init__(self, video_source, audio_source=None, subtitle_source=None):
        self.video = video_source
        if audio_source==None and subtitle_source == None:
            command = "ffmpeg -i {} -c:v copy {}.mp4".format(video_source, video_source[:-4])
        elif audio_source != None and subtitle_source == None:
            self.audio = audio_source
            command = "ffmpeg -i {} -i {} -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 {}_{}.mp4".format(video_source, audio_source, video_source[:-4], audio_source[:-4])
        elif audio_source == None and subtitle_source != None:
            self.subtitle = subtitle_source
            command = "ffmpeg -i {} -i {} -c:v copy -c:a aac -c:s mov_text -map 0:v:0 -map 1:s:0 {}_{}.mp4".format(video_source, subtitle_source, video_source[:-4],subtitle_source[:-4])
        elif audio_source != None and subtitle_source != None:
            self.audio = audio_source
            self.subtitle = subtitle_source
            command = "ffmpeg -i {} -i {} -i {} -c:v copy -c:a aac -c:s mov_text -map 0:v:0 -map 1:a:0 -map 2:s:0 {}_{}_{}.mp4".format(video_source, audio_source, subtitle_source, video_source[:-4],audio_source[:-4],subtitle_source[:-4])
        sp.run(command, shell = True)

    def broadcast(self):
        source = ""
        if hasattr(self,'audio')==False and hasattr(self, 'subtitle') == False:
            source = self.video
        elif hasattr(self, 'audio') == True and hasattr(self, 'subtitle') == False:
            source = self.video[:-4]+"_"+self.audio[:-4]+".mp4"
        elif hasattr(self, 'audio') == False and hasattr(self, 'subtitle') == True:
            source = self.video[:-4]+"_"+self.subtitle[:-4]+".mp4"
        elif hasattr(self,'audio')==True and hasattr(self, 'subtitle') == True:
            source = self.video[:-4]+"_"+self.audio[:-4]+"_"+self.subtitle[:-4]+".mp4"


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
