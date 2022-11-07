import vlc

instance = vlc.Instance()
player = instance.media_player_new()
music = instance.media_new("assets/music/level1.mp3")
player.set_media(music)
player.audio_set_volume(70)


player.play()
# Move to starting time
player.set_time(int(41000))


while True:
    a=0