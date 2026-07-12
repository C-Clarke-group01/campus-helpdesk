CREATE DATABASE IF NOT EXISTS campus_helpdesk;
USE campus_helpdesk;

CREATE TABLE IF NOT EXISTS tickets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    requester_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    category VARCHAR(50) NOT NULL,
    title VARCHAR(150) NOT NULL,
    description TEXT NOT NULL,
    priority VARCHAR(20) DEFAULT 'Medium',
    status VARCHAR(20) DEFAULT 'Open',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

INSERT INTO tickets (requester_name, email, category, title, description, priority, status)
VALUES
('Sample Student', 'student@example.com', 'Technical', 'WiFi not working in Library', 'The WiFi keeps disconnecting on the 2nd floor of the library.', 'High', 'Open'),
('Sample Staff', 'staff@example.com', 'Facilities', 'Broken projector in Room 204', 'Projector bulb needs replacement before Monday class.', 'Medium', 'In Progress');
