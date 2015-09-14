import xbmcaddon
import xbmc
import organizer


if __name__ == '__main__':
	## This have to be recovered from the settings.xml	
	xbmc.log('Recovering the settings values for the execution')
	settings = xbmcaddon.Addon(id='script.downloadorganizer')
	
	allExtensions = ("avi","mp4","mkv")
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
	xbmc.executebuiltin('XBMC.Notification("DownloadOrganizer","Video files haven been organized",10)') 