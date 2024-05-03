function newImg = sharpeningFilter(oldImg, sharpening)
    [rows, cols, chns] = size(oldImg);
    newImg = zeros(rows, cols, chns);
    if chns == 3
        oldImg = rgb2gray(oldImg);
    end
    if nargin < 2
        sharpening = 'point';  % Default sharpening mask option
    end
    
    % Define masks
    switch sharpening
        case 'point'
            mask = [0 -1 0; -1 5 -1; 0 -1 0];
        case 'diagonal_left'
            mask = [0 0 1; 0 0 0; -1 0 0];
        case 'diagonal_right'
            mask = [1 0 0; 0 0 0; 0 0 -1];
        case 'horizontal'
            mask = [0 1 0; 0 1 0; 0 -1 0];
        case 'vertical'
            mask = [0 0 0; 1 0 -1; 0 0 0];
        otherwise
            error('Invalid sharpening mask option. Please choose a valid option.');
    end
    
    temp = (size(mask, 1) - 1) / 2;
    padImg = padarray(double(oldImg), [temp temp], 'replicate');
    for row = 1 : rows
        for col = 1 : cols
            arr = padImg(row : row + size(mask, 1) - 1, col : col + size(mask, 1) - 1);
            newImg(row, col) = sum(sum(arr .* mask));
        end
    end
    
    newImg = uint8(newImg);
    subplot(1,2,1), imshow(oldImg), title('Old Image');
    subplot(1,2,2), imshow(newImg), title('New Image');
end