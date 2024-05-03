function newImg = imgGray(oldImg)
    r = oldImg(:, :, 1);
    g = oldImg(:, :, 2);
    b = oldImg(:, :, 3);
    newImg = 0.3 * r + 0.59 * g + 0.11 * b;
    newImg = uint8(newImg);
    subplot(1,2,1), imshow(oldImg), title('Old Image');
    subplot(1,2,2), imshow(newImg), title('New Image');
end