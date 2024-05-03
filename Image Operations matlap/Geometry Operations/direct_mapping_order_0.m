function newImg = direct_mapping_order_0(oldImg, factor)
    [oldRows, oldCols, channels] = size(oldImg);
    newRows = oldRows * factor;
    newCols = oldCols * factor;
    newImg = zeros(newRows, newCols, channels);

    for chn = 1:channels
        for row = 1:oldRows
            for col = 1:oldCols
                newImg((row - 1) * factor + 1:row * factor, (col - 1) * factor + 1:col * factor, chn) = oldImg(row, col, chn);
            end
        end
    end

    newImg = uint8(newImg);
    figure, imshow(oldImg), title('Old Image');
    figure, imshow(newImg), title('New Image');
end