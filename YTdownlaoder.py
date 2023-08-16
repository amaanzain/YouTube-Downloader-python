
# The High-Quality YouTube Video Downloader project is a Python application that empowers users to effortlessly download YouTube videos
# with superior video and audio quality. This project combines the power of Python programming with a user-friendly GUI interface, allowing users 
# to interact with the downloader in a seamless manner.

import os
from pytube import YouTube
from breezypythongui import EasyFrame
import tkinter

class Tube(EasyFrame):   
    def __init__(self):
        EasyFrame.__init__(self,width=800,height=300,title="YouTube Downloader")
        self.addLabel(text="Enter the link of the youtube vedio that you want to download: ",row=0,column=0)
        self.link=self.addTextField(text="",row=0,column=0)
        self.addLabel(text="Title: ",row=1,column=0)
        self.title=self.addTextField(text="",row=1,column=0,width=70)
        self.addLabel(text="Views: ",row=2,column=0)
        self.view=self.addTextField(text="",row=2,column=0,width=20)
        self.addButton(text="Download",row=3,column=0,command=self.execu)
        self.addButton(text="open download location",row=3,column=1,command=self.down)

    def execu(self):
        yt=YouTube(self.link.getText())
        t=str(yt.title)
        self.title.setValue(t)
        v=str(yt.views)
        self.view.setValue(v)
        yd=yt.streams.get_highest_resolution()
        yd.download('D:\code\projects\python\YTdownloader\downloads')#the download path is given here
        self.messageBox(title="download",message="the vedio is downloaded successfully")
   
    def down(self):
        folder_path='D:\code\projects\python\YTdownloader\downloads'
        os.system(f'explorer "{folder_path}"')

def main():
    Tube().mainloop()

if __name__=="__main__":
    main()


