function y = reorient(x, y, d0, epsilon);

% Translate y from x
y = y - x;
mag = norm(y);
if mag == 0,
    mag = epsilon;
end;

% Scale y to size d0
y = d0 * y / mag;

% Translate y to x
y = y + x;

end
