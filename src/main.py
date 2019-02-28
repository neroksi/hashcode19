# Main file


def main():
    file = open("../dataset/a_example.txt")

    content = file.read().splitlines()
    lines = [line.rstrip('\n') for line in file]

    slide_1 = ["garden", "cat"]
    slide_2 = ["selfie", "smile", "garden"]
    s = score_slide(slide_1, slide_2)
    print(s)
    
    # Output the file according to Google format
    # list_of_slides = [0, (1, 2), 5]
    # output_file(list_of_slides)


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

    return order_slides


def merge_vertical(slide_h_1, slide_h_2):
    """Merge in the case of two verticals:
    [1, "V", ["cat", "garden"]]
    [5, "V", ["garden", "dog"]]

    Output:  [(1, 5), "H", ["cat", "garden", "dog"]]
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
    """Output the file.
    Format ex:  list_of_slides = [0, (1, 2), 5]
    """
    file = open("../dataset/output.txt", 'w')
    n = len(list_of_slides)
    file.write(str(n) + '\n')  # Write the number of slides
    for x in list_of_slides:
        if isinstance(x, int):  # If this is int (i.e horizontal)
            file.write(str(x) + '\n')
        else:  # If this is a tuple
            a, b = x
            file.write(str(a) + ' ' + str(b) + '\n')
            
def solver(nH, nV):
    return [imVs[0], imHs[0] + imHs[nH -1], imHs[nV-1] ]

if __name__ == '__main__':
    main()
