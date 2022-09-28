from pytube import YouTube
try:
    # Entering the link of the video
    url = "https://www.youtube.com/watch?v=MbTM6xnl5Qc"
    streams = YouTube(url).streams.get_lowest_resolution()
    print("wait some seconds ..")
    # where you want to download.....! 
    streams.download(r"D:\snap Tube")
    print("Done....... ")
except:
    print("Connection Error ....!")

