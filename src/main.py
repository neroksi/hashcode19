# Main file


def main():
    file = open("../dataset/a_example.txt")

    content = file.read().splitlines()
    lines = [line.rstrip('\n') for line in file]

    slide_1 = ["garden", "cat"]
    slide_2 = ["selfie", "smile", "garden"]
    s = score_slide(slide_1, slide_2)
    print(s)


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


if __name__ == '__main__':
    main()
