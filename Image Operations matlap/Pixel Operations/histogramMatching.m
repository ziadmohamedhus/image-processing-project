function newImg = histogramMatching(img1, img2)
    %Images histogram equalization
    [~, indices1] = histogramEqualization(img1);
    [~, indices2] = histogramEqualization(img2);
    %Max color
    mxc = size(indices1, 1);
    %Intial variables
    matching = zeros(mxc, 1);
    %Matching
    for i = 1 : mxc
        arr = abs(indices2 - indices1(i));
        [~, mni] = min(arr);
        matching(i) = mni - 1;
    end
    %Replacing
    [rows, cols, chns] = size(img1);
    newImg = zeros(rows, cols, chns);
    for chn = 1 : chns
        for row = 1 : rows
            for col = 1 : cols
                newImg(row, col, chn) = matching(img1(row, col, chn) + 1);
            end
        end
    end
    
    newImg = uint8(newImg);
    subplot(1, 3, 1), imshow(newImg), title('New Image');
    subplot(1, 3, 2), imshow(img1), title('Image 1');
    subplot(1, 3, 3), imshow(img2), title('Image 2');
end