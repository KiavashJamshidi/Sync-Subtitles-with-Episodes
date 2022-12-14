import os
import shutil

def createEpisodes(dirPath) -> list:
    episodes = []
    for episode in os.listdir(dirPath):
        if os.path.isfile(os.path.join(dirPath, episode)):
            formatEpisode = episode[-4:].lower()
            if formatEpisode == ".mkv" or formatEpisode == ".mp4":
                episodes.append(episode[:-4])
    
    episodes.sort()
    return episodes

                
def createSubtitles(dirPath) -> list:
    subtitles = []
    for subtitle in os.listdir(dirPath):
        if os.path.isfile(os.path.join(dirPath, subtitle)):
            formatSubtitle = subtitle[-4:].lower()
            if formatSubtitle == ".srt":
                subtitles.append(subtitle[:-4])
    
    subtitles.sort()
    return subtitles

                
def getInput():
    return input("Enter the path of the directory which episodes are in? "), \
        input("Enter the path of the directory which subtitles are in? ")
        
def rename(episodes, subtitles, dirEpisodesPath, dirSubtitlesPath) -> None:
    for (episode, subtitle) in zip(episodes, subtitles):
        print(subtitle + ".srt has changed to -> " + episode + ".srt")
        os.rename(os.path.join(dirSubtitlesPath, subtitle) + ".srt", os.path.join(dirEpisodesPath, episode) + ".srt")
        
def copyToEpisodesDirectory(subtitles, dirSubtitlesPath, dirEpisodesPath) -> None:
    try:
        for fname in subtitles:
            shutil.copy2(os.path.join(dirSubtitlesPath, fname) + ".srt", dirEpisodesPath)
    except:
        pass
    
                
if __name__ == "__main__":
    dirEpisodesPath, dirSubtitlesPath = getInput()
    episodes, subtitles = createEpisodes(dirEpisodesPath), createSubtitles(dirSubtitlesPath)

    rename(episodes, subtitles, dirEpisodesPath, dirSubtitlesPath)
    
    copyToEpisodesDirectory(subtitles, dirSubtitlesPath, dirEpisodesPath)
    
    print("Done :D")