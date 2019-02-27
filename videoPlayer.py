import vlc
import time


def playerVLC():
    proces = subprocess.Popen(['obs'])
    proc
    from OBS import obsSceneTransition, obsSceneVLC
    playlist = '/app/playlist.pls'
    with open(playlist, 'r') as f:
        playlist=[i for line in f for i in line.split(',')]
        playlist = map(lambda s: s.strip(), playlist)
    instance = vlc.Instance()
    player = instance.media_player_new()
    playing = set([1,2,3,4])
    for i in playlist:
        obsSceneVLC()
        player.set_mrl(i)
        player.play()
        play=True
        while play == True:
            time.sleep(1)
            play_state = player.get_state()
            if play_state in playing:
                continue
            else:
                obsSceneTransition()
                play = False

playerVLC()


