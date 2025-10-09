require('dotenv').config();
const path = require('path');
const express = require('express');
const db = require('./db');

const app = express();
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.get('/users-safe', (req, res) => {
  const name = req.query.name || '';
  const sql = "SELECT id, name, email FROM users WHERE name LIKE ?";
  db.all(sql, [`%${name}%`], (err, rows) => {
    if (err) return res.status(500).send('Error DB');
    res.render('users', { rows, q: name });
  });
});

// views/echo.ejs (usa <%= msg %>)
app.get('/echo', (req, res) => {
  const msg = req.query.msg || '';
  res.render('echo', { msg });
});

app.get('/', (req, res) => res.render('index'));

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`App en http://localhost:${port}`));