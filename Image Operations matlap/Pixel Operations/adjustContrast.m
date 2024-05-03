function newImg = adjustContrast(oldImg, newMin, newMax)
    if size(oldImg, 3) == 3
        oldImg = rgb2gray(oldImg);
    end
    counts = imhist(oldImg);
    oldMin = find(counts, 1);
    oldMax = find(counts, 1, 'last');
    
    newImg = uint8(round(((oldImg - oldMin) / (oldMax - oldMin)) * (newMax - newMin) + newMin));
    subplot(1,2,1), imshow(oldImg), title('Old Image');
    subplot(1,2,2), imshow(newImg), title('New Image');
end