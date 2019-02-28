# Main file
import numpy as np
import random


def main():

    n_images, images = get_content("../dataset/d_pet_pictures.txt")
    list_of_images = parse_image(images)
    #print(list_of_images)
    list_of_images_horizontal = h_to_v2(list_of_images)
    #print(list_of_images_horizontal)

    test = calcul_order_permute(list_of_images_horizontal)
    #print(test)
    output_file(test)
    return 0


def h_to_v2(imgs):
    imVs = []
    imHs = []
    for img in imgs:
        img = img.copy()
        if img[1] == "V":
            imVs.append(img)
        else:
            imHs.append(img)

    idH = len(imHs)
    idV = len(imVs)

    k = idH
    L = []
    o = np.random.choice(idV, idV, False)

    for i, j in zip(o[:int(idV / 2)], o[int(idV / 2):]):
        img1 = imVs[i]
        img2 = imVs[j]
        img = merge_vertical(img1, img2)
        L.append(img)
    return imHs + L


def get_content(filename):
    with open(filename, mode='r') as file:
        content = file.read()
        sequences = content.split('\n')
    n_images = int(sequences[0])
    images = sequences[1:-1]
    assert n_images == len(images)
    return n_images, images


def parse_image(images):
    """
    outputs a list of lists
    below is an example
    [[0, 'H', ['cat', 'beach', 'sun']],
     [1, 'V', ['selfie', 'smile']],
     [2, 'V', ['garden', 'selfie']],
     [3, 'H', ['garden', 'cat']]]

    """
    parsed_images = []
    for i, image in enumerate(images):
        tokens = image.split(' ')
        _type_ = tokens[0]
        number = int(tokens[1])
        tags = tokens[2:]
        assert number == len(tags)
        parsed_images.append([i, _type_, tags])
    return parsed_images


def calcul_order_permute(list_of_images):
    """
    Calculate the order and then give back the order of slides.
    We suppose there are only horizontal images.

    :param list_of_images:  [[1, "H", ["cat", "field"], [(2,5) , "H", ["cat", "garden"]],
    [3, "H", ["chat", "garden"]
    :return:  list_of_slides = [1, (2,5), 3]
    """
    order_slides = []

    score = score_slide(list_of_images[0][2], list_of_images[1][2])
    print("score:" + str(score))


    for x in list_of_images:
        order_slides.append(x[0])  # Add the id.

    random.shuffle(order_slides)

    order_slides = list(set(order_slides))
    return order_slides


def parse_to_horizontal_2(list_of_images):
    """

    :param list_of_images:
    :return:
    """

    list_of_horizontal = []
    it = iter(list_of_images)
    for x in it:
        list_of_horizontal.append(merge_vertical(x, next(it)))

    return list_of_horizontal


def parse_to_horizontal(list_of_images):
    """
    Get the list of images.
    :param list_of_images: [[
    :return:
    """
    list_of_horizontal = []
    for x in list_of_images:
        if x[1] == 'H':  # If this is vertical
            list_of_horizontal.append(x)
    return list_of_horizontal


def merge_vertical(slide_h_1, slide_h_2):
    """Merge in the case of two verticals:
    [1, V, ["cat", "garden"]]
    [5, V, ["garden", "dog"]]

    Output:  [(1, 5), H, ["cat", "garden", "dog"]]
    """
    a = (slide_h_1[0], slide_h_2[0])  # Tuple of the id
    merge_tags = list(set(slide_h_1[2] + slide_h_2[2]))
    image = [a, "H", merge_tags]
    return image


def score_slide(slide_1, slide_2):
    """Given both tags of slides, return the score.
        slide_1 = ["garden", "cat"]
        slide_2 = ["selfie", "smile", "garden"]
    """
    number_common = len(list(set(slide_1).intersection(slide_2)))   # Number of common elements between both slides
    number_diff_left = len(list(set(slide_1) - set(slide_2)))
    number_diff_right = len(list(set(slide_2) - set(slide_1)))
    min_score = min(number_common, min(number_diff_right, number_diff_left))
    return min_score


def output_file(list_of_slides):
    """Output the file."""
    file = open("../dataset/output_d.txt", 'w')
    n = len(list_of_slides)
    file.write(str(n) + '\n')  # Write the number of slides
    for x in list_of_slides:
        if isinstance(x, int):  # If this is int (i.e horizontal)
            file.write(str(x) + '\n')
        else:  # If this is a tuple
            a, b = x
            file.write(str(a) + ' ' + str(b) + '\n')


if __name__ == '__main__':
    main()
