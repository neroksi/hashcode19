def h_to_v(imgs):
    imVs = []
    imHs = []
    for  img in imgs :
        img = img.copy()
        if img[1] == "V":
            imVs.append(img)
        else :
            imHs.append(img)

    idH = len(imHs)
    idV = len(imVs)

    L = []
    for i in range(idV):
        for j in range(idV):
            if i != j :
                img1 = imVs[i]
                img2 = imVs[j]
                img = merge_vertical(img1, img2)
                L.append(img)
            
    return imHs + L
