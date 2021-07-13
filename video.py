 # load audio file
import moviepy.editor as mp
import math
output_path = "./slowed-reverb.mp4"
audio_clip = mp.AudioFileClip('./final.mp3')

    # load video
video_clip = mp.VideoFileClip('./vid.gif')

    # loop the gif for the duration of the audio
num_loops = math.ceil(audio_clip.duration / video_clip.duration)
video_clip2 = video_clip.loop(n=num_loops)

    # add the audio to the video
video_clip3 = video_clip2.set_audio(audio_clip)

    # save result
video_clip3.write_videofile(output_path, verbose=False, logger=None)