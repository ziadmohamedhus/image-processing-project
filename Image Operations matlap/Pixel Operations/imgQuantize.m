function newImg = imgQuantize(oldImg, levels)
    oldImg = im2double(oldImg);
    [rows, cols, chns] = size(oldImg);
    newImg = zeros(rows, cols, chns);
    maxVal = max(oldImg(:));
    minVal = min(oldImg(:));
    range = maxVal - minVal;
    gap = range / levels;

    for chn = 1 : chns
        for row = 1 : rows
            for col = 1 : cols
                temp = oldImg(row, col) - minVal;
                index = floor(temp / gap) + 1;
                index = min(index, levels);
                index = max(index, 1);
                color = (index - 1) * gap + minVal;
                newImg(row, col) = color;
            end
        end
    end

    newImg = im2uint8(newImg);
    imshow(newImg), title('Quantized Image');
end