const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

// POST /bfhl endpoint
app.post('/bfhl', (req, res) => {
    const data = req.body.data || [];
    const fileB64 = req.body.file_b64 || "";

    const numbers = data.filter(item => /^\d+$/.test(item));
    const alphabets = data.filter(item => /^[a-zA-Z]$/.test(item));
    const highestLowercase = alphabets
        .filter(item => /^[a-z]$/.test(item))
        .sort()
        .pop() || "";

    const isPrime = numbers.some(num => isPrimeNumber(parseInt(num)));

    res.json({
        is_success: true,
        user_id: "ashlesha_saxena_22092001",
        email: "ashlesha@xyz.com",
        roll_number: "CSE123",
        numbers,
        alphabets,
        highest_lowercase_alphabet: highestLowercase,
        is_prime_found: isPrime,
        file_valid: !!fileB64,
        file_mime_type: fileB64 ? "application/octet-stream" : null,
        file_size_kb: fileB64 ? (Buffer.from(fileB64, 'base64').length / 1024).toFixed(2) : 0
    });
});

// GET /bfhl endpoint
app.get('/bfhl', (req, res) => {
    res.json({ operation_code: 1 });
});

function isPrimeNumber(num) {
    if (num <= 1) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) return false;
    }
    return true;
}

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
