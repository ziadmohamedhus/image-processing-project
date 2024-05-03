function newImg = powerTransform(oldImg, gamma)
    oldImg = im2double(oldImg);
    newImg = oldImg .^ gamma;
    newImg = im2uint8(newImg);
    subplot(1,2,1), imshow(oldImg), title('Old Image');
    subplot(1,2,2), imshow(newImg), title('New Image');
end