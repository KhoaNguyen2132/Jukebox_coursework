import tkinter as tk
import track_library as lib


class UpdateTracks:
    def __init__(self, window):
        window.geometry("750x200")
        window.title("Update Tracks")

        # Enter Track Number and Rating
        tk.Label(window, text="Enter Track Number").grid(row=0, column=0, padx=10, pady=10)
        self.track_num_txt = tk.Entry(window, width=5)
        self.track_num_txt.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(window, text="Enter New Rating (1-5)").grid(row=0, column=2, padx=10, pady=10)
        self.rating_txt = tk.Entry(window, width=5)
        self.rating_txt.grid(row=0, column=3, padx=10, pady=10)

        update_track_btn = tk.Button(window, text="Update Track", command=self.update_track_clicked)
        update_track_btn.grid(row=0, column=4, padx=10, pady=10)

        # Status label
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=1, column=0, columnspan=5, pady=10)

    def update_track_clicked(self):
        track_num = self.track_num_txt.get()
        try:
            rating = int(self.rating_txt.get())
            if rating < 1 or rating > 5:
                self.status_lbl.configure(text="Rating must be between 1 and 5.")
                return
        except ValueError:
            self.status_lbl.configure(text="Invalid rating. Please enter a number between 1 and 5.")
            return

        track = lib.get_track(track_num)
        if track:
            lib.set_rating(track_num, rating)
            self.status_lbl.configure(
                text=f"Track '{track.name}' updated! New rating: {rating}, Play count: {track.play_count}."
            )
        else:
            self.status_lbl.configure(text="Invalid track number. Please try again.")
def update_track_clicked(self):
    track_num = self.track_num_txt.get()
    if not track_num.isdigit() or len(track_num) != 2:  # Check valid track number
        self.status_lbl.configure(text="Invalid track number. Please enter a valid two-digit number (e.g., '01').")
        return

    try:
        rating = int(self.rating_txt.get())
        if rating < 1 or rating > 5:
            self.status_lbl.configure(text="Rating must be between 1 and 5.")
            return
    except ValueError:
        self.status_lbl.configure(text="Invalid rating. Please enter a numeric value between 1 and 5.")
        return

    track = lib.get_track_details(track_num)
    if track:
        lib.set_rating(track_num, rating)
        self.status_lbl.configure(
            text=f"Track '{track.name}' updated! New rating: {rating}, Play count: {track.play_count}."
        )
    else:
        self.status_lbl.configure(text="Track not found. Please try again.")
if __name__ == "__main__":
    window = tk.Tk()
    UpdateTracks(window)
    window.mainloop()