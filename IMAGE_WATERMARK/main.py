import tkinter as tk

from tkinter import filedialog, messagebox

from PIL import Image, ImageTk, ImageDraw, ImageFont



def upload_image():

    """Open a dialog to upload an image."""

    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")])

    if file_path:

        try:

            global img, img_display, img_path

            img_path = file_path

            img = Image.open(file_path)

            img.thumbnail((400, 400))  # Resize for display

            img_display = ImageTk.PhotoImage(img)

            canvas.create_image(200, 200, image=img_display)

        except Exception as e:

            messagebox.showerror("Error", f"Unable to open image: {e}")



def add_watermark():

    """Add a text watermark to the image."""

    global img

    if not img:

        messagebox.showwarning("Warning", "Please upload an image first.")

        return



    text = watermark_text.get()

    if not text:

        messagebox.showwarning("Warning", "Please enter a watermark text.")

        return



    watermark_img = img.copy()

    draw = ImageDraw.Draw(watermark_img)

    font = ImageFont.truetype("arial.ttf", 30)

    width, height = watermark_img.size



    text_width, text_height = draw.textsize(text, font=font)

    position = (width - text_width - 10, height - text_height - 10)  # Bottom-right corner



    draw.text(position, text, fill=(255, 255, 255, 128), font=font)



    # Display the watermarked image

    global img_display

    img_display = ImageTk.PhotoImage(watermark_img)

    canvas.create_image(200, 200, image=img_display)



    # Save the watermarked image temporarily

    global watermarked_img

    watermarked_img = watermark_img



def save_image():

    """Save the watermarked image."""

    if not watermarked_img:

        messagebox.showwarning("Warning", "No watermarked image to save.")

        return



    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")])

    if file_path:

        try:

            watermarked_img.save(file_path)

            messagebox.showinfo("Success", "Image saved successfully!")

        except Exception as e:

            messagebox.showerror("Error", f"Unable to save image: {e}")



# Initialize main window

root = tk.Tk()

root.title("Watermark App")

root.geometry("500x500")



# Canvas for displaying the image

canvas = tk.Canvas(root, width=400, height=400, bg="gray")

canvas.pack(pady=10)



# Input for watermark text

watermark_text = tk.StringVar()

entry = tk.Entry(root, textvariable=watermark_text, width=30)

entry.pack(pady=5)

entry.insert(0, "Enter watermark text")



# Buttons

btn_upload = tk.Button(root, text="Upload Image", command=upload_image)

btn_upload.pack(pady=5)



btn_add_watermark = tk.Button(root, text="Add Watermark", command=add_watermark)

btn_add_watermark.pack(pady=5)



btn_save = tk.Button(root, text="Save Image", command=save_image)

btn_save.pack(pady=5)



# Global variables

img = None

img_display = None

watermarked_img = None



root.mainloop()