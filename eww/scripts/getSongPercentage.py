import subprocess

def convert_time_to_seconds(time_str):
    minutes, seconds = map(int, time_str.split(':'))
    return minutes * 60 + seconds

def get_song_percentage():
    # Run the Bash script to get the song length
    song_length_str = subprocess.check_output(['scripts/getSongLength'], shell=True, text=True)
    song_length = convert_time_to_seconds(song_length_str.strip())

    song_progress = subprocess.check_output(['playerctl -p spotify metadata --format "{{ duration(position) }}"'], shell=True, text=True)
    
    song_progress_seconds = convert_time_to_seconds(song_progress)
    
    song_percentage = (song_progress_seconds / song_length) * 100
    print(f"{song_percentage:.2f}")

get_song_percentage()
