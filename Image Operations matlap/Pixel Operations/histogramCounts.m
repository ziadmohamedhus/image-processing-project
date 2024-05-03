function counts = histogramCounts(img)
    [rows, cols, channels] = size(img);
    
    if channels == 3
        img = rgb2gray(img);
    end
    
    mxc = size(img, 1);
    counts = zeros(mxc, 1);
    
    for row = 1 : rows
        for col = 1 : cols
            v = img(row, col);
            counts(v + 1) = counts(v + 1) + 1;
        end
    end
end