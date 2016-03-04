#!/usr/bin/env python

import sys, requests, urllib, json, threading, time, string, re, os
import mutagen
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error

MAX_THREAD_COUNT = 5

class SoundcloudDownloader:
    def __init__(self,filename):
        self.urls = urls

    def parse_filename(self, filename):
        return ''.join(c for c in filename if c in '-_&.() %s%s' % (string.ascii_letters, string.digits))

    def grab_track_info(self, soundcloud_url):
        json = requests.get('http://soundcloud.com/widget.json?url=%s' % soundcloud_url).json()

        return {
            'soundcloud_url': soundcloud_url,
            'stream_url': json['stream_url'],
            'image_url': (json['artwork_url'] if json['artwork_url'] else json['user']['avatar_url']).replace('-large', '-t500x500'),
            'title': json['title'],
            'user': json['user']['username']
        }

    def do_download(self, track_info):
        print 'Downloading %s' % track_info['soundcloud_url']

        mp3_url = requests.get(track_info['stream_url'], allow_redirects=False).headers.get('location')
        mime = requests.get(track_info['image_url']).headers['content-type']

        filename = '%s.mp3' % self.parse_filename(track_info['title'])[0]
        urllib.urlretrieve(mp3_url, filename)
        urllib.urlretrieve(track_info['image_url'], "%s.tmp" % filename)

        try:
            artist = re.findall(r'(.+)\s\-\s.+', track_info['title'])[0]
        except:
            artist = track_info['user']
        audio = mutagen.File(filename, easy=True)
        audio.add_tags()
        audio['title'] = track_info['title']
        audio['artist'] = artist
        audio.save(filename, v1=2)

        audio = MP3(filename)
        audio.tags.add(APIC(3,mime,3,'Cover', open('%s.tmp' % filename, 'rb').read()))
        audio.save()

        os.remove('%s.tmp' % filename)

    def run(self):
        while True:
            if self.urls:
                url = self.urls.pop()
                self.do_download(self.grab_track_info(url))
            else:
                exit()

class thread(threading.Thread):
    def __init__(self,sc_instance):
        threading.Thread.__init__(self)
        self.sc_instance = sc_instance

    def run(self):
        self.sc_instance.run()

if len(sys.argv) < 2:
    sys.exit('No arguments provided.')

urls = [url for url in sys.argv[1:]]
sc = SoundcloudDownloader(urls)
threads = [thread(sc) for x in (range(len(urls)) if len(urls) <= MAX_THREAD_COUNT else range(MAX_THREAD_COUNT))]

for thread in threads:
    thread.start()

