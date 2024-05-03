function newImg = direct_mapping_order_1(oldImg, factor)
    [oldRows, oldCols, channels] = size(oldImg);
    newRows = oldRows * factor;
    newCols = oldCols * factor;
    newImg = zeros(newRows, newCols, channels);

    %Corners
    newImg(1:factor:end, 1:factor:end, :) = oldImg;

    %Rows
    for chn = 1 : channels
        for row = 1 : factor : newRows
            for start = 1 : factor : newCols - factor
                x = newImg(row, start, chn);
                y = newImg(row, start + factor, chn);
                l = start + 1;
                r = start + factor - 1;
                if (x == y)
                    newImg(row, l : r, chn) = x;
                else
                    it = 0;
                    if (x < y)
                        for col = l : r
                            it = it + 1;
                            newImg(row, col, chn) = round(((y - x) / factor) * it + x);
                        end
                    else
                        for col = r : -1 : l
                            it = it + 1;
                            newImg(row, col, chn) = round(((x - y) / factor) * it + y);
                        end
                    end
                end
            end
        end
    end

    %Colums
    for chn = 1 : channels
        for col = 1 : newCols - factor + 1
            for start = 1 : factor : newRows - factor
                x = newImg(start, col, chn);
                y = newImg(start + factor, col, chn);
                u = start + 1;
                d = start + factor - 1;
                if (x == y)
                    newImg(u : d, col, chn) = x;
                else
                    it = 0;
                    if (x < y)
                        for row = u : d
                            it = it + 1;
                            newImg(row, col, chn) = round(((y - x) / factor) * it + x);
                        end
                    else
                        for row = d : -1 : u
                            it = it + 1;
                            newImg(row, col, chn) = round(((x - y) / factor) * it + y);
                        end
                    end
                end
            end
        end
    end

    %Completing rows with the same value
    for chn = 1 : channels
        for row = 1 : newRows - factor + 1
            newImg(row, newCols - factor + 2 : newCols, chn) = newImg(row, newCols - factor + 1, chn);
        end
    end

    %Completing columns with the same value
    for chn = 1 : channels
        for row = newRows - factor + 2 : newRows
            newImg(row, :, chn) = newImg(newRows - factor + 1, :, chn);
        end
    end

    newImg = uint8(newImg);
    figure, imshow(oldImg), title('Old Image');
    figure, imshow(newImg), title('New Image');
end