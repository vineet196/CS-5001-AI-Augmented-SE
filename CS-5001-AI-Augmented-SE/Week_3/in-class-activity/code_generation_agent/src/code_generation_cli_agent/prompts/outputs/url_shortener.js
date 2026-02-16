const express = require('express');
const crypto = require('crypto');
const app = express();
const PORT = 3000;

const urlMap = {};

app.use(express.json());

app.post('/shorten', (req, res) => {
  const { longUrl } = req.body;
  if (!longUrl) {
    return res.status(400).json({ error: 'longUrl is required' });
  }

  const id = crypto.randomBytes(3).toString('hex').slice(0, 6);
  urlMap[id] = longUrl;

  res.json({ id });
});

app.get('/:id', (req, res) => {
  const { id } = req.params;
  const longUrl = urlMap[id];

  if (longUrl) {
    res.redirect(302, longUrl);
  } else {
    res.status(404).send('URL not found');
  }
});

app.use((req, res) => {
  res.status(404).send('Not Found');
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});