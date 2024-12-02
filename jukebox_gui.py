from tkinter import Tk, Label, Listbox
from PIL import Image, ImageTk

def display_image(track_number):
    """Load and display the corresponding track image."""
    # Load corresponding image based on track number
    image_path = f'images/track_{track_number}.jpg'  # Assuming images are in the 'images' folder
    
    try:
        img = Image.open(image_path)
        img = img.resize((100, 100))  # Resize the image to fit
        img_tk = ImageTk.PhotoImage(img)

        # Create a label to display the image
        label.config(image=img_tk)  # Update the label with the new image
        label.image = img_tk  # Keep a reference to avoid garbage collection
        label.pack()
    except FileNotFoundError:
        print(f"Image for track {track_number} not found.")

# Initialize main window
root = Tk()

# List of tracks to display
tracks = [1, 2, 3, 4, 5]

# Listbox to display track numbers
track_listbox = Listbox(root)
for track in tracks:
    track_listbox.insert('end', f"Track {track}")
track_listbox.pack(pady=10)

# Create a label to display the image
label = Label(root)
label.pack(pady=10)

# Function to update the displayed image when a track is selected
def on_track_select(event):
    selected_track = track_listbox.get(track_listbox.curselection())  # Get the selected track
    track_number = int(selected_track.split()[-1])  # Extract track number
    display_image(track_number)

# Bind the listbox selection event to display the image
track_listbox.bind("<<ListboxSelect>>", on_track_select)

# Run the Tkinter event loop
root.mainloop()
