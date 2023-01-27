import tkinter
import customtkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

import aiohttp
import asyncio

from PIL.Image import Resampling
from bs4 import BeautifulSoup
import io
from rx import create
from rx.core import Observer

dict = {}
observerList = []


class ProgressBar(Observer):
    def on_next(self, v):
        v.step(1)


class App(customtkinter.CTk):

    def __init__(self, loop, interval=1 / 120):
        super().__init__()
        self.loop = loop
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.tasks = []
        self.tasks.append(loop.create_task(self.updater(interval)))

        user_input = tkinter.StringVar()
        self.entry_1 = customtkinter.CTkEntry(master=self, placeholder_text="Search for an image",
                                              textvariable=user_input)
        self.entry_1.grid(row=0, column=0, pady=10, padx=10)

        button = customtkinter.CTkButton(master=self, command=self.get_value,text="Buscar")
        button.grid(row=0, column=1, pady=10, padx=10)

        self.listbox = tkinter.Listbox(self, width=50, height=30)
        self.listbox.grid(row=1, column=0, pady=10, padx=10)
        self.listbox.bind("<<ListboxSelect>>", lambda x: self.set_image())

        frame = customtkinter.CTkFrame(master=self)
        frame.grid(row=1, column=1, pady=10, padx=10)

        self.progressbar = ttk.Progressbar(master=self, length=200, mode="determinate")
        self.progressbar.grid(row=3, column=0, pady=10, padx=10)

        self.images_label = customtkinter.CTkLabel(master=self, text="", font=("Arial", 15))
        self.images_label.grid(row=2, column=0, pady=10, padx=10)

        self.navigation_frame_label = customtkinter.CTkLabel(master=frame, compound="center",
                                                             text="", width=800, height=500)
        self.navigation_frame_label.grid(row=0, column=0, pady=10, padx=10)

    async def updater(self, interval):
        while True:
            self.update()
            await asyncio.sleep(interval)

    def close(self):
        for task in self.tasks:
            task.cancel()
        self.loop.stop()
        self.destroy()

    def get_value(self):
        e_text = self.entry_1.get()
        self.tasks.append(loop.create_task(self.extract_images(e_text)))

    def set_image(self):
        image = Image.open(io.BytesIO(dict[self.listbox.get(self.listbox.curselection())]))
        image = image.resize((800, 500), Resampling.LANCZOS)
        image = ImageTk.PhotoImage(image)
        self.navigation_frame_label.configure(image=image)
        self.navigation_frame_label.image = image

    async def download_images(self, image, observer):
        if image['src'].endswith('.png') or image['src'].endswith('.jpg'):
            async with aiohttp.ClientSession() as session:
                async with session.get(image['src']) as response:
                    imageBytes = await response.content.read()
                    imageName = image['alt']
                    dict.update({imageName: imageBytes})
                    self.listbox.insert(END, imageName)
                    observer.on_next(self.progressbar)

    async def extract_images(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                page = await response.content.read()
                soup = BeautifulSoup(page, 'html.parser')
                images = soup.findAll('img')

                taskList = []

                self.listbox.delete(0, END)
                self.images_label.configure(text=f"Se han encontrado {len(images)} imágenes")
                self.progressbar['value'] = 0
                self.progressbar['maximum'] = len(images)

                for image in images:
                    try:
                        observable = create(await self.download_images(image, ProgressBar()))
                        taskList.append(asyncio.create_task(observable.subscribe(ProgressBar())))
                    except:
                        pass

                asyncio.gather(*taskList)

loop = asyncio.get_event_loop()
app = App(loop)
loop.run_forever()
loop.close()