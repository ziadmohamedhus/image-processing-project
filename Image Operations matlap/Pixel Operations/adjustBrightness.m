function newImg = adjustBrightness(oldImg, offset)
    newImg = uint8(min(max(oldImg + offset, 0), 255));
    subplot(1,2,1), imshow(oldImg), title('Old Image');
    subplot(1,2,2), imshow(newImg), title('New Image');
end