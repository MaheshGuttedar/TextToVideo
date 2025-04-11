from moviepy.editor import *
from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont

# Step 1: Create an image with text
img = Image.new('RGB', (1280, 720), color='black')
draw = ImageDraw.Draw(img)


# Optional: Use your own font and size  
#font = ImageFont.truetype("arial.ttf", 60)
# Assuming you have 'arial.ttf' in the same directory as your notebook
font = ImageFont.load_default()  
draw.text((100, 300), "Welcome to My Python Video changed !", font=font, fill='white')
img.save("frame1.png")

# Step 2: Create voice narration
tts = gTTS("Welcome to my Python-generated video.", lang='en')
tts.save("narration.mp3")

# Step 3: Load image as clip
image_clip = ImageClip("frame1.png").set_duration(5)

# Step 4: Load audio (voice + music)
voice = AudioFileClip("narration.mp3")

# Optional: add background music
# music = AudioFileClip("background_music.mp3").volumex(0.2)
# final_audio = CompositeAudioClip([voice, music])

# Use just the voice
image_clip = image_clip.set_audio(voice)

# Step 5: Export video
image_clip.write_videofile("output_video.mp4", fps=24)
