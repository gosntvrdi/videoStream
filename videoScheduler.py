from apscheduler.schedulers.blocking import BlockingScheduler
from videoPlayerPlaylist import playlist
from player import playerVLC
from OBS import obsSceneVLC




scheduler = BlockingScheduler()
scheduler.add_job(obsSceneVLC, trigger='cron', hour='03', minute='00')
#scheduler.add_job(cecPowerOn, trigger='cron', hour='08', minute='00')
#scheduler.add_job(cecInputNuc, trigger='cron', hour='08', minute='01')
scheduler.add_job(playerVLC, trigger='interval', minutes = 30)
scheduler.start()
