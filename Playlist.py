import requests
from bs4 import BeautifulSoup
import json

class Playlist:

    def __init__(self, playlist_link):
        
        self.playlist_link = playlist_link

    def stats(self):

        stats = {}

        try:

            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36"}

            response = requests.get(url=self.playlist_link, headers=headers)

            soup = BeautifulSoup(response.text, 'html.parser')

            script_elements = soup.find_all('script')

            for e in script_elements:

                if e.text.startswith("var ytInitialData"):
                   
                    data_dict = json.loads(e.text[20:-1])

                    playlist = data_dict["contents"]["twoColumnWatchNextResults"]["playlist"]["playlist"]
                    
                    if "title" in playlist:
                        stats["title"] = playlist["title"]
                    else:
                        stats["title"] = ""

                    if "totalVideos" in playlist:
                        stats["totalVideos"] = playlist["totalVideos"]
                    else:
                        stats["totalVideos"] = ""

                    if "ownerName" in playlist:
                        stats["channelName"] = playlist["ownerName"]["simpleText"]
                    else:
                        stats["channelName"] = ""

                    if "playlistShareUrl" in playlist:
                        stats["playlistUrl"] = playlist["playlistShareUrl"]
                    else:
                        stats["playlistUrl"] = ""

                    if "contents" in playlist:

                        playlist_videos = playlist["contents"]

                        stats["videos"] = []

                        for video in playlist_videos:

                            video_data = {}

                            video = video["playlistPanelVideoRenderer"]

                            if "title" in video:
                                video_data["title"] = video["title"]["simpleText"]
                            else:
                                video_data["title"] = ""

                            if "lengthText" in video:
                                video_data["duration"] = video["lengthText"]["simpleText"]
                            else:
                                video_data["duration"] = ""

                            if "videoId" in video:
                                video_data["id"] = video["videoId"]
                            else:
                                video_data["id"] = ""

                            stats["videos"].append(video_data) # Update Stats with video

                    stats["duration"] = self.__calculatePlaylistDuration(stats["videos"])

                    break # Target Element Found; Break loop

        except Exception as e:
            print("Error in stats():", e)

        return stats
    
    def __calculatePlaylistDuration(self, videos_data):

        total_duration = "00:00:00"

        try:

            hours, minutes, seconds = 0,0,0

            for video in videos_data:

                video_duration = video["duration"]

                video_duration_parts = video_duration.split(":")
                
                if len(video_duration_parts) == 3:
                    hours += int(video_duration_parts[0])
                    minutes += int(video_duration_parts[1])
                    seconds += int(video_duration_parts[2])
                
                if len(video_duration_parts) == 2:
                    minutes += int(video_duration_parts[0])
                    seconds += int(video_duration_parts[1])
                
                if len(video_duration_parts) == 1:
                    seconds += int(video_duration_parts[0])

            hours += minutes // 60

            minutes = minutes % 60

            minutes += seconds // 60

            seconds = seconds % 60

            total_duration = f"{hours}:{minutes}:{seconds}"

        except Exception as e:
            print("Error in __calculatePlaylistDuration():", e)

        return total_duration

print(Playlist(playlist_link="https://www.youtube.com/watch?v=_t2GVaQasRY&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12").stats())