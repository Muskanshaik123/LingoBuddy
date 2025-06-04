const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, '../public')));

app.post('/analyze', async (req, res) => {
  try {
    const response = await axios.post('http://127.0.0.1:5000/analyze', req.body);
    res.json(response.data);
  } catch (err) {
    res.status(500).json({ error: 'NLP server error' });
  }
});

app.listen(3000, () => {
  console.log('Node.js server running at http://localhost:3000');
});
