function newImg = medianFilter(oldImg, filterSize)
    if mod(filterSize, 2) == 0
        error('Filter size must be odd!');
    end
    [rows, cols, chns] = size(oldImg);
    newImg = zeros(rows, cols, chns);
    temp = (filterSize - 1) / 2;
    padImg = padarray(oldImg, [temp temp], 'replicate');
    
    for chn = 1 : chns
        for row = 1 : rows
            for col = 1 : cols
                arr = padImg(row : row + filterSize - 1, col : col + filterSize - 1, chn);
                newImg(row, col, chn) = median(arr(:));
            end
        end
    end
    
    newImg = uint8(newImg);
    subplot(1,2,1), imshow(oldImg), title('Old Image');
    subplot(1,2,2), imshow(newImg), title('New Image');
end