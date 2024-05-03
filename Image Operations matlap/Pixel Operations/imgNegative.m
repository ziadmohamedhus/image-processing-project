function newImg = imgNegative(oldImg)
newImg = 255 - oldImg;
imshow(newImg), title('New Image');
end