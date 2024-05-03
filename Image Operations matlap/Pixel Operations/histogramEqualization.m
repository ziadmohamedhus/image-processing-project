function [newCounts, indices] = histogramEqualization(img)
    %Image histogram
    oldCounts = histogramCounts(img);
    indices = oldCounts;
    %Max color
    mxc = size(indices, 1);
    %Prefix sum
    for i = 2 : mxc
        indices(i) = indices(i - 1) + indices(i);
    end
    %Divide and multiply
    indices = round(indices / indices(mxc) * (mxc - 1));
    %New counts
    newCounts = zeros(mxc, 1);
    for i = 1 : mxc
        newCounts(indices(i) + 1) = newCounts(indices(i) + 1) + oldCounts(i);
    end
end