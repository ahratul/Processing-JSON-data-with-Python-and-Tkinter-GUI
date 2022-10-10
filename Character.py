import io, requests
from PIL import Image
import os.path


class Character:
    def __init__(self, name, gender, species,
                 origin, status,
                 image, number_of_episodes):
        self.name = name
        self.gender = gender
        self.species = species
        self.origin = origin
        self.status = status
        self.image_url = image
        self.number_of_episodes = number_of_episodes
        # names for downloaded images
        self.image_path ='./images/'+self.name.replace(' ', '')+'.png'
        self.download_image()

    def download_image(self):

        # Check if the file does not exists then download the image
        if not os.path.exists(self.image_path):
            response = requests.get(self.image_url)
            img_data = response.content
            image = Image.open(io.BytesIO(img_data))
            # resizing the image
            resized_image = image.resize((200, 200), Image.ANTIALIAS)
            resized_image.save(self.image_path)

            print(self.name + ' Image is Downloaded!')

    def get_image(self):
        return Image.open(self.image_path)