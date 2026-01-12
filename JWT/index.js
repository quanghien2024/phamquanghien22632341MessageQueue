const express = require('express');
const jwt = require('jsonwebtoken');

const app = express();
app.use(express.json());

const SECRET_KEY = 'secret_key_123';

const users = [];

// Register
app.post('/register', (req, res) => {
    const { username, password } = req.body;
    users.push({ username, password });
    res.status(201).json({ message: 'Đăng ký thành công' });
});

// Login
app.post('/login', (req, res) => {
    const { username, password } = req.body;
    const user = users.find(
        u => u.username === username && u.password === password
    );

    if (!user) {
        return res.status(401).json({ message: 'Sai tài khoản hoặc mật khẩu' });
    }

    const token = jwt.sign(
        { username: user.username },
        SECRET_KEY,
        { expiresIn: '30s' }
    );

    res.json({ token });
});

// Protected API
app.get('/profile', (req, res) => {
    const authHeader = req.headers.authorization;
    const token = authHeader && authHeader.split(' ')[1];

    if (!token) {
        return res.status(401).json({ message: 'Chưa đăng nhập' });
    }

    jwt.verify(token, SECRET_KEY, (err, decoded) => {
        if (err) {
            return res.status(403).json({ message: 'Token hết hạn hoặc không hợp lệ' });
        }
        res.json({ message: 'Xin chào ' + decoded.username });
    });
});

app.listen(3000, () => {
    console.log('Server chạy tại http://localhost:3000');
});
