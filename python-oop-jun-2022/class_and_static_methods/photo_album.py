from math import ceil


class PhotoAlbum:
    PICTURE_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for p in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / PhotoAlbum.PICTURE_PER_PAGE)
        return cls(pages)

    def add_photo(self, label):
        for index, page in enumerate(self.photos):
            if len(page) < PhotoAlbum.PICTURE_PER_PAGE:
                page.append(label)
                return f"{label} photo added successfully on page {index + 1} slot {len(page)}"
        return "No more free slots"

    def display(self):
        result = f"{11 * '-'}\n"
        for page in self.photos:
            result += f"{' '.join('[]' for s in page)}\n"
            result += f"{11 * '-'}\n"
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
