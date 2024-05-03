function newImg = reverse_mapping_order_0(oldImg, factRow, factCol)
    [oldRows, oldCols, channels] = size(oldImg);
    newRows = oldRows * factRow;
    newCols = oldCols * factCol;
    rowRatio = oldRows / newRows;
    colRatio = oldCols / newCols;
    newImg = zeros(newRows, newCols, channels);

    for ch = 1:channels
        for newX = 1:newRows
            oldX = floor(newX * rowRatio);
            if oldX == 0
                oldX = 1;
            end
            for newY = 1:newCols
                oldY = floor(newY * colRatio);
                if oldY == 0
                    oldY = 1;
                end
                newImg(newX, newY, ch) = oldImg(oldX, oldY, ch);
            end
        end
    end

    newImg = uint8(newImg);
    figure, imshow(oldImg), title('Old Image');
    figure, imshow(newImg), title('New Image');
end