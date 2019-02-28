def get_content(filename):
    with open(filename, mode = 'r') as file:
        content = file.read()
        sequences = content.split('\n')
    n_images = int(sequences[0])
    images = sequences[1:-1]
    assert n_images == len(images)
    return n_images, images

def parse_image(images):
    parsed_images = []
    for i, image in enumerate(images):
        tokens = image.split(' ')
        _type_ = tokens[0]
        number = int(tokens[1])
        tags =  tokens[2:]
        assert number == len(tags)
        parsed_images.append([i,_type_,tags])
    return parsed_images

### Example ###
#filename    
filename = 'b_lovely_landscapes.txt'

# Load the images
n_images, images = get_content(filename)
print('we have %d images'%n_images)  

#parse the images  
parsed_images = parse_image(images)

print('id: ', parsed_images[0][0])
print('type: '+parsed_images[0][1])
print(parsed_images[0][2])




