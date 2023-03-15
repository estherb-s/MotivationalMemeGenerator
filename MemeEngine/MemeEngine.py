import random
from PIL import Image, ImageDraw, ImageFont
from QuoteEngine import QuoteModel


class MemeEngine():
    """The MemeEngine class takes an output directory, saves a meme to this
    location and returns the output path."""

    def __init__(self, out_dir):
        self.out_dir = out_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Make a meme

        Arguments:
            img_path {str} -- file location for the image.
            text {str} -- text used as the meme's quote body.
            author {str} -- quote author for the meme.
            width {int} -- The pixel width for the image, default=500.
        Returns:
            str -- the file path to the output image.
        """
        try:
            image = Image.open(img_path)
        except Exception as e:
            print(f'Exception: {e}')
        else:
            if width is not None:
                height = float(image.size[1])
                aspect_ratio = width / float(image.size[0])
                new_height = int(aspect_ratio * height)
                image = image.resize((width, new_height), Image.NEAREST)
            if text and author:
                height = image.size[1] // 2
                width = image.size[0] // 2
                rand_height = float(random.sample(range(0, height), 1)[0])
                rand_width = float(random.sample(range(0, width), 1)[0])
                random_text_location = (rand_width, rand_height)
                draw = ImageDraw.Draw(image)
                font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf',
                                          size=20
                                          )
                quote_model = repr(QuoteModel(text, author))
                draw.text(random_text_location,
                          quote_model,
                          font=font,
                          fill='white'
                          )
            out_path = f'{self.out_dir}/{random.randint(0, 100000000)}.jpg'
            image.save(out_path)
            return out_path
