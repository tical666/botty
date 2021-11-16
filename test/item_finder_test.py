import pytest
import cv2
from item_finder import ItemFinder


class ScreenMock():
    def __init__(self, img_path: str):
        self._img_path = ".\\assets\\test\\item_finder\\" + img_path

    def grab(self):
        return cv2.imread(self._img_path)

@pytest.fixture(scope="module")
def item_finder():
    item_finder = ItemFinder()
    return item_finder

@pytest.mark.parametrize("image,items", [("test1.png", 1), ("test2.png", 1)])
def test_search(item_finder: ItemFinder, image: str, items: int):
    screen = ScreenMock(image)
    img = screen.grab()
    item_list = item_finder.search(img)
    print(item_list)
    assert len(item_list) == items