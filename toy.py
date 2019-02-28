from ParseImages import get_parsed_images, score_slide
#filename = 'a_example.txt'
#filename = 'b_lovely_landscapes.txt'
filename = 'c_memorable_moments.txt'

#parse the images  
parsed_images = get_parsed_images(filename)

print('id: ', parsed_images[0][0])
print('type: '+parsed_images[0][1])
print(parsed_images[0][2])

import numpy as np


def merge_all(parsed_images, seed=1233):
    """
    generate a list where we merge randomly vertical images
    """
    np.random.seed(seed)
    h_images = [parsed_image for parsed_image in parsed_images if parsed_image[1]=='H' ]

    v_images = [parsed_image for parsed_image in parsed_images if parsed_image[1]=='V' ]

    nn = len(v_images)

    hh = np.random.permutation(range(nn))

    vv_images = [[(v_images[hh[2*i]][0],v_images[hh[2*i+1]][0]), 'V', 
              list(set(v_images[hh[2*i]][2]).union(v_images[hh[2*i+1]][2]))] for i in range(nn//2)]
    
    out = h_images+ vv_images
    
    return out

def score_submission(out):
    """
    evaluate the submission
    """

    N = len(out) - 1
    m = 0

    for i in range(N):
        m += score_slide(out[i][2], out[i+1][2])
    return m

out = merge_all(parsed_images, 125)
m = score_submission(out)


#permu

def run_chain(out, n_iters=1000):
    """
    ascending permutation
    
    """
    sub = out.copy()
    m = score_submission(sub)
    choices = list(range(len(out)))
    scores = [m]
    
    for i in range(n_iters):
        uu = np.random.choice(choices, 2)
        sub__ = sub.copy()
        i,j = uu[0], uu[1]
        sub__[j] = sub[i]
        sub__[i] = sub[j]
        m__ = score_submission(sub__)
        m = score_submission(sub)
        if m__>=m:
            sub = sub__.copy()
            scores.append(m__)
        else:
            scores.append(m)
    return sub, scores
        
    
    
sub, scores = run_chain(out)     
import matplotlib.pyplot as plt
plt.plot(scores)












