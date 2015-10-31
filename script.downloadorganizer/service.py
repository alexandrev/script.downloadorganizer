import os
import re
import time
import xbmcaddon
import xbmc
import organizer

if __name__ == '__main__':
    monitor = xbmc.Monitor()
 
    while True:
        ## This have to be recovered from the settings.xml
        allExtensions = ("avi","mp4","mkv")
        xbmc.log('Recovering the settings values for the execution')
        settings = xbmcaddon.Addon(id='script.downloadorganizer')     
        
    	extensions = ()
    	for ext in allExtensions:
		extValue = settings.getSetting(ext)
		if(extValue):
			extensions = extensions + (ext,)
	    
        xbmc.log("Extensions available: "+str(extensions))           
        downloadFolder = settings.getSetting("downloadFolder")
        xbmc.log("Download Folder "+downloadFolder)
        moviesRootFolder = settings.getSetting("movieRootFolder")
        xbmc.log("Movies Root Folder "+moviesRootFolder)
        tvshowsRootFolder = settings.getSetting("tvshowRootFolder")
        xbmc.log("TV Shows Folder"+tvshowsRootFolder)                
        organizer.organize(downloadFolder,tvshowsRootFolder,moviesRootFolder,extensions)
        xbmc.executebuiltin('UpdateLibrary("video")') 
        xbmc.executebuiltin('XBMC.Notification("DownloadOrganizer","Video files haven been organized",10)')              
        # Sleep/wait for abort for 3600 seconds
        if monitor.waitForAbort(3600):
            # Abort was requested while waiting. We should exit
            break            
