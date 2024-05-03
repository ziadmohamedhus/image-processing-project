function newImg = reverse_mapping_order_1(oldImg, factRow, factCol)
    [oldRows, oldCols, channels] = size(oldImg);
    newRows = oldRows * factRow;
    newCols = oldCols * factCol;
    rowRatio = oldRows / newRows;
    colRatio = oldCols / newCols;
    newImg = zeros(newRows, newCols, channels);

    for ch = 1:channels
        for newX = 1:newRows
            oldX = newX * rowRatio;
            x1 = floor(oldX);
            if x1 == 0
                x1 = 1;
            end
            x2 = x1 + 1;
            if x2 > oldRows
                x2 = oldRows;
            end
            x = abs(oldX - x1);
            for newY = 1:newCols
                oldY = newY * colRatio;
                y1 = floor(oldY);
                if y1 == 0
                    y1 = 1;
                end
                y2 = y1 + 1;
                if y2 > oldCols
                    y2 = oldCols;
                end
                y = abs(oldY - y1);
                p1 = oldImg(x1, y1, ch);
                p2 = oldImg(x2, y1, ch);
                p3 = oldImg(x1, y2, ch);
                p4 = oldImg(x2, y2, ch);
                z1 = p1 * (1 - x) + p2 * x;
                z2 = p3 * (1 - x) + p4 * x;
                p = z1 * (1 - y) + z2 * y;
                newImg(newX, newY, ch) = floor(p);
            end
        end
    end

    newImg = uint8(newImg);
    figure, imshow(oldImg), title('Old Image');
    figure, imshow(newImg), title('New Image');
end