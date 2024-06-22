# YouTube Scraping Tools

This repository contains collection of scraping tools for YouTube.

## Table of Contents

- Modules
    - [Playlist](#playlist)
        - [Playlist Output Format](#output-format)

## Playlist

This module retrieve information about playlist in json using the playlist link.

### Playlist Output Format

```
    {
        'title': ..., 
        'totalVideos': ..., 
        'channelName': ..., 
        'playlistUrl': ..., 
        'videos': [
            {
                'title': ..., 
                'duration': ..., 
                'id': ...
            }
            , 
            .
            .
            .
            ], 
        'duration': ...
    }
```
