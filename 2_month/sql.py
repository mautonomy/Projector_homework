# 1 Task

CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    full_name VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    host_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    residents INT NOT NULL,
    price_per_night DECIMAL(10, 2) NOT NULL,
    has_ac BOOLEAN NOT NULL,
    has_refrigerator BOOLEAN NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (host_id) REFERENCES Users(user_id)
);

CREATE TABLE Reservations (
    reservation_id INT AUTO_INCREMENT PRIMARY KEY,
    room_id INT NOT NULL,
    guest_id INT NOT NULL,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id),
    FOREIGN KEY (guest_id) REFERENCES Users(user_id)
);


CREATE TABLE Reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    room_id INT NOT NULL,
    guest_id INT NOT NULL,
    rating INT NOT NULL CHECK (rating >= 1 AND rating <= 5),
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id),
    FOREIGN KEY (guest_id) REFERENCES Users(user_id)
);


# Task 2

INSERT INTO Users (user_type, name, email, password_hash, phone_number)
VALUES
('host', 'Alice Johnson', 'alice@example.com', 'password1', '123-456-7890'),
('guest', 'Bob Smith', 'bob@example.com', 'password1', '234-567-8901'),
('guest', 'Carol White', 'carol@example.com', 'password1', '345-678-9012');


INSERT INTO Rooms (host_id, title, description, residents, price_per_night, has_ac, has_refrigerator)
VALUES
(1, 'Cozy Apartment in Kyiv', 'A nice and cozy apartment in the heart of the city.', 2, 75.00, TRUE, TRUE),
(1, 'Modern Loft', 'Cool loft in the downtown.', 4, 120.00, TRUE, TRUE),
(1, 'Retro Style Villa', '70s-looking villa outskirts.', 5, 90.00, TRUE, FALSE);

INSERT INTO Reservations (room_id, guest_id, check_in_date, check_out_date, total_price)
VALUES
(1, 2, '2024-06-01', '2024-06-07', 525.00),
(2, 3, '2024-07-15', '2024-07-20', 600.00),
(3, 2, '2024-08-05', '2024-08-10', 450.00);


INSERT INTO Reviews (room_id, guest_id, rating, comment)
VALUES
(1, 2, 5, 'Lovely place.'),
(2, 3, 4, 'Great place in the heart of the city.'),
(3, 2, 5, 'Loved the villa!');

# Task 3

SELECT u.user_id, u.name, COUNT(r.reservation_id) AS reservation_count
FROM Users u
JOIN Reservations r ON u.user_id = r.guest_id
WHERE u.user_type = 'guest'
GROUP BY u.user_id, u.name
ORDER BY reservation_count

SELECT u.user_id AS host_id, u.name AS hostname, SUM(r.total_price) AS total_earnings
FROM Users u
JOIN Rooms rm ON u.user_id = rm.host_id
JOIN Reservations r ON rm.room_id = r.room_id
WHERE u.user_type = 'host'
AND r.check_out_date >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
GROUP BY u.user_id, u.name
ORDER BY total_earnings




