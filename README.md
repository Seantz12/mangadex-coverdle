# mangadex-coverdle
A wordle inspired game where you try to guess a manga from your mangadex list

Uses the MangaDexPy library

Some notes for myself:
Initialize with MangaDexPy.MangaDex()

get_user_list() returns list of user following manga (default limit 100)
this returns a list of Manga objects
Manga objects can be called with get_covers() to get a list of Cover objects
each Cover object has a url property that returns a link to the cover

https://stackoverflow.com/questions/32908639/open-pil-image-from-byte-file

this is for grabbing an image

# things that i should probably do 
* instead of blurring the image in the backend, unblurred image should be passed to front end and then all image modifications should occur there