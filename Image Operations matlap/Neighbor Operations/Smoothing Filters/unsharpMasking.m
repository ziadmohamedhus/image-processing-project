function newImg = unsharpMasking(oldImg)
    if size(oldImg, 3) == 3
        oldImg = rgb2gray(oldImg);
    end
    weightedImg = weightedFilter(oldImg, 3);
    newImg = oldImg + (oldImg - weightedImg);
    newImg = uint8(newImg);
    subplot(1,2,1), imshow(oldImg), title('Old Image');
    subplot(1,2,2), imshow(newImg), title('New Image');
end