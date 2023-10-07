import subprocess

def convertTimeToSeconds(timeStr):
    minutes, seconds = map(int, timeStr.split(':'))
    return minutes * 60 + seconds

def getSongPercentage():
    songLengthStr = subprocess.check_output(['scripts/getSongLength'], shell=True, text=True)
    songLength = convertTimeToSeconds(songLengthStr.strip())

    songProgress = subprocess.check_output(['playerctl -p spotify metadata --format "{{ duration(position) }}"'], shell=True, text=True)
    
    songProgressSeconds = convertTimeToSeconds(songProgress)
    
    songPercentage = (songProgressSeconds / songLength) * 100
    print(f"{songPercentage:.2f}")

getSongPercentage()
