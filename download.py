from pytube import YouTube
try:
    url = "https://www.youtube.com/watch?v=MbTM6xnl5Qc"
    streams = YouTube(url).streams.get_lowest_resolution()
    streams.download(r"D:\snap Tube")
    print("Done....... ")
except:
    print("Connection Error ....!")

