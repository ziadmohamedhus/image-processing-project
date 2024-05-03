function newImg = imgsSub(img1, img2)
    [rows1, cols1, chns] = size(img1);
    [rows2, cols2, ~] = size(img2);
    minRows = min(rows1, rows2);
    minCols = min(cols1, cols2);

    if (rows1 > rows2)
        newImg = img1;
    else
        newImg = img2;
    end

    for chn = 1 : chns
        for row = 1 : minRows
            for col = 1 : minCols
                v = img1(row, col, chn) - img2(row, col, chn);
                newImg(row, col, chn) = v;
            end
        end
    end
    
    newImg = uint8(newImg);
    imshow(newImg), title('New Image');
end
