import mysql.connector as mariadb
import ftplib
import os
from apscheduler.schedulers.blocking import BlockingScheduler
from OBS import obsSceneVLC
import sys

#reload(sys)
#sys.setdefaultencoding('utf-8')

dirname = os.path.dirname(__file__)
my_path = os.path.abspath(os.path.dirname(__file__))

conn = mariadb.connect(host='192.168.150.251', user='videostream', password='mirko', database='songsDB')
cursor = conn.cursor(buffered=True)

morning = dirname + '/video/morning'
day = dirname + '/video/day'
commercials = dirname + '/video/commercials'

def deleteVideoFiles(folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            pass


def dayClock():
    cursor.execute("SELECT songName, attribute, fileLocation FROM songsDBFileLocation WHERE attribute = 'day' ORDER BY RAND() LIMIT 240")
    data = cursor.fetchall()
    ftp = ftplib.FTP('192.168.150.251', 'videostream', 'yammatFM102.5')
    ftp.cwd('/04-PUBLIC/LUKA/videoplayer/video/day')
    cwd = os.getcwd()
    print(cwd)
    currentPath = (os.path.relpath(cwd))
    os.chdir(day)
    for x in data:
        os.chdir(dirname)
        song = x[0]
        attribute = x[1]
        fileLocation = (x[2])
        print(song + ", '" + attribute + "'" + ', ' + fileLocation)
        with open('playlist.pls', 'a') as playlist:
            playlist.write(fileLocation + '\n')
            localFilename = os.path.join(currentPath + fileLocation)
            localFilename = (localFilename[1:])
            localFilename = (os.path.basename(fileLocation))
            os.chdir(day)
            try:
                with open(localFilename, "wb") as file: ftp.retrbinary("RETR " + localFilename, file.write)
            except ftplib.error_perm:
                pass

def morningClock():
    cursor.execute("SELECT songName, attribute, fileLocation FROM songsDBFileLocation WHERE attribute = 'morning' ORDER BY RAND() LIMIT 120")
    data = cursor.fetchall()
    ftp = ftplib.FTP('192.168.150.251', 'videostream', 'yammatFM102.5')
    ftp.cwd('/04-PUBLIC/LUKA/videoplayer/video/morning')
    cwd = os.getcwd()
    currentPath = (os.path.relpath(cwd))
    os.chdir(morning)
    for x in data:
        os.chdir(dirname)
        song = x[0]
        attribute = x[1]
        fileLocation = (x[2])
        print(song + ", '" + attribute + "'" + ', ' + fileLocation)
        with open('playlist.pls', 'a') as playlist:
            playlist.write(fileLocation + '\n')
            localFilename = os.path.join(currentPath + fileLocation)
            localFilename = (localFilename[1:])
            localFilename = (os.path.basename(fileLocation))
            os.chdir(morning)
            try:
                with open(localFilename, "wb") as file: ftp.retrbinary("RETR " + localFilename, file.write)
            except ftplib.error_perm:
                pass


def commercialsClock():
    cursor.execute("SELECT songName, attribute, fileLocation FROM songsDBFileLocation WHERE attribute = 'morning' ORDER BY RAND() LIMIT 120")
    data = cursor.fetchall()
    ftp = ftplib.FTP('192.168.150.251', 'videostream', 'yammatFM102.5')
    ftp.cwd('/04-PUBLIC/LUKA/videoplayer/video/morning')
    cwd = os.getcwd()
    currentPath = (os.path.relpath(cwd))
    os.chdir(commercials)
    for x in data:
        os.chdir(dirname)
        song = x[0]
        attribute = x[1]
        fileLocation = (x[2])
        print(song + ", '" + attribute + "'" + ', ' + fileLocation)
        with open('commercials.txt', 'a') as commercialsList:
            commercialsList.write(fileLocation + '\n')
            localFilename = os.path.join(currentPath + fileLocation)
            localFilename = (localFilename[1:])
            localFilename = (os.path.basename(fileLocation))
            os.chdir(morning)
            try:
                with open(localFilename, "wb") as file: ftp.retrbinary("RETR " + localFilename, file.write)
            except ftplib.error_perm:
                pass


def deletePlaylist():
    #os.chdir('/app')
    open('playlist.pls', 'w').close()


def playlist():
    deletePlaylist()
    deleteVideoFiles(morning)
    deleteVideoFiles(day)
    morningClock()
    for _ in range(50):
        dayClock()





def insertCommercials():
    with open("playlist.pls", "r+") as f2:

        i = 0
        for x in range(2):
            f2.readline()  # skip past early lines
        pos = f2.tell()  # remember insertion position
        f2_remainder = f2.read()  # cache the rest of f2
        f2.seek(pos)
        with open("commercials.txt", "r") as f1:
            f2.write(f1.read())
        f2.write(f2_remainder)

    # commercialsTxt = open('commercials.txt', 'r')
    # lines = commercialsTxt.read().split('\n')
    # print (lines)
    # with open('commercials.txt', 'r') as prev_file, open(dirname + 'playlist.pls', 'w') as new_file:
    #     prev_contents = prev_file.readlines()
    #     # Now prev_contents is a list of strings and you may add the new line to this list at any position
    #     prev_contents.insert(4, "\n This is a new line \n ")
    #     new_file.write("\n".join(prev_contents))


insertCommercials()
#commercialsClock()

# scheduler = BlockingScheduler()
# scheduler.add_job(obsSceneVLC, trigger='cron', hour='03', minute='00')
# scheduler.add_job(playlist, trigger='cron', hour='11', minute='25')
# scheduler.start()


