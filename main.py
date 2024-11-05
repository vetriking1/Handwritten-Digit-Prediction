import tkinter as tk
from PIL import Image, ImageDraw
from DigitClassifier import predict_image

class DrawApp:
    def __init__(self, root):
        
        # Initialize the root window
        self.root = root
        self.root.title("Draw on Canvas")

        # Create a white background image
        self.image = Image.new("RGB", (400, 400), "black")
        self.draw = ImageDraw.Draw(self.image)
        
        # Create a canvas to draw on
        self.canvas = tk.Canvas(root, width=400, height=400, bg="black")
        self.canvas.pack()

        # Bind mouse events to canvas
        self.canvas.bind("<B1-Motion>", self.paint) # left mouse button
        self.canvas.bind("<ButtonRelease-1>", self.repoint)

        # Initialize start position for drawing
        self.last_x, self.last_y = None, None

        self.stringVar = tk.StringVar()
        self.stringVar.set("Result: - ")
        
        label = tk.Label(root, textvariable=self.stringVar)
        label.pack(pady=20)

        # Button to save and reset the drawing
        save_button = tk.Button(root, text="Predict", command=self.save_and_predict_image)
        save_button.pack(pady=10)
        reset_button = tk.Button(root, text="Reset", command=self.reset_image)
        reset_button.pack(pady=10)

    def paint(self, event):
        # Draw a line from the last point to the current point
        if self.last_x and self.last_y:
            self.canvas.create_line((self.last_x, self.last_y, event.x, event.y), fill='white', width=10, capstyle=tk.ROUND, smooth=tk.TRUE, splinesteps=36)
            self.draw.line((self.last_x, self.last_y, event.x, event.y), fill='white', width=10)

        # Update the last point to the current point
        self.last_x, self.last_y = event.x, event.y
    
    # reset last x,y when stop drawing
    def repoint(self, event):
        
        self.last_x, self.last_y = None, None

    def save_and_predict_image(self):
        # Save the image
        self.image.save("drawing.png")
        result = predict_image("drawing.png")
        self.stringVar.set(f"Result: {str(result)}")
        
    def reset_image(self):

        # Clear the canvas
        self.canvas.delete("all")
        self.image = Image.new("RGB", (400, 400), "black")
        self.draw = ImageDraw.Draw(self.image)
        self.stringVar.set("Result: - ")
        self.last_x = None
        self.last_y = None

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x600")
    app = DrawApp(root)
    root.mainloop()
