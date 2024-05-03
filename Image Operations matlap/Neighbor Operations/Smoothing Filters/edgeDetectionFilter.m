function newImg = edgeDetectionFilter(oldImg, detection)
    [rows, cols, chns] = size(oldImg);
    newImg = zeros(rows, cols, chns);
    if chns == 3
        oldImg = rgb2gray(oldImg);
    end
    if nargin < 2
        detection = 'point';  % Default mask option
    end
    
    % Define masks
    switch detection
        case 'point'
            mask = [0 -1 0; -1 4 -1; 0 -1 0];
        case 'horizontal'
            mask = [1 2 1; 0 0 0; -1 -2 -1];
        case 'vertical'
            mask = [1 0 -1; 2 0 -2; 1 0 -1];
        case 'diagonal_left'
            mask = [2 1 0; 1 0 -1; 0 -1 -2];
        case 'diagonal_right'
            mask = [0 1 2; -1 0 1; -2 -1 0];
        otherwise
            error('Invalid mask option. Please choose a valid option.');
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
    subplot(1, 2, 1), imshow(oldImg), title('Old Image');
    subplot(1, 2, 2), imshow(newImg), title('New Image');
end