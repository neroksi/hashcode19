def get_content(filename):
    with open(filename, mode = 'r') as file:
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
        tags =  tokens[2:]
        assert number == len(tags)
        parsed_images.append([i,_type_,tags])
    return parsed_images

def get_parsed_images(filename):
    """
    input : filename or file path  
    output : list of lists (parsed images)
    """
    n_images, images = get_content(filename)
    parsed_images = parse_image(images)
    return parsed_images

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


