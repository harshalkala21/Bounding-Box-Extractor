import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

class BoundingBoxExtractor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bounding Box Extractor")

        # Initialize variables
        self.image_path = ""
        self.x_start = None
        self.y_start = None
        self.x_end = None
        self.y_end = None

        # Create canvas for displaying image
        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.pack()

        # Create buttons for loading image and extracting bounding box
        load_button = tk.Button(self.root, text="Load Image", command=self.load_image)
        load_button.pack(side="left", padx=10, pady=10)
        bbox_button = tk.Button(self.root, text="Extract Bounding Box", command=self.extract_bbox)
        bbox_button.pack(side="left", padx=10, pady=10)

        self.root.mainloop()

    def load_image(self):
        # Open file dialog to select image
        self.image_path = filedialog.askopenfilename(filetypes=(("Image Files", "*.jpg;*.jpeg;*.png"),))

        # Display image on canvas
        image = Image.open(self.image_path)
        image = image.resize((500, 500), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo)

    def extract_bbox(self):
        # Bind canvas events to track mouse movements and button clicks
        self.canvas.bind("<Button-1>", self.on_click_start)
        self.canvas.bind("<ButtonRelease-1>", self.on_click_end)
        self.canvas.bind("<B1-Motion>", self.on_drag)

    def on_click_start(self, event):
        # Save starting coordinates of bounding box
        self.x_start = event.x
        self.y_start = event.y

    def on_click_end(self, event):
        # Save ending coordinates of bounding box
        self.x_end = event.x
        self.y_end = event.y

        # Draw bounding box on canvas
        self.canvas.create_rectangle(self.x_start, self.y_start, self.x_end, self.y_end, outline="red", width=3)

        # Unbind canvas events
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<B1-Motion>")

        # Print bounding box coordinates
        bbox = (self.x_start, self.y_start, self.x_end, self.y_end)
        print("Bounding Box Coordinates:", bbox)

    def on_drag(self, event):
        # Update ending coordinates of bounding box while dragging
        self.x_end = event.x
        self.y_end = event.y

        # Redraw bounding box on canvas
        self.canvas.delete("bbox")
        self.canvas.create_rectangle(self.x_start, self.y_start, self.x_end, self.y_end, outline="red", width=3, tags="bbox")

if __name__ == "__main__":
    BoundingBoxExtractor()
