import io
from PIL import Image, ImageDraw, ImageFont
def draw(text="undefined"):
    cover = Image.open("./public/cover.png").convert("RGBA")
    draw = ImageDraw.Draw(cover)
    font = ImageFont.truetype("./public/SmileySans-Oblique.ttf", 65)
    position = (250, 590)
    draw.text(position, text, font=font)
    output_io = io.BytesIO()
    cover.save(output_io, "WEBP")
    output_io.seek(0)
    return output_io
