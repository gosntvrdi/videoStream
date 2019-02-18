from apscheduler.schedulers.blocking import BlockingScheduler
from OBS import obsSceneVLC
from videoPlaylist import playlist
#from videoPlayer import playerVLC



scheduler = BlockingScheduler()
scheduler.add_job(obsSceneVLC, trigger='cron', hour='03', minute='00')
#scheduler.add_job(cecPowerOn, trigger='cron', hour='08', minute='00')
#scheduler.add_job(cecInputNuc, trigger='cron', hour='08', minute='01')
scheduler.add_job(playlist, trigger='cron', hour='03', minute='10')
#scheduler.add_job(playerVLC, trigger='cron', hour='03', minute='40')
scheduler.start()

