import os
import re
import time
import xbmc
import shutil
import organizer

def generate_final_path(tmp_file,tvshowsRootFolder,moviesRootFolder):
      finalPath = "";
      base_file = os.path.basename(tmp_file)
      groups = re.split("(.*)\s*[\.\-]\s*(([sS][0-9])?[0-9])([eE]|x|of)?([0-9][0-9])\..*",base_file)
      if len(groups) > 1:
            xbmc.log("Detected TV Show episode")
            tvshows = groups[1];
            if tvshows != "":
                  tvshows = tvshows.replace("."," ")
                  tvshows = tvshows.title()
            xbmc.log("TV Show: "+tvshows)
            season = groups[2]
            if season != "":
                  season = season.title()
                  if season.startswith('S'):
                        season = str(int(season[1:]))
            xbmc.log("Season: "+season)
            episode = groups[5]
            xbmc.log("Episode: "+episode)
            dirPath = tvshowsRootFolder + "/" + tvshows + "/Season " +season
            xbmc.log("Dir path: "+dirPath)
            finalPath = dirPath + "/" + base_file
      else:
            xbmc.log("Treated the File as a Movie")
            dirPath = moviesRootFolder + "/" + os.path.splitext(base_file)[0]
            xbmc.log("Dir path: "+dirPath)
            finalPath =  dirPath + "/" + base_file
      return finalPath


def process_file(tmp_file,tvshowsRootFolder,moviesRootFolder):
      try:
              finalPath = generate_final_path(tmp_file,tvshowsRootFolder,moviesRootFolder)
              try:
                    xbmc.log("Starting to move the file to: "+finalPath)
                    folder = os.path.dirname(finalPath)
                    if folder != "":
                        if not os.path.isdir(folder):
                            xbmc.log("Creating the folder if they don't exist.")
                            os.makedirs(folder);
                            xbmc.log("Created the folder if they don't exist.")
                        if not os.path.isfile(finalPath):
                              try:
                                  xbmc.log("Renaming the file")
                                  os.rename(tmp_file,finalPath)
                                  xbmc.log("Renamed the file")
                              except Exception as e:
                                    xbmc.log("Error renaming the file: "+str(e))
                                    xbmc.log("Trying to copy the file")
                                    shutil.copy(tmp_file,finalPath)
                                    xbmc.log("File copied")
                        else:
                            xbmc.log("Removing the original file")
                            os.remove(tmp_file)
                            xbmc.log("Removed the original file")
                    xbmc.log("Ending to move the file to: "+finalPath)
              except Exception as e:
                  xbmc.log("Error processing the file: "+str(e))
      except Exception as e:
            xbmc.log("Error processing the file: "+str(e))

def organize(downloadFolder,tvshowsRootFolder,moviesRootFolder,extensions):
   xbmc.log("Recovering the files recursively")
   files = []
   for root, directories, filenames in os.walk(downloadFolder):
            for filename in filenames:
                  files.append(os.path.join(root,filename))
   xbmc.log("Files recovered")
   xbmc.log("Filtering recovered files")
   filtered_files = []
   for tmp_file in files:
            xbmc.log(tmp_file);
            if tmp_file.lower().endswith(extensions):
                  filtered_files.append(tmp_file)

   xbmc.log("Filtered recovered files: "+str(len(filtered_files)))

   for tmp_file in filtered_files:
        process_file(tmp_file,tvshowsRootFolder,moviesRootFolder)
