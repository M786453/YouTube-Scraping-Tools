# YouTube Scraping Tools

This repository contains collection of scraping tools for YouTube.

## Table of Contents

- Modules
    - [Playlist](#playlist)

## Playlist

This module retrieve information about playlist in json format using the playlist link.

### Playlist Output Format

```
    {
        "title": ..., 
        "totalVideos": ..., 
        "channelName": ..., 
        "playlistUrl": ..., 
        "duration": ...,
        "videos": [
            {
                "title": ..., 
                "duration": ..., 
                "id": ...
            }
            , 
            .
            .
            .
            ], 
    }
```
